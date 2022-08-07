# 1.Data manager envirement:

import sqlalchemy as db
import pandas as pd
    
# 1.1 turn on database engine:   
dbEngine=db.create_engine('sqlite:///database.db')                              # Ensure this is the correct path for the sqlite file.
    
''' 
A connection to the database 'Sqlite' is established here. In order for the 
data transfer from data bank to Python and vice versa to work without problems,
Sqlalchemy is used. This is a kind of intermediate layer and helps to organize
the data transfer correctly.
'''
    
    
    
# 1.2 create a class for downloading and uploading datas:
class DataTableProvider: 
    
    '''
    This creates a class DataTableProvider. This class should help with this 
    clearly download the tables from Sqlite and upload them vice versa.
    '''
        
    def __init__(self, tablename):
        
        '''     
        Parameters
        ----------
        tablename : (string)
            Name of the selected table.
        Returns
        -------
        Initializes a new data table object.
        '''
            
        self.tablename = tablename # Name der 
                      
    def downlaod(self):
        
        '''        
        Returns
        -------
        Loads the table into Python from Sqlite and converts the table with 
        Help from pandas into a dataframe.
        '''
    
        return pd.read_sql(f'select * from {self.tablename}',dbEngine)
            
    def upload_as(self, name):
        
        '''        
        Parameters
        ----------
        dataframe : Dataframe
            The desired dataframe must be specified as a parameter
        Returns
        -------
        Uploads a dataframe to Sqlite
        '''
        
        self.tablename.to_sql(name, dbEngine, if_exists='fail')
  

          
df_train = DataTableProvider('train') .downlaod() 
df_ideal = DataTableProvider('ideal') .downlaod() 
df_test  = DataTableProvider('test') .downlaod() 
df_test.sort_values(by=['x'], inplace=True)                                     # sorts the dataframe

            
            
class TrainDataProvider(DataTableProvider):
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
        super().__init__(tablename)
        self.y_train = y_train
            
    def create_dataframe(self):
        '''
            
        Returns
        -------
        Dataframe
            Hier entsteht ein Dataframe mit x und einem gewählten y-Wert
        '''
        df_train = DataTableProvider(self.tablename).downlaod() 
        #df_train = pd.read_sql(f'SELECT * FROM {self.tablename}', con=engine)
        return df_train.filter(['x', self.y_train])
        
    def show_dataframe(self):
            
        print(f'Dataframe from train datas for x and {self.y_train}:')
        print(df_train.filter(['x', self.y_train]))
        print('\n')
        return df_train.filter(['x', self.y_train])
    
  
      
class IdealFunktionProvider(TrainDataProvider):
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
        df_ideal = DataTableProvider('ideal') .downlaod() 
        df_ideal.drop(['x'], axis = 1, inplace = True)
        mylist=[] 
        for name in df_ideal:
            mylist.append(sum((df_train[self.y_train]-df_ideal[str(name)])**2))
        index_min = (mylist.index(min(mylist)))        
        df_ideal = DataTableProvider('ideal').downlaod() # originaler df_ideal geladen, weil oben x herausgenommen wurde.
        return df_ideal.filter(['x',f'y{index_min+1}'])
        
    def show_dataframe(self):
        ''' 
        Zeigt den Dataframe der gefundenen idealen Funktion an
        '''
        print(f'\nIdeal function dataframe for train dataset {self.y_train}:')
        print(IdealFunktionProvider(self.y_train).find())
        print('\n')
        return (IdealFunktionProvider(self.y_train).find())
        
    def show_columnname(self):
        '''
        Zeigt den Spaltennamen der oben gefundenen ideealen Funktion an
        '''
            
        print(f'The {self.y_train} dataset of the training data includes the ideal function:'                  
              ,((IdealFunktionProvider(self.y_train).find()).columns[1]))
            
        
    def return_columname(self):
        return IdealFunktionProvider(self.y_train).find().columns[1]
            
           
             
