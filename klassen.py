# 1.import datas managing from sqlite:
import sqlalchemy as db
import pandas as pd

# 1.1 turn on database engine:   
dbEngine=db.create_engine('sqlite:///database.db')                               # ensure this is the correct path for the sqlite file.

''' Hier wird eine Verbindung zu der Datenbank 'MySQL' hergestellt. Damit
der Datentransfer von Datenbamk zu Python und umgekehrt ohne Probleme
funktioniert wird Sqlalchemy verwendet. Dies ist eine Art Zwischenschicht
und hilft den Datentransfer richtig zu organisieren'''



# 1.2 create a class for downloading and uploading datas:
class Datentabelle:  
    '''
    Hier entsteht eine Klasse Datentabelle. Dises Klasse soll dabei helfen
    übersichtlich die Tabellen aus MySQL zu downloaden und umgekehrt uploaden.
    '''
    
    def __init__(self, tablename):
        '''     
        Parameters
        ----------
        tablename : (string)
            Name der gewählten Tabelle
        Returns
        -------
        Initialisiert ein neues Objekt Datentabelle
        '''
        
        self.tablename = tablename # Name der 
                  
    def downlaod(self):
        '''        
        Returns
        -------
        Ladet aus MySQL die Tabelle in Python und wandelt die Tabelle mit
        Hilfe von Pandas in einen Dataframe um
        '''

        return pd.read_sql(f'select * from {self.tablename}',dbEngine)
        
        
        
    def upload_as(self, name):
        '''        
        Parameters
        ----------
        dataframe : Dataframe
            Als Parameter muss der gewünschte Dataframe angegeben werden
        Returns
        -------
        Ladet einen Dataframe in MySQL hoch
        '''
        self.tablename.to_sql(name, dbEngine, if_exists='fail')
        
df_train = Datentabelle('train') .downlaod() 
df_ideal = Datentabelle('ideal') .downlaod() 
df_test  = Datentabelle('test') .downlaod() 
df_test.sort_values(by=['x'], inplace=True)                                     # sorts the dataframe
#print(df_train) 
#print(df_ideal) 
#print(df_test) 
#Datentabelle(df_train).upload_as('df_train')
        
        
        
class TrainDataProvider(Datentabelle):
    '''
    Hier entsteht eine Klasse die die Erstellung eines Dataframes von x und dem
    entsprechenden y Wert organisiert. Die restlichen Werte werden gefiltert.
    Zudem wurde hier eine Vererbung der Klasse 'Datentabelle' eingebaut.
    '''
    
    def __init__(self, y_train, tablename = 'train'):
        '''
        Parameters
        ----------
        y : (string)
            Name des gewählten y-Wertes
        tablename : (string)
            Name des Datendatzes
        Returns
        -------
        Initialisiert ein neues Objekt TrainDataProvider
        '''
        super().__init__(tablename = 'train')
        self.y_train = y_train
        
    def create(self):
        '''
        
        Returns
        -------
        Dataframe
            Hier entsteht ein Dataframe mit x und einem gewählten y-Wert
        '''
        #df_train = Datentabelle(self.tablename).downlaod() 
        #df_train = pd.read_sql(f'SELECT * FROM {self.tablename}', con=engine)
        return df_train.filter(['x', self.y_train])

    






    

