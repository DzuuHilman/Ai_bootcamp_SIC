import numpy as np
import pandas as pd
import matplotlib.pyplot as plt         #used for animating data
import seaborn as sns                   #used for improve matplotlib animation

pd.options.display.max_columns = None
pd.options.display.max_rows= None
pd.options.display.width = None
pd.options.display.expand_frame_repr = False

sales_df = pd.read_csv("D:\Pendidikan\Pelatihan\Samsung Inovation Campus Batch 5\Stage 3 - AI bootcamp\sales_data_sample.csv", encoding= 'latin-1', encoding_errors='replace')

print(sales_df.head(3)) 