class MaxDeltaFinder(TrainDataProvider):
        
    '''
    Hier ensteht eine Klasse, welche aus dem Trainigsdatendatz und dem 
    Idealdatensatz die maximalen Abweichungen zwischen den  einzelnen 
    Trainingsdatensätze y1-y4 und deren gefundenen idealen Funktionen ermittelt.
    '''
        
    def __init__(self, y_train = 1):
            
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
        df_train_xy = TrainDataProvider(self.y_train).create_dataframe()                        # Laden des Trainingdatensatzes
        #df_train_xy.drop(['x'], axis = 1, inplace = True)                      # Löschen der x -Spalte
        df_ideal = IdealFunktionProvider(self.y_train).find()                         # Laden des Trainingdatensatzes
        #df_ideal.drop(['x'], axis = 1, inplace = True)                         # Löschen der x -Spalte
        maxdelta = abs((df_train_xy.iloc[:,1]-df_ideal.iloc[:,1]).max())
        faktordelta = maxdelta*(math.sqrt(2))
        return faktordelta
        
    def show_maxdelta(self):
            
        '''
        Zeigt den Zahlenwert der maximalen Abweichung an
        '''
            
        print(f'\nDie maximale Abweichung zwischen {self.y_train} und',
                (IdealFunktionProvider(self.y_train).find()).columns[1],'ist:',
                 MaxDeltaFinder(self.y_train).find())
    
    def average_maxdelte(self):
        print('\nAn average value of 0.71 is used for the next mathematical values')
    
  
        
class TestDataProvider:
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
            
        #md1 = MaxDeltaFinder('y1').find()                                       # Findet die maximale Abweichung zwischen y1-Traingsdatensatz und dem dazugehörigen Idealdatensatz
        #md2 = MaxDeltaFinder('y2').find()                                       # Findet die maximale Abweichung zwischen y2-Traingsdatensatz und dem dazugehörigen Idealdatensatz
        #md3 = MaxDeltaFinder('y3').find()                                       # Findet die maximale Abweichung zwischen y3-Traingsdatensatz und dem dazugehörigen Idealdatensatz
        #md4 = MaxDeltaFinder('y4').find()                                       # Findet die maximale Abweichung zwischen y4-Traingsdatensatz und dem dazugehörigen Idealdatensatz
             
        #md_avrg = (md1+md2+md3+md4)/4  
            
        #print(md_avrg)
             
        df_ideal = DataTableProvider('ideal') .downlaod() 
        df_test  = DataTableProvider('test') .downlaod() 
        df_test.sort_values(by=['x'], inplace=True)                              # Laden der Idealdaten
        df_merged_test = df_test.merge(df_ideal, on = 'x')                      # Zusammenfügen vom Testdatensatz und Idealdatensatz, aber nur die gemeinsamen x - Werte
        df_merged_test = df_merged_test.filter(['x','y', self.y_idealfunktion])                  # Erstellung eines Dateframes mit den x und y- Werten des Trainingsdatensatzes und den y- Werten des Idealdatendatzes
        df_merged_test.insert(loc=2, column = f'Diff {self.y_idealfunktion}',   # Einfügen einer Spalte, welche die Differenz zwischen den y- Werten vom Trainingsdatensatz und dem Idealdatensatz anzeigt
        value =abs(df_merged_test['y']-df_merged_test[self.y_idealfunktion]))   
        #df_mask=df_merged_test[f'Diff {self.y_idealfunktion}']<= 0.71
        df_mask=df_merged_test[f'Diff {self.y_idealfunktion}']<= 0.71        # Erstellung einer Maske wo nur Werte < max. Abweichung einer ausgewählten Spalte erstellt
        filtered_df = df_merged_test[df_mask]     
        return filtered_df                               # Aktivierung der Maske auf den Dataframe. Übrig bleiben die Indexzeilen, der zuvor erstellten Spalte mit den gefilterten Werten
                                                                 # Rückgabe eines Dataframes mit den x+y- Werten des Testdatensatzes, der y - Werte von der gewählten idealen Funktion und die Differenz der beiden y -Werten
        
    def show_dataframe(self):
            
        '''
        Zeigt den gefilterten Dataframe an
        '''
        print('Found test data with max. difference for',
                  TestDataProvider(self.y_idealfunktion).find().columns[3],':')
        print(TestDataProvider(self.y_idealfunktion).find())
        print('\n')
            
    def return_dataframe(self):
        return TestDataProvider(self.y_idealfunktion).find()
     

TestDataProvider('y36').show_dataframe()     
        
     
# Visualisation envirement:
        
from matplotlib import pyplot as plt
from matplotlib import style    
        