class IdealFunktionProviderFor(TrainDataProvider):
    '''
    Hier entstent eine Klasse die die ideale Funktion zu den Trainingsdaten
    findet. Zudem wurde hier eine Vererbung der Klasse 'TrainDataProvider'
    eingebaut.
    '''
    def __init__(self, y_train, tablename = 'train'):
        '''
        
        Parameters
        ----------
        y : (string)
            Name des gewählten y-Wertes
        tablename : (string)
            Name des Datendatzes
        Returns
        -------
        Initialisiert ein neues Objekt IdealFunktionProvider
        
        '''
        self.y_train = y_train
    
    def find(self):
        '''
        
        Returns
        -------
        Dataframe
            Hier wird die best passende ideale Funktion zu den einzelnen 
            Trainingsdaten gesucht. Anschließend wird ein wird der Dataframe
            gefiltert, sodass nur die x-Werte und die y-Werte der idealen
            Funktion übrig bleiben.
            
        '''
        #df_train = Datentabelle(self.tablename).downlaod() 
        #df_train = Datentabelle('train').downlaod() 
        #df_ideal = Datentabelle('ideal').downlaod()
        df_ideal = Datentabelle('ideal') .downlaod() 
        df_ideal.drop(['x'], axis = 1, inplace = True)
        
        mylist=[] 
        
        for name in df_ideal:
            mylist.append(sum((df_train[self.y_train]-df_ideal[str(name)])**2))
        index_min = (mylist.index(min(mylist)))        
        df_ideal = Datentabelle('ideal').downlaod() # originaler df_ideal geladen, weil oben x herausgenommen wurde.
        return df_ideal.filter(['x',f'y{index_min+1}'])
    
    def show_dataframe(self):
        ''' 
        Zeigt den Dataframe der gefundenen idealen Funktion an
        '''
        print(IdealFunktionProviderFor(self.y_train).find())
    
    def show_columnname(self):
        '''
        Zeigt den Spaltennamen der oben gefundenen ideealen Funktion an
        '''
        
        print(f'Zu den {self.y}-Werten vom Trainigsdaten gehört die ideale Funktion:'
              ,((IdealFunktionProviderFor(self.y_train).find()).columns[1]))
        
        
#IdealFunktionProviderFor('y1').show_dataframe()




        
class MaxDeltaFinder(TrainDataProvider):
    
    '''
    Hier ensteht eine Klasse, welche aus dem Trainigsdatendatz und dem 
    Idealdatensatz die maximalen Abweichungen zwischen den  einzelnen 
    Trainingsdatensätze y1-y4 und deren gefundenen idealen Funktionen ermittelt.
    '''
    
    def __init__(self, y_train):
        
        '''
        Parameters
        ----------
        y : (string)
            Name des gewählten y-Wertes
        
        Returns
        -------
        Initialisiert ein neues Objekt TrainDataProvider
        '''
        
        super().__init__(y_train)
    
    def find(self):
        
        '''
        Returns
        -------
        Gibt die maximale Abweichung zwischen den einzelnen Trainingsdatensätze
        (y1-y4) und den entsprechenden gefundenen Idealdatensätze aus. Diese
        Abweichungen wurden mit dem Faktor sqrt(2) multipliziert. Diese Abweichung
        wird als Grenze zur Selektion der Testdaten verwendet. Liegt der
        der Datenpunkt unter der Abweichung gehört er zur idealen Funktion,
        wenn nein, dann gehört dieser nicht dazu.
        '''
        
        import math
        df_train_xy = TrainDataProvider(self.y_train).create()                        # Laden des Trainingdatensatzes
        #df_train_xy.drop(['x'], axis = 1, inplace = True)                      # Löschen der x -Spalte
        df_ideal = IdealFunktionProviderFor(self.y_train).find()                         # Laden des Trainingdatensatzes
        #df_ideal.drop(['x'], axis = 1, inplace = True)                         # Löschen der x -Spalte
        
        maxdelta = abs((df_train_xy.iloc[:,1]-df_ideal.iloc[:,1]).max())
        faktordelta = maxdelta*(math.sqrt(2))
        return faktordelta
    
    def show_maxdelta(self):
        
        '''
        Zeigt den Zahlenwert der maximalen Abweichung an
        '''
        
        print(f'Die maximale Abweichung zwischen {self.y_train} und',
              (IdealFunktionProviderFor(self.y_train).find()).columns[1],'ist:',
              MaxDeltaFinder(self.y_train).find())

