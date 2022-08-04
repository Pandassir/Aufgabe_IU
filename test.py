# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:55:47 2022

@author: marvi
"""

import sqlalchemy as db
import pandas as pd
#2.-Turn on database engine
dbEngine=db.create_engine('sqlite:///inputdb.db') # ensure this is the correct path for the sqlite file. 

#3.- Read data with pandas
df_train = pd.read_sql('select * from train',dbEngine)
df_test = pd.read_sql('select * from test',dbEngine)
df_ideal = pd.read_sql('select * from ideal',dbEngine)

print(df_train)
print(df_test)
print(df_ideal)