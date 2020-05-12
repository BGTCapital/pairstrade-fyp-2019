import sys, pandas

sys.path.append('./log_helper')
sys.path.append('./model')

from process_raw_prices import generate_pair_df

csv1 = pandas.read_csv(r'C:\Users\russi\PycharmProjects\pairstrade-fyp-2019-master\model\dataset\nyse-daily-trimmed-same-length\LEAF.csv')
csv2 = pandas.read_csv(r'C:\Users\russi\PycharmProjects\pairstrade-fyp-2019-master\model\dataset\nyse-daily-trimmed-same-length\XRX.csv')

df = generate_pair_df(csv1, csv2, 52)

print(df['normalizedLogClose1'])