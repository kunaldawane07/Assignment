import seaborn as sns
import pandas as pd
from django.shortcuts import render
from io import BytesIO
import base64
from matplotlib import pyplot as plt
from .forms import UploadFileForm

# for upload csv file
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            # for reading the csv file
            data = pd.read_csv(file)

            # for include a numeric data
            numeric_data = data.select_dtypes(include='number')

            # for calculating mean, median, standart deviation
            stats = {
                'Mean': numeric_data.mean(),
                'Median': numeric_data.median(),
                'Standard Deviation': numeric_data.std()
            }

            # convert statistics data into html format
            stats_html = '<table border="1"><thead><tr><th>Statistic</th>'
            stats_html += ''.join([f'<th>{col}</th>' for col in numeric_data.columns])
            stats_html += '</tr></thead><tbody>'
            
            for stat_name, stat_values in stats.items():
                stats_html += f'<tr><td>{stat_name}</td>'
                for col in numeric_data.columns:
                    stats_html += f'<td>{stat_values[col]:.2f}</td>'
                stats_html += '</tr>'
            
            stats_html += '</tbody></table>'

            # handling missing value
            missing_values = data.isnull().sum()

            # for printing data 
            print("Data Head:")
            print(data.head())
            print("Statistics:")
            print(stats_html)

            # create plot using seaborn
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(numeric_data, ax=ax)
            plt.tight_layout()

            # save plot in to bytesio format
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_png = buf.getvalue()
            buf.close()

            # converting image based format
            image_base64 = base64.b64encode(image_png).decode('utf-8')

            # returning all values
            return render(request, 'result.html', {
                'data': data.head().to_html(),
                'summary': stats_html,
                'image_base64': image_base64
            })
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
