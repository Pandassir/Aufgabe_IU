# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:55:47 2022

@author: marvi
"""

import sqlalchemy as db
import pandas as pd
#2.-Turn on database engine
dbEngine=db.create_engine('sqlite:///database.db') # ensure this is the correct path for the sqlite file. 

#3.- Read data with pandas
df_train = pd.read_sql('select * from train',dbEngine)

print(df_train)

html = df_train.to_html()
print(html)

text_file = open("index.html", "w")
text_file.write(html)
text_file.close()


import webbrowser
webbrowser.open('index.html')