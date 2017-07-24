#Python 3.5+
#Concatenate Excel files.
#Require Pandas module. Installed with Anacoda distribution
#http://pandas.pydata.org/pandas-docs/stable/install.html
#http://stackoverflow.com/questions/25400240/using-pandas-combining-merging-2-different-excel-files-sheets
#http://chrisalbon.com/python/pandas_dataframe_importing_csv.html

import os
import glob
import pandas

df = pandas.DataFrame()

for f in glob.iglob('.\*.xlsx',recursive=False):
    data = pandas.read_excel(f, 0, skiprows=3)
    df = df.append(data)

df.to_excel("all.xls")