class IdealGraphProvider:
        
        
        
    def __init__(self, nrows = 4, ncolumns = 2, figsize = (10,10), 
                     title = 'Found ideal functions', font = 20):
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
        df_train = DataTableProvider('train').downlaod() 
        df_ideal = DataTableProvider('ideal').downlaod()
         
        
        axs[0][0].set(title='train data y1', xlabel='x - axis', 
                      ylabel='y - axis')
        axs[0][1].set(title='ideal function to y1', xlabel='x - axis',
                      ylabel='y - axis')
        axs[1][0].set(title='train data y2', xlabel='x - axis', 
                      ylabel='y - axis')
        axs[1][1].set(title='ideal function to y2', xlabel='x - axis', 
                      ylabel='y - axis')
        axs[2][0].set(title='train data y3', xlabel='x - axis', 
                      ylabel='y - axis')
        axs[2][1].set(title='ideal function to y3', xlabel='x - axis', 
                      ylabel='y - axis')
        axs[3][0].set(title='train data y4', xlabel='x - axis', 
                      ylabel='y - axis')
        axs[3][1].set(title='ideal function to y4', xlabel='x - axis', 
                      ylabel='y - axis')
    
        axs[0][0].plot(df_train['x'],df_train['y1'])
        axs[0][1].plot(df_ideal['x'],df_ideal[IdealFunktionProvider('y1').
                                    return_columname()], color = 'black')
        axs[1][0].plot(df_train['x'],df_train['y2'])
        axs[1][1].plot(df_train['x'],df_ideal[IdealFunktionProvider('y2').
                                    return_columname()], color = 'black')
        axs[2][0].plot(df_train['x'],df_train['y3'])
        axs[2][1].plot(df_train['x'],df_ideal[IdealFunktionProvider('y3').
                                    return_columname()], color = 'black')
        axs[3][0].plot(df_train['x'],df_train['y4'])
        axs[3][1].plot(df_train['x'],df_ideal[IdealFunktionProvider('y4').
                                    return_columname()], color = 'black')
            
        axs[0][0].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1) #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
        axs[0][1].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)
        axs[1][0].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)
        axs[1][1].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)
        axs[2][0].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)
        axs[2][1].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)
        axs[3][0].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)
        axs[3][1].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)
            
        axs[0][0].legend(['train data y1']) #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
        axs[0][1].legend(['ideal function to y1'])
        axs[1][0].legend(['train data y2'])
        axs[1][1].legend(['ideal function to y2'])
        axs[2][0].legend(['train data y3'])
        axs[2][1].legend(['ideal function to y3'])
        axs[3][0].legend(['train data y4'])
        axs[3][1].legend(['ideal function to y4'])
        plt.show()
                
    
     
class TestDataGraphProvider(IdealGraphProvider):
    def __init__(self, y_ideal = 1, nrows = 1, ncolumns = 1, figsize = (10,10), 
                 title ='Test data', font = 20):
        super().__init__(nrows , ncolumns, figsize, title , font)
        self.y_ideal = y_ideal
        
    def show_testdata(self):
        style.use('ggplot')
        fig, axs = plt.subplots(nrows=self.nrows, ncols=self.ncolumns, 
                   constrained_layout=True, figsize=self.figsize)
        fig.suptitle(self.title, fontsize = self.font)
        df_test = DataTableProvider('test').downlaod() 
        axs.set(xlabel='x - axis', ylabel='y - axis')
        axs.scatter(df_test['x'],df_test['y'],color= 'black', linewidth=0.1 ) # Hier wurde plot gegen scatter getauscht, https://www.geeksforgeeks.org/matplotlib-axes-axes-scatter-in-python/
        axs.grid(visible=True, which='major', axis='both', color='white', linestyle='-', linewidth=1)
        axs.set_facecolor('LightGray')
        axs.legend(['test data'], fontsize = 15, facecolor='white') #facecolor https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html
        plt.show()
            
    def show_fitted_testdata(self):
        style.use('ggplot')
        fig, axs = plt.subplots(nrows=self.nrows, ncols=self.ncolumns, 
                   constrained_layout=True, figsize=self.figsize)
        fig.suptitle(f"Fitted test data for ideal function {self.y_ideal}"
                     , fontsize = self.font)
        filtered_df = TestDataProvider(self.y_ideal).find()
        df_ideal = DataTableProvider('ideal') .downlaod() 
        axs.set(xlabel='x - Achse', ylabel='y - Achse')        
        axs.scatter(filtered_df['x'],filtered_df['y'])
        axs.plot(df_ideal['x'],df_ideal[self.y_ideal], color = 'black')
        axs.legend([(f'Ideal function {self.y_ideal}'),('Test data (+/- 0,71)')],
                   fontsize = 15, facecolor='white')
        plt.show()
    


class HTMLProvider(DataTableProvider):
    def __intit__(self, tablename):
        super().__init__(tablename)
    
    def show(self):
        df = pd.read_sql(f'select * from {self.tablename}',dbEngine)
        html = df.to_html()
        text_file = open(f'{self.tablename}.html', 'w')
        text_file.write(html)
        text_file.close()
        import webbrowser
        webbrowser.open(f'{self.tablename}.html')
            


  
  
        
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    