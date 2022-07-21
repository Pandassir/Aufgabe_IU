#1. Traingsdaten einlesen
#2. Finden der idealen Funktiom mittels least square
#3. Visualisierung der gefundenen idealen Funktionen
    
''' laden der Bibliotheken zur Erstellumg der Dataframes'''
import pandas as pd
import numpy as np
print(pd.__version__)


''' Einlesem der CSV Datei'''
#1. Einlesen vom Trainingsdatensatz:
df_train = pd.read_csv("Datensatz/train.csv")
print('Spalten vom Trainigsdatensatz:','\n',df_train.columns.values.tolist()) #Name der Spalte: https://www.delftstack.com/de/howto/python-pandas/how-to-get-pandas-dataframe-column-headers-as-a-list/
print('Handelt es sich bei df_ideal um einen  Dataframe?:',(isinstance(df_train, pd.DataFrame)),'\n')


#1.2 Einlesen der idealen Funktionen:
df_ideal = pd.read_csv('Datensatz/ideal.csv')
print('Spalten vom Idealdatensatz:','\n',df_ideal.columns.values.tolist())
print('Handelt es sich bei df_train um einen  Dataframe?:',(isinstance(df_ideal, pd.DataFrame)),'\n')

#1.3 Entfernung der x-Spalte vom idealen Datensatz:
df_ideal.drop(['x'], axis = 1, inplace = True) #https://www.delftstack.com/de/howto/python-pandas/pandas-drop-columns-by-index/
print('Spalten vom neuen Idealdatensatz:','\n',df_ideal.columns.values.tolist())



#2 Finden der idealen Funktion:
#2. Bilden der Differrenzen:
''' Hier wurde eine Funktion erstellt. Zuerst wurde eine leere Liste initialisiert.
Mit der for - Schleife wurde jede Spalte im idealen Funktionen Datensatz itrtativ
abgearbeitet. Die Summe der Differenzen zum quadrat wird in die Liste aufgenommen.'''
def delta(spalte_train):
    mylist=[] 
    
    for name in df_ideal:
        mylist.append(sum((df_train[str(spalte_train)]-df_ideal[str(name)])**2))
    return mylist
'''Erstellung der Differenzenlisten über die delta Funktion'''
diff_list1 = delta('y1')
diff_list2 = delta('y2')
diff_list3 = delta('y3')
diff_list4 = delta('y4')

print(diff_list1)
print(diff_list1.index(min(diff_list1)))
x =list(df_ideal.columns)
print(x)

#2.1 Finden der minimalsten Abweichung:
''' An dieser Stelle wird der kleinste Wert der einzelnen Differrenzenlisten 
mittels der min Methode gesucht'''
index_min1 = (diff_list1.index(min(diff_list1)))
index_min2 = (diff_list2.index(min(diff_list2)))
index_min3 = (diff_list3.index(min(diff_list3)))
index_min4 = (diff_list4.index(min(diff_list4)))

print(index_min1)

print(df_ideal.iloc[:,index_min1])


    
#3. Visualisierung der grfundenen idealen Funktionen:
'''Zur Visualisierung wurde die Bibliothek matplotlib verwendet. Es wurde ein
Figure erstellt und anschlißend das Axes Object. Des Weiteren wurden Schönheits
verbesserungen durchgeführt.'''
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
fig, axs = plt.subplots(nrows=4, ncols=2, constrained_layout=True, figsize=(10,10))
fig.suptitle('Auswertung zu gefundenen idealen Funktionen', fontsize = 20)

axs[0][0].set(title='verauschte Funktion y1', xlabel='x - Achse', ylabel='y - Achse')
axs[0][1].set(title='ideale Funktion zu y1', xlabel='x - Achse', ylabel='y - Achse')
axs[1][0].set(title='verauschte Funktion y2', xlabel='x - Achse', ylabel='y - Achse')
axs[1][1].set(title='ideale Funktion zu y2', xlabel='x - Achse', ylabel='y - Achse')
axs[2][0].set(title='verauschte Funktion y3', xlabel='x - Achse', ylabel='y - Achse')
axs[2][1].set(title='ideale Funktion zu y3', xlabel='x - Achse', ylabel='y - Achse')
axs[3][0].set(title='verauschte Funktion y4', xlabel='x - Achse', ylabel='y - Achse')
axs[3][1].set(title='ideale Funktion zu y4', xlabel='x - Achse', ylabel='y - Achse')

axs[0][0].plot(df_train['x'],df_train['y1'])
axs[0][1].plot(df_train['x'],df_ideal.iloc[:,index_min1], color = 'black')
axs[1][0].plot(df_train['x'],df_train['y2'])
axs[1][1].plot(df_train['x'],df_ideal.iloc[:,index_min2], color = 'black')
axs[2][0].plot(df_train['x'],df_train['y3'])
axs[2][1].plot(df_train['x'],df_ideal.iloc[:,index_min3], color = 'black')
axs[3][0].plot(df_train['x'],df_train['y4'])
axs[3][1].plot(df_train['x'],df_ideal.iloc[:,index_min4], color = 'black')

axs[0][0].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1) #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
axs[0][1].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1)
axs[1][0].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1)
axs[1][1].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1)
axs[2][0].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1)
axs[2][1].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1)
axs[3][0].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1)
axs[3][1].grid(visible=True, which='major', axis='both', color='LightGrey', linestyle='--', linewidth=1)

axs[0][0].legend(['Datenpunkte verauscht y1']) #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
axs[0][1].legend(['ideal Funktion zu y1'])
axs[1][0].legend(['Datenpunkte verauscht y2'])
axs[1][1].legend(['ideal Funktion zu y2'])
axs[2][0].legend(['Datenpunkte verauscht y3'])
axs[2][1].legend(['ideal Funktion zu y3'])
axs[3][0].legend(['Datenpunkte verauscht y4'])
axs[3][1].legend(['ideal Funktion zu y4'])
plt.show()