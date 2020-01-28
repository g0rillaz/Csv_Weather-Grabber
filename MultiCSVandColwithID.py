import glob
import os
import pandas as pd
from colors import bcolors
import tkinter as tk
from tkinter import filedialog



path = r'Quellpath der CSV-files'
all_files = glob.glob(os.path.join(path, "*.csv"))
names = [os.path.basename(x).split('.')[-2] for x in all_files]

print(len(names))


df = pd.DataFrame()


# df = pd.DataFrame()
for file_, stationId in zip(all_files, names):
    file_df = pd.read_csv(file_, index_col=0, header=None)
    file_df['stationId'] = stationId
    print("Csv-Daten-frame der Station-Id: {} wird importiert".format(stationId))
    df = df.append(file_df)

df.to_csv(r'E:\CSV_Container\BIG-CSV_Col-stationId.csv', encoding="utf8")

print("Die Datei 'BIG-CSV_Col-stationId.csv' ist fertig! ")

