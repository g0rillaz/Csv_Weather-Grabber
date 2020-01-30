import glob
import os
import pandas as pd
# from colors import bcolors


pfad = r'Quellpath der CSV-files' # input-path
alle_datein = glob.glob(os.path.join(pfad, "*.csv"))
namen = [os.path.basename(x).split('.')[-2] for x in alle_datein] # for all paths take only the base name split it at "." take the name behind "." in all_
print("Es stehen Daten zu:",len(namen),"Stationen zur verfügung!" )

df = pd.DataFrame()

for file_, stationId in zip(alle_datein, namen):
    file_df = pd.read_csv(file_, index_col=0, header=None)
    file_df['stationId'] = stationId
    print("Csv-Daten-frame der Station-Id: {} wird importiert".format(stationId))
    df = df.append(file_df)
    
print("Die Datei wird geschrieben ")
df.to_csv(r'E:\CSV_Container\BIG-CSV_Col-stationId.csv', encoding="utf8") # # output-path
print("Die Datei 'BIG-CSV_Col-stationId.csv' ist fertig! ")
