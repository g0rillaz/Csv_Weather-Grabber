# https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe/21232849#21232849


"""Import multiple csv files into pandas and concatenate into one DataFrame"""


import pandas as pd
import glob

path = r'C:\Users\Jipsy\PycharmProjects\singlePandasDF_from.csvPython\csv_files' # use your path
all_files = glob.glob(path + "/*.csv")

# print(all_files)

li = []

for filename in all_files:
    #  print(li)
    df = pd.read_csv(filename, index_col=None, header=0) #.head(3) # head(rows) nimm die ersten drei Zeilen. TODO:: Muss raus wenns fertig ist und auf alle daten angewandt werden


    df["StationID"] = filename.split("")[:-1]
    #print(filename)

    # In this case it might make sense to use a list comprehension to strip all of the extra spaces.
    # df.columns = [col.strip() for col in df.columns]
    #print(df.iloc[1:4]) # Spalte 1 bis 4 ausgeben
    li.append(df) # is klar

frame = pd.concat(li, axis=0, ignore_index=False, sort=False) # Concatenate all data into one DataFrame
print(frame.head())
# print(frame)

frame.to_csv(r'E:\CSV_Container\File export_Frame2.csv', encoding="utf8", index=False, header=False)

# boom Using this answer allowed me to add new column with the file name eg with df['filename'] = os.path.basename(file_)
"""df['filename'] = os.path.basename(file_)"""

