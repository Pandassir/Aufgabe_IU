#1. Traingsdaten einlesen
#2. Finden der idealen Funktiom mittels least square
#3. Visualisierung der gefundenen idealen Funktionen

def main():   
    ''' laden der Bibliotheken zur Erstellumg der Dataframes'''
import pandas as pd
import numpy as np
print(pd.__version__)


''' Einlesem der CSV Datei'''
#1. Einlesen vom Trainingsdatensatz:
df_train = pd.read_csv("Datensatz/train.csv")

#1.2 Einlesen der idealen Funktionen:
df_ideal = pd.read_csv('Datensatz/ideal.csv')

#1.3 Entfernung der x-Spalte vom idealen Datensatz:
df_ideal.drop(['x'], axis = 1, inplace = True) #https://www.delftstack.com/de/howto/python-pandas/pandas-drop-columns-by-index/

#1.4 Einlesen der Testdaten:
df_test = pd.read_csv('Datensatz/test.csv')
#df_test = df_test.sort_values(by=['x'], ascending=True) # nach absteigender Reihenfolge sortieren, https://www.delftstack.com/de/api/python-pandas/pandas-dataframe-dataframe.sort_values-function/

    
def show_datasets():
    print('Spalten vom Trainigsdatensatz:','\n',df_train.columns.values.tolist()) #Name der Spalte: https://www.delftstack.com/de/howto/python-pandas/how-to-get-pandas-dataframe-column-headers-as-a-list/
    print('Handelt es sich bei df_ideal um einen  Dataframe?:',(isinstance(df_train, pd.DataFrame)),'\n')
    print(df_train)
    
    print('Spalten vom originalen Idealdatensatz:','\n',df_ideal.columns.values.tolist())
    print('Handelt es sich beim org. Idealdatensatz um einen  Dataframe?:',(isinstance(df_ideal, pd.DataFrame)),'\n')
    print(df_ideal)
    
    print('Spalten vom neuen Idealdatensatz:','\n',df_ideal.columns.values.tolist())
    print(df_ideal)
    
    print('Spalten vom Testdatensatz:','\n',df_test.columns.values.tolist())
    print('Handelt es sich beim Testdatensatz um einen  Dataframe?:',(isinstance(df_test, pd.DataFrame)),'\n')  
    print(df_test) 
# show_datasets()    

#2 Finden der idealen Funktion:
#2.1 Bilden der Differrenzen:
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

def show_diff():
    print('Differenzenliste 1')
    print(diff_list1)
    print(diff_list1.index(min(diff_list1)))
    x =list(df_ideal.columns)
    print(x)
#show_diff()

#2.1 Finden der minimalsten Abweichung:
''' An dieser Stelle wird der kleinste Wert der einzelnen Differrenzenlisten 
mittels der min Methode gesucht'''
index_min1 = (diff_list1.index(min(diff_list1)))
index_min2 = (diff_list2.index(min(diff_list2)))
index_min3 = (diff_list3.index(min(diff_list3)))
index_min4 = (diff_list4.index(min(diff_list4)))

def index_min_show():
    print(index_min1)
    print(index_min2)
    print(index_min3)
    print(index_min4)

    print(df_ideal.iloc[:,index_min1])
# index_min_show()

    
#3. Visualisierung der grfundenen idealen Funktionen:
'''Zur Visualisierung wurde die Bibliothek matplotlib verwendet. Es wurde ein
Figure erstellt und anschlißend das Axes Object. Des Weiteren wurden Schönheits
verbesserungen durchgeführt.'''

from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

def vis_train_ideal():

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
#vis_train_ideal()

#3.2 Visualisierung des Testdatensatzes:

def vis_testdata():
    fig, axs = plt.subplots(nrows=1, ncols=1, constrained_layout=True, figsize=(10,8))
    fig.suptitle('Testdatensatz', fontsize = 20)
    axs.set(xlabel='x - Achse', ylabel='y - Achse')
    axs.scatter(df_test['x'],df_test['y'],color= 'black', linewidth=0.1 ) # Hier wurde plot gegen scatter getauscht, https://www.geeksforgeeks.org/matplotlib-axes-axes-scatter-in-python/
    axs.grid(visible=True, which='major', axis='both', color='white', linestyle='-', linewidth=1)
    axs.set_facecolor('LightGray')
    axs.legend(['Testdaten'], fontsize = 15, facecolor='white') #facecolor https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html

#vis_testdata()



#4. Suchen vom maximalen Delta der einzelnen Datenpunkte in der Trainingsdaten
# vs. idealen Daten:
print('AB HIER DELTA')


    
def max_delta(trainingsdaten, index_min_ideal):
    return abs((df_train[str(trainingsdaten)]-(df_ideal.iloc[:,index_min_ideal])).max()) # Mit abs auf das gesamte Ergebnis, bekommt man die positive wahre Differenz
     
#wenn der Doppelpunkt weg ist, iteriert er nur einmal die komplette Spalete /df_ideal.iloc[index_min_ideal] bei df_ideal.iloc[:,index_min_ideal] iteriert 400x!
import math

max_diff_y1 = (max_delta('y1',index_min1))*(math.sqrt(2))
max_diff_y2 = (max_delta('y2',index_min2))*(math.sqrt(2))
max_diff_y3 = (max_delta('y3',index_min3))*(math.sqrt(2))
max_diff_y4 = (max_delta('y4',index_min4))*(math.sqrt(2))
print (max_diff_y1)
print (max_diff_y2)
print (max_diff_y3)
print (max_diff_y4)
    
def min_list():
    mylist = []
    for num in df_test['x']:
        x = math.sqrt((num-df_train['x'])**2)
        y = abs(x)
        mylist.append(min(y))
        
    return mylist
x = min_list()
print(sorted(x))

def test():
    mylist = []
    for num in x:
        if num < 0.36:
            mylist.append(num)
    return mylist
x = test()
print(x)

print(abs(df_train['x']-df_ideal['y36']))

    
    
    