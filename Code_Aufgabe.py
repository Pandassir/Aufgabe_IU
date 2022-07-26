#1. CSV-Dateien einlesen
#2. Finden der idealen Funktiom mittels least square
#3. Visualisierung der gefundenen idealen Funktionen
#4. Suchen von der maximalen Abweichung von den Traingsdaten minus ideale Daten!
#5. Präsentation Validierungsergebnis:
    
        
    
    
   
''' laden der Bibliotheken zur Erstellumg der Dataframes'''
import pandas as pd
import numpy as np
print('Welche pandas Version wird verwendet?:', pd.__version__,'\n')






#1. Einlesen vom Trainingsdatensatz: #https://pynative.com/python-pandas-read-csv/
''' Einlesem der CSV Datei'''
df_train = pd.read_csv("Datensatz/train.csv")
#1.2 Einlesen der idealen Funktionen:
df_ideal = pd.read_csv('Datensatz/ideal.csv')
df_ideal2 = pd.read_csv('Datensatz/ideal.csv')
#1.3 Entfernung der x-Spalte vom idealen Datensatz:
df_ideal.drop(['x'], axis = 1, inplace = True) #https://www.delftstack.com/de/howto/python-pandas/pandas-drop-columns-by-index/
#1.4 Einlesen der Testdaten:
df_test = pd.read_csv('Datensatz/test.csv')
    

    
def show_datasets():
    print('Trainingsdatensatz:','\n', df_train,'\n')
    print('Spalten vom Trainigsdatensatz:','\n',df_train.columns.values.tolist(),'\n') #Name der Spalte: https://www.delftstack.com/de/howto/python-pandas/how-to-get-pandas-dataframe-column-headers-as-a-list/
    print('Handelt es sich bei df_train um einen  Dataframe?:',(isinstance(df_train, pd.DataFrame)),'\n')
    
    print('Idealdatensatz:','\n', df_ideal2,'\n')
    print('Spalten vom originalen Idealdatensatz:','\n',df_ideal2.columns.values.tolist(),'\n')
    print('Handelt es sich beim org. Idealdatensatz um einen  Dataframe?:',(isinstance(df_ideal2, pd.DataFrame)),'\n')
    
    print('Idealdatensatz x raus genommen:','\n', df_ideal,'\n')
    print('Spalten vom neuen Idealdatensatz:','\n',df_ideal.columns.values.tolist(),'\n')
    print('Handelt es sich beim gek. Idealdatensatz um einen  Dataframe?:',(isinstance(df_ideal, pd.DataFrame)),'\n')
    
    print('Testdatensatz:','\n', df_test,'\n')
    print('Spalten vom Testdatensatz:','\n',df_test.columns.values.tolist(),'\n')
    print('Handelt es sich beim Testdatensatz um einen  Dataframe?:',(isinstance(df_test, pd.DataFrame)),'\n')  
    
#show_datasets()    





#2 Finden der idealen Funktion:
''' Hier wurde eine Funktion erstellt. Zuerst wurde eine leere Liste initialisiert.
Mit der for - Schleife wurde jede Spalte im idealen Funktionen Datensatz itertativ
abgearbeitet. Die Summe der Differenzen zum quadrat wird in die Liste aufgenommen.
Danach wird der Index der kleinsten Summe in der Tabelle ermittelt. Dieser
Index + 1 ist der gesuchte ideale y-Datensatz.'''
def delta(spalte_train):
    mylist=[] 
    
    for name in df_ideal:
        mylist.append(sum((df_train[str(spalte_train)]-df_ideal[str(name)])**2))
    #return mylist
    index_min = (mylist.index(min(mylist)))
    print(f'Zu den {spalte_train} Trainigsdaten gehört die ideale Fynktion: y{index_min +1}')
    return index_min


print('Hier die gefundenen idealen Funktionen:')
index_min1 = delta('y1')
index_min2 = delta('y2')
index_min3 = delta('y3')
index_min4 = delta('y4')
print('\n')




    
#3. Visualisierung der gefundenen idealen Funktionen:
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
    plt.show()
#vis_testdata()





#4. Suchen von der maximalen Abweichung von den Traingsdaten minus ideale Daten!
''' '''    
def max_delta(trainingsdaten, index_min_ideal):
    return abs((df_train[str(trainingsdaten)]-(df_ideal.iloc[:,index_min_ideal])).max()) # Mit abs auf das gesamte Ergebnis, bekommt man die positive wahre Differenz
     