#MaxDeltaFinder('y1').show_maxdelta()    
        
        
        
    
class TestDataFinder:
    '''
    Hier ensteht eine Klasse, welche zu einer Idealfunktion die passenden 
    Testdaten aus dem kompletten Testdatensatz ermittelt.
    '''
     
    def __init__(self, y_idealfunktion):
        
        '''
        Parameters
        ----------
        y_idealfunktion : (string)
            Spaltenname der gewählten idealen Funktion
        
        Returns
        -------
        Initialisiert ein neues Objekt TrainDataFinder
        '''
        
        self.y_idealfunktion = y_idealfunktion
         
    def find(self):
        
        '''
        Returns
        -------
        Rückgabe eines Dataframes mit den x+y- Werten des Testdatensatzes,
        der y - Werte von der gewählten idealen Funktion und die Differenz der 
        beiden y -Werten. Alle Werte über der maximalen Abweichung werden
        aussortiert.
        '''
        
        md1 = MaxDeltaFinder('y1').find()                                       # Findet die maximale Abweichung zwischen y1-Traingsdatensatz und dem dazugehörigen Idealdatensatz
        md2 = MaxDeltaFinder('y2').find()                                       # Findet die maximale Abweichung zwischen y2-Traingsdatensatz und dem dazugehörigen Idealdatensatz
        md3 = MaxDeltaFinder('y3').find()                                       # Findet die maximale Abweichung zwischen y3-Traingsdatensatz und dem dazugehörigen Idealdatensatz
        md4 = MaxDeltaFinder('y4').find()                                       # Findet die maximale Abweichung zwischen y4-Traingsdatensatz und dem dazugehörigen Idealdatensatz
         
        md_avrg = (md1+md2+md3+md4)/4  
        
        print(md_avrg)
         
        df_ideal = Datentabelle('ideal') .downlaod() 
        df_test  = Datentabelle('test') .downlaod() 
        df_test.sort_values(by=['x'], inplace=True)                              # Laden der Idealdaten
        df_merged_test = df_test.merge(df_ideal, on = 'x')                      # Zusammenfügen vom Testdatensatz und Idealdatensatz, aber nur die gemeinsamen x - Werte
        df_merged_test = df_merged_test.filter(['x','y', self.y_idealfunktion])                  # Erstellung eines Dateframes mit den x und y- Werten des Trainingsdatensatzes und den y- Werten des Idealdatendatzes
        df_merged_test.insert(loc=3, column = f'Diff {self.y_idealfunktion}',   # Einfügen einer Spalte, welche die Differenz zwischen den y- Werten vom Trainingsdatensatz und dem Idealdatensatz anzeigt
        value =abs(df_merged_test['y']-df_merged_test[self.y_idealfunktion]))   
        #df_mask=df_merged_test[f'Diff {self.y_idealfunktion}']<= 0.71
        df_mask=df_merged_test[f'Diff {self.y_idealfunktion}']<= 0.71        # Erstellung einer Maske wo nur Werte < max. Abweichung einer ausgewählten Spalte erstellt
        filtered_df = df_merged_test[df_mask]                                   # Aktivierung der Maske auf den Dataframe. Übrig bleiben die Indexzeilen, der zuvor erstellten Spalte mit den gefilterten Werten
        return filtered_df                                                      # Rückgabe eines Dataframes mit den x+y- Werten des Testdatensatzes, der y - Werte von der gewählten idealen Funktion und die Differenz der beiden y -Werten
    
    def show(self):
        
        '''
        Zeigt den gefilterten Dataframe an
        '''
        
        print(TestDataFinder(self.y_idealfunktion).find())
 
TestDataFinder('y36').show()
 
    
 
    
from matplotlib import pyplot as plt
from matplotlib import style    
    
