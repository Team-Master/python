import numpy as np
import pandas as pd
import os

base_dir = 'data'
file_nm = 'df.xlsx'
xls_dir = os.path.join(base_dir, file_nm)

df = pd.DataFrame({
  'group': ['a', 'b', 'c', 'd'],
  'value_1': [10, 20, 30, 40],
  'value_2': [100, 200, 300, 400]
},
index = [1, 2, 3, 4 ])

df.to_excel(
  xls_dir,
  sheet_name = 'Sheet1', 
  na_rep = 'NaN', 
  float_format = "%.2f", 
  header = True, 
  # columns = ["group", "value_1", "value_2"], # if header is False
  index = True, 
  index_label = 'id', 
  startrow = 1, 
  startcol = 1, 
  # engine = 'xlsxwriter', 
  freeze_panes = (2, 0)
)