import math
max_diff_y1 = (max_delta('y1',index_min1))*(math.sqrt(2))
max_diff_y2 = (max_delta('y2',index_min2))*(math.sqrt(2))
max_diff_y3 = (max_delta('y3',index_min3))*(math.sqrt(2))
max_diff_y4 = (max_delta('y4',index_min4))*(math.sqrt(2))

def show_max_delta():
    print ('Hier die max. Differenzen:')
    print (f'Abweichung y1(train) zu y{index_min1+1}(ideal): ',max_diff_y1)
    print (f'Abweichung y1(train) zu y{index_min2+1}(ideal): ',max_diff_y2)
    print (f'Abweichung y1(train) zu y{index_min3+1}(ideal): ',max_diff_y3)
    print (f'Abweichung y1(train) zu y{index_min4+1}(ideal): ',max_diff_y4)
    print ('Die max. allgemeine Abweichung wird auf 0,71 festgelegt.')
#show_max_delta()





#5. Präsentation Validierungsergebnis:
def val():
    
    while True:
        '''Hier wird mit der merge Methode der Testdatensatz und der ideale Datensatz,
        zusammengelegt. Dabei wurde x als Variable gewählt. Pandas sucht hier die 
        gemeinsame Schnittmenge der x- Werte und die restlichen x-Werte fliegen raus!'''
        df_test_sort = df_test.sort_values(by=['x'], ascending=True) #nach absteigender Reihenfolge sortieren, https://www.delftstack.com/de/api/python-pandas/pandas-dataframe-dataframe.sort_values-function/
        df_merged_test = df_test_sort.merge(df_ideal2, on = 'x')
        
        ''' Initialisierung einer Liste, welche später hilft Spalten zu e
        entfernen'''
        remove_list = list(range(2,52))
        num = int(input('Für welchen idealen Datensatz wollen Sie die dazugehörigen'
                    'Testdaten?\nWähle zwischen y2,y11,y33 oder y36.\n'
                    'Hier die Eingabe y:'))
        remove_list.remove(num+1)
        '''Entfernung unnötiger Spalten aus DF'''
        df_merged_test.drop(columns = df_merged_test.columns[remove_list], inplace = True) #Spalten entfernen
        '''Einfügen der Abweichungsspalte'''
        df_merged_test.insert(loc=3, column = f'Diff y{num}', value =abs(df_merged_test['y']-df_merged_test[f'y{num}'])) #https://www.youtube.com/watch?v=IKiDSOUTQX8
        '''Erzeugung einer Maske mit Bedingungen'''
        df_mask=df_merged_test[f'Diff y{num}']<= 0.71 #https://www.delftstack.com/de/howto/python-pandas/how-to-filter-dataframe-rows-based-on-column-values-in-pandas/
        ''' Maske auf Dataframe anwenden'''
        filtered_df = df_merged_test[df_mask]
            
        fig, axs = plt.subplots(nrows=1, ncols=1, constrained_layout=True, figsize=(8,8))
        fig.suptitle(f'Ideale Funktion y({num}) vs. Testdaten', fontsize = 20)
        axs.set(xlabel='x - Achse', ylabel='y - Achse')        
        axs.scatter(filtered_df['x'],filtered_df['y'])
        if num == 2:
            axs.plot(df_train['x'],df_ideal.iloc[:,index_min3], color = 'black')
        elif num == 11:
            axs.plot(df_train['x'],df_ideal.iloc[:,index_min2], color = 'black')
        elif num == 33:
            axs.plot(df_train['x'],df_ideal.iloc[:,index_min4], color = 'black')
        else:
            axs.plot(df_train['x'],df_ideal.iloc[:,index_min1], color = 'black')         
        axs.legend([(f'ideale Funktion {num}'),('Testdaten (+/- 0,71)')], fontsize = 15, facecolor='white')
        print(filtered_df)
        plt.show()
        
        quest = str(input('Wollen Sie ein weiteren Datensatz auslesen? Y/N:'))
        if quest.lower() == 'y':
            continue
        else:
            break
#val()



