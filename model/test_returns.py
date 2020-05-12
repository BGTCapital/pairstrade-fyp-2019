import pandas as pd
import os

rootdir = r'C:\Users\russi\PycharmProjects\pairstrade-fyp-2019-master\model\dataset\nyse-daily-trimmed-same-length'

start_date = '2017-03-20'
end_date = '2018-01-02'
combined_return = 0
total_assets = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".csv"):
            df = pd.read_csv(filepath, index_col=False)

            start_val = float(df[df['date'] == start_date]['close'])
            end_val = float(df[df['date'] == end_date]['close'])

            combined_return += end_val / start_val - 1

            total_assets += 1

print(combined_return / total_assets)