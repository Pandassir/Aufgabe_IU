import pandas as pd
from sqlalchemy import create_engine as ce

''' Hier wird eine Verbindung zu der Datenbank 'MySQL' hergestellt. Damit
der Datentransfer von Datenbamk zu Python und umgekehrt ohne Probleme
funktioniert wird Sqlalchemy verwendet. Dies ist eine Art Zwischenschicht
und hilft den Datentransfer richtig zu organisieren'''

engine = ce( 'mysql+pymysql://root:&5WdgSjT6$D/1W;u@localhost:3306/daten_iu') # https://overiq.com/sqlalchemy-101/installing-sqlalchemy-and-connecting-to-database/
engine.connect()

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

        return pd.read_sql(f'SELECT * FROM {self.tablename}', con=engine)
        
        
    def upload(self, dataframe):
        '''        

        Parameters
        ----------
        dataframe : Dataframe
            Als Parameter muss der gewünschte Dataframe angegeben werden

        Returns
        -------
        Ladet einen Dataframe in MySQL hoch

        '''
        dataframe.to_sql(self.tablename, engine)
        
        
        
        
        
class TrainDataProvider(Datentabelle):
    '''
    Hier entsteht eine Klasse die die Erstellung eines Dataframes von x und dem
    entsprechenden y Wert organisiert. Die restlichen Werte werden gefiltert.
    Zudem wurde hier eine Vererbung der Klasse 'Datentabelle' eingebaut.
    '''
    
    def __init__(self, y, tablename = 'train'):
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
        self.y = y
        
    def create(self):
        '''
        
        Returns
        -------
        Dataframe
            Hier entsteht ein Dataframe mit x und einem gewählten y-Wert

        '''
        #df_train = Datentabelle(self.tablename).downlaod() 
        df_train = pd.read_sql(f'SELECT * FROM {self.tablename}', con=engine)
        return df_train.filter(['x', self.y])

    





    

class IdealFunktionProvider(TrainDataProvider):
    '''
    Hier entstent eine Klasse die die ideale Funktion zu den Trainingsdaten
    findet. Zudem wurde hier eine Vererbung der Klasse 'TrainDataProvider'
    eingebaut.
    '''
    def __init__(self, y, tablename = 'train'):
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
        self.y = y
    
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
        df_train = Datentabelle('train').downlaod() 
        df_ideal = Datentabelle('ideal').downlaod()
        df_ideal.drop(['x'], axis = 1, inplace = True)
        
        mylist=[] 
        
        for name in df_ideal:
            mylist.append(sum((df_train[self.y]-df_ideal[str(name)])**2))
        index_min = (mylist.index(min(mylist)))        
        df_ideal = Datentabelle('ideal').downlaod() # originaler df_ideal geladen, weil oben x herausgenommen wurde.
        return df_ideal.filter(['x',f'y{index_min+1}'])
    
    def show_dataframe(self):
        ''' 
        Zeigt den gefundenen Dataframe an
        '''
        print(IdealFunktionProvider(self.y).find())
    
    def show_columnname(self):
        '''
        Zeigt die oben gefundenen Werte an
        '''
        
        print(f'Zu den {self.y}-Werten vom Trainigsdaten gehört die ideale Fynktion:'
              ,((IdealFunktionProvider(self.y).find()).columns[1]))
        
        

        
class MaxDeltaFinder(TrainDataProvider):
    '''
    Hier ensteht eine Klasse, welche aus dem Testdatensatz die Datenpunkte
    findet, welche zu der entsprechenden idealen Funktion gehört.
    '''
    def __init__(self, y):
        super().__init__(y)
    
    def find(self):
        import math
        df_train_xy = TrainDataProvider(self.y).create()
        df_train_xy.drop(['x'], axis = 1, inplace = True)
        df_ideal = IdealFunktionProvider(self.y).find()
        df_ideal.drop(['x'], axis = 1, inplace = True)
        
        maxdelta = abs((df_train_xy.iloc[:,0]-df_ideal.iloc[:,0]).max())
        faktordelta = maxdelta*(math.sqrt(2))
        return faktordelta
    
    def show_maxdelta(self):
        print(f'Die maximale Abweichung zwischen {self.y} und',
              (IdealFunktionProvider(self.y).find()).columns[1],'ist:',
              MaxDeltaFinder(self.y).find())

    
        
        
        
    
class TrainDataFinder:
     
     def __init__(self, y_idealfunktion):
         self.y_idealfunktion = y_idealfunktion
         
     def find(self):
         
        df_test = Datentabelle('test').downlaod()  
        df_ideal = Datentabelle('ideal').downlaod()
        df_merged_test = df_test.merge(df_ideal, on = 'x')
        df_merged_test.filter(['x','y', self.y_idealfunktion])
        return df_merged_test.insert(loc=3, column = f'Diff {self.y_idealfunktion}', 
                              value =abs(df_merged_test['y']-df_merged_test[self.y_idealfunktion])) #https://www.youtube.com/watch?v=IKiDSOUTQX8
        #df_mask=df_merged_test[f'Diff {self.y_idealfunktion}']<= 0.71
        #filtered_df = df_merged_test[df_mask]
        #return filtered_df
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    