class IdealGraphProvider:
    
    
    
    def __init__(self, nrows = 4, ncolumns = 2, figsize = (10,10), 
                 title = 'Gefundene ideale Funktionen', font = 20):
        self.nrows = nrows
        self.ncolumns = ncolumns
        self.figsize = figsize
        self.title = title
        self.font = font
                
        
    def show_idealfunctions(self):
        
        
        style.use('ggplot')
        fig, axs = plt.subplots(nrows=self.nrows, ncols=self.ncolumns, 
                                constrained_layout=True, figsize=self.figsize)
        fig.suptitle(self.title, fontsize = self.font)
        
        df_train = Datentabelle('train').downlaod() 
        df_ideal = Datentabelle('ideal').downlaod()
     
    
        axs[0][0].set(title='verauschte Funktion y1', xlabel='x - Achse', ylabel='y - Achse')
        axs[0][1].set(title='ideale Funktion zu y1', xlabel='x - Achse', ylabel='y - Achse')
        axs[1][0].set(title='verauschte Funktion y2', xlabel='x - Achse', ylabel='y - Achse')
        axs[1][1].set(title='ideale Funktion zu y2', xlabel='x - Achse', ylabel='y - Achse')
        axs[2][0].set(title='verauschte Funktion y3', xlabel='x - Achse', ylabel='y - Achse')
        axs[2][1].set(title='ideale Funktion zu y3', xlabel='x - Achse', ylabel='y - Achse')
        axs[3][0].set(title='verauschte Funktion y4', xlabel='x - Achse', ylabel='y - Achse')
        axs[3][1].set(title='ideale Funktion zu y4', xlabel='x - Achse', ylabel='y - Achse')

        axs[0][0].plot(df_train['x'],df_train['y1'])
        axs[0][1].plot(df_ideal['x'],df_ideal['y36'], color = 'black')
        axs[1][0].plot(df_train['x'],df_train['y2'])
        axs[1][1].plot(df_train['x'],df_ideal['y11'], color = 'black')
        axs[2][0].plot(df_train['x'],df_train['y3'])
        axs[2][1].plot(df_train['x'],df_ideal['y2'], color = 'black')
        axs[3][0].plot(df_train['x'],df_train['y4'])
        axs[3][1].plot(df_train['x'],df_ideal['y33'], color = 'black')
        
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
        
IdealGraphProvider().show_idealfunctions()
        
class TrainDataGraphProvider(IdealGraphProvider):
    def __init__(self, nrows = 1, ncolumns = 1, figsize = (10,10), 
                 title = 'Gefundene ideale Funktionen', font = 20):
        super().__init__(nrows , ncolumns, figsize, 
                     title , font)
        
    def show_traindatas(self):
        style.use('ggplot')
        fig, axs = plt.subplots(nrows=self.nrows, ncols=self.ncolumns, 
                                    constrained_layout=True, figsize=self.figsize)
        fig.suptitle(self.title, fontsize = self.font)
            
        df_test = Datentabelle('test').downlaod() 
            
            
        axs.set(xlabel='x - Achse', ylabel='y - Achse')
        axs.scatter(df_test['x'],df_test['y'],color= 'black', linewidth=0.1 ) # Hier wurde plot gegen scatter getauscht, https://www.geeksforgeeks.org/matplotlib-axes-axes-scatter-in-python/
        axs.grid(visible=True, which='major', axis='both', color='white', linestyle='-', linewidth=1)
        axs.set_facecolor('LightGray')
        axs.legend(['Testdaten'], fontsize = 15, facecolor='white') #facecolor https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html
        plt.show()
            
TrainDataGraphProvider().show_traindatas()


class TestDataGraphProvider(IdealGraphProvider):
    def __init__(self, nrows = 1, ncolumns = 1, figsize = (10,10), 
             title ='Ideale Funktion y36 s. Testdaten', font = 20):
        super().__init__(nrows , ncolumns, figsize, 
                 title , font)
        
    def show_fitted_testdata(self, y_ideal):
        style.use('ggplot')
        fig, axs = plt.subplots(nrows=self.nrows, ncols=self.ncolumns, 
                                    constrained_layout=True, figsize=self.figsize)
        fig.suptitle(self.title, fontsize = self.font)
            
            
            
        filtered_df = TestDataFinder(y_ideal).find()
        df_ideal = Datentabelle('ideal') .downlaod() 
            
            
        axs.set(xlabel='x - Achse', ylabel='y - Achse')        
        axs.scatter(filtered_df['x'],filtered_df['y'])
    
        axs.plot(df_ideal['x'],df_ideal[y_ideal], color = 'black')
                    
        axs.legend([(f'ideale Funktion {y_ideal}'),('Testdaten (+/- 0,71)')],
                       fontsize = 15, facecolor='white')
        print(filtered_df)
        plt.show()

TestDataGraphProvider().show_fitted_testdata('y36')
TestDataGraphProvider().show_fitted_testdata('y2')
TestDataGraphProvider().show_fitted_testdata('y11')
TestDataGraphProvider().show_fitted_testdata('y33')           
    
    
        
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    