#6. Hinzufügen der gefoderten Datensätze mySQL'''
''' Zuerst wurde aus Punkt 5 einen Teil vom Code entnommen und dafür verwendet
die Dataframes mit den Abweichungen von den Testdaten zu Idealdaten zu bekommen.'''
def get_selceted_df(num):
        df_test_sort = df_test.sort_values(by=['x'], ascending=True) #nach absteigender Reihenfolge sortieren, https://www.delftstack.com/de/api/python-pandas/pandas-dataframe-dataframe.sort_values-function/
        df_merged_test = df_test_sort.merge(df_ideal2, on = 'x')
        
        ''' Initialisierung einer Liste, welche später hilft Spalten zu e
        entfernen'''
        remove_list = list(range(2,52))
        remove_list.remove(num+1)
        '''Entfernung unnötiger Spalten aus DF'''
        df_merged_test.drop(columns = df_merged_test.columns[remove_list], inplace = True) #Spalten entfernen
        '''Einfügen der Abweichungsspalte'''
        df_merged_test.insert(loc=3, column = f'Diff y{num}', value =abs(df_merged_test['y']-df_merged_test[f'y{num}'])) #https://www.youtube.com/watch?v=IKiDSOUTQX8
        '''Erzeugung einer Maske mit Bedingungen'''
        df_mask=df_merged_test[f'Diff y{num}']<= 0.71 #https://www.delftstack.com/de/howto/python-pandas/how-to-filter-dataframe-rows-based-on-column-values-in-pandas/
        ''' Maske auf Dataframe anwenden'''
        filtered_df = df_merged_test[df_mask]
        return filtered_df
    
df_y2_selected = get_selceted_df(2)
df_y11_selected = get_selceted_df(11)
df_y33_selected = get_selceted_df(33)
df_y36_selected = get_selceted_df(36)

def show_sel():
    print(df_y2_selected,'\n')
    print(df_y11_selected,'\n')
    print(df_y33_selected,'\n')
    print(df_y36_selected,'\n')
#show_sel()


#def my_sql():
#Import the neccessary modules
from sqlalchemy import create_engine as ce
# restlichen Dataframes hochladen
# Alles genau dokumentieren
# Verbindung zum MySQL-Server bei localhost mit PyMySQL DBAPI 
''' DBAPI pymysql wurde zuerst über pip install pymysql installiert. Das hat 
nicht funktioniert. Anschließend wurde pymysql in der Anaconda Umgebung installiert.
Danach hat der Code funktioniert.'''
engine  =  ce ( 'mysql+pymysql://root:pass123@localhost:3306/dfs_aufgabe' ) # https://overiq.com/sqlalchemy-101/installing-sqlalchemy-and-connecting-to-database/
engine.connect()
df_ideal2.to_sql('datensatz_ideal', engine)
df_train.to_sql('datensatz_training', engine)
df_test.to_sql('datensatz_test', engine)
df_y2_selected.to_sql('datensatz_test_vs_y2_ideal', engine)
df_y11_selected.to_sql('datensatz_test_vs_y11_ideal', engine)
df_y33_selected.to_sql('datensatz_test_vs_y33_ideal', engine)
df_y36_selected.to_sql('datensatz_test_vs_y36_ideal', engine)
''' Die Tabellen können optional über diese Methode abgerufen werden'''
#df = pd.read_sql_table('datensatz_ideal', engine)  #https://de.acervolima.com/lesen-sie-die-sql-datenbanktabelle-mit-sqlalchemy-in-einen-pandas-dataframe/
#print(df)
def show_html():
    '''Zur Visualisierung wurde die Dataframes in MySQL visualisiert über 
    select * from datensatz_ideal; und die Grafik wurde gespeichert. 
    Diese Grafik wird hier visualisert:'''
    # import module
    import webbrowser   #https://www.geeksforgeeks.org/creating-and-viewing-html-files-with-python/
    # open html file
    webbrowser.open('datensatz_train.html')
    webbrowser.open('datensatz_ideal.html')
    webbrowser.open('datensatz_test.html')
    webbrowser.open('datensatz_test_vs_y2_ideal.html')
    webbrowser.open('datensatz_test_vs_y11_ideal.html')
    webbrowser.open('datensatz_test_vs_y33_ideal.html')
    webbrowser.open('datensatz_test_vs_y36_ideal.html')
show_html()






# In My SQL Tabellen Abfragen : https://www.youtube.com/watch?v=mBFI7jm7eRg