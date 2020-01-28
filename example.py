import pandas as pd

csv_file_list = ["sample1.csv", "sample2.csv"]


list_of_dataframes = []

for filename in csv_file_list:
    list_of_dataframes.append(pd.read_csv(filename))


merged_df = pd.concat(list_of_dataframes) # "pd.concat" mergerd die listen aus list_of_dataframes[] in merged_df rein die sich wiederum ausgeben lässt

print(merged_df)
