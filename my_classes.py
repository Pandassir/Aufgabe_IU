# 1.Data manager envirement:

import sqlalchemy as db
import pandas as pd
import sys
import colorama
from colorama import Fore
from colorama import Style
colorama.init()
    
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
    Creates a class DataTableProvider. This class should help with this 
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
        Initializes new object DataTableProvider.
        '''
            
        self.tablename = tablename # Name der 
                      
    def downlaod(self):
        
        '''        
        Returns
        -------
        Loads the table into Python from Sqlite and converts the table with 
        help from pandas into a dataframe.
        '''    
        
        
        class DownloadError(Exception):                                         # User-defined Exceptions in case of wrong chosen table.
            def __init__(self):
                my_message = ("Please downlaod in my_classes 'train-','ideal-'"
                "or 'test' table from database. Change and try again!!!")
                self.my_message = my_message
        try:
            mylist = ['train','ideal','test']
            if self.tablename in mylist:
               return pd.read_sql(f'select * from {self.tablename}',dbEngine)
            else:
               raise DownloadError
        except DownloadError:
            
            print(Fore.RED + Style.BRIGHT + "DownloadError:" + Style.RESET_ALL)
            print(DownloadError().my_message)
            sys.exit()  
            
    def upload_as(self, name):
        
        '''        
        Parameters
        ----------
        name : (string)
            Name of table in Sqlite
        Returns
        -------
        Uploads a dataframe to Sqlite as table
        '''
        
        try:                                                                    # Exception in case of the table already exists in data base.
            self.tablename.to_sql(name, dbEngine, if_exists='fail')
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "ValueError:" + Style.RESET_ALL)
            print('Problems in main code part 3 in .upload as:')
            print(f'The table {name} already exist!!!')
        else:
            print(f'Successful upload of {name} table to database.')
        finally:
            print('The program continues.')
  
          
df_train = DataTableProvider('train') .downlaod() 
df_ideal = DataTableProvider('ideal') .downlaod() 
df_test  = DataTableProvider('test') .downlaod() 
df_test.sort_values(by=['x'], inplace=True)                                     # Sort dataframes.
                             

            
            
class TrainDataProvider(DataTableProvider):
    
    '''
    Creates a class that allows the creation of a dataframe of x and the 
    corresponding y value. The remaining values are filtered. In 
    addition, an inheritance of the class 'DataTableProvider' has been built 
    in here.
    '''
        
    def __init__(self, y_train, tablename = 'train'):
        
        '''
        Parameters
        ----------
        y_train : (string)
            Name of train data y-column
        tablename : (string)
            Name of data table
        Returns
        -------
        Initializes new object TrainDataProvider.
        '''
        
        super().__init__(tablename)
        self.y_train = y_train
        
    
    def create_dataframe(self):
        
        '''            
        Returns
        -------
        Dtaframe with x and a chosen y-column.
        '''
        
        df_train = DataTableProvider(self.tablename).downlaod() 
        return df_train.filter(['x', self.y_train])                             # filter dataframes.
        
    def show_dataframe(self):
        
        '''        
        Returns
        -------
        Shows the createt dataframe.
        '''
        
        class Y_Error(Exception):                                               # User-defined Exceptions in case of wrong chosen y.
            def __init__(self):
                my_message = ("Y-column doesn't exists in train table! Please"
                              " choose in main code part 1.1 between"
                              " y1-y4. Change and try again!!!")
                self.my_message = my_message
        try:
            mylist = ['y1','y2','y3','y4']
            if self.y_train in mylist:
                print(f'Dataframe from train datas for x and {self.y_train}:')
                print(df_train.filter(['x', self.y_train]))
                print('\n')
            else:
                raise Y_Error
    
        except Y_Error:
            
            print(Fore.RED + Style.BRIGHT + "Y_Error:" + Style.RESET_ALL)
            print(Y_Error().my_message)
            sys.exit()
            
    
  
      
class IdealFunctionProvider(TrainDataProvider):
    
    ''' 
    Creates a class to find the ideal function for the training data. In 
    addition, an inheritance of the class 'TrainDataProvider' has been 
    established here built-in. 
    '''
    
    def __init__(self, y_train, tablename = 'train'):
        
        '''
        Parameters
        ----------
        y_train : (string)
            Name of train data y-column
        tablename : (string)
            Name of data table
        Returns
        -------
        Initializes new object TrainDataProvider.
        '''
        
        self.y_train = y_train
        
    def find(self):
        
        '''
        Returns
        -------
        finds the best matching ideal function for the individual training data.
        It then filters the dataframe so that only the x and y values of the 
        ideal function remain.
        '''

        df_ideal = DataTableProvider('ideal') .downlaod() 
        df_ideal.drop(['x'], axis = 1, inplace = True)
        mylist=[] 
        for name in df_ideal:                                                   # for loop itrates through all columns in ideal data.
            mylist.append(sum((df_train[self.y_train]-df_ideal[str(name)])**2)) # append sum of differences between chosen y-column from train data and a y-column from ideal data.
        index_min = (mylist.index(min(mylist)))                                 # finds index with lowest sum in list.
        df_ideal = DataTableProvider('ideal').downlaod()                        
        return df_ideal.filter(['x',f'y{index_min+1}'])                         # index is used to create the dataframe with a filter.
        
    def show_dataframe(self):
       
        '''
        Returns
        -------
        Shows the dataframe of found ideal function.
        '''

        print(f'\nIdeal function dataframe for train dataset {self.y_train}:')
        print(IdealFunctionProvider(self.y_train).find())
        print('\n')
        
    def return_columname(self):
               
        '''
        Returns
        -------
        Columname of found ideal function.
        '''
        
        return IdealFunctionProvider(self.y_train).find().columns[1]    
        
    def show_columnname(self):
       
        '''
        Returns
        -------
        Shows the columname of found ideal function.
        '''
            
        print(f'The {self.y_train} dataset of the training data includes the ideal function:'                  
              ,((IdealFunctionProvider(self.y_train).find()).columns[1]))
            
        
    
           
  
             
class MaxDeltaFinder(TrainDataProvider):
        
    '''
    Creates a class that determines the maximum deviations from the training 
    data and the associated ideal data. In addition, an inheritance of the 
    class 'TrainDataProvider' has been established here built-in. 
    '''        
    def __init__(self, y_train = 'y1'):
            
        '''
        Parameters
        ----------
        y_train : (string)
            Name of train data y-column
            
        Returns
        -------
        Initializes new object MaxDeltaFinder.
        '''
            
        super().__init__(y_train)
        
    def find(self):
            
        '''
        Returns
        -------
        Finds the maximum deviation between each training data (y1-y4) and the 
        corresponding ideal data. These deviations were multiplied by the 
        factor sqrt(2). This deviation is used as a limit for the selection of 
        the test data. If the data point is below the deviation, it belongs to 
        the ideal function, if not, then it is an outlier.
        '''
            
        import math
        df_train_xy = TrainDataProvider(self.y_train).create_dataframe()        # Dataframe with x and y from train data.
        df_ideal = IdealFunctionProvider(self.y_train).find()                   # Dataframe with x and y from ideal data.
        maxdelta = abs((df_train_xy.iloc[:,1]-df_ideal.iloc[:,1]).max())        # Finds max. difference between y-values
        faktordelta = maxdelta*(math.sqrt(2))
        return faktordelta
        
    def show_maxdelta(self):
            
        '''
        Returns
        -------
        Shows the maximum delta between train data and corresponding ideal data.
        '''
          
        print(f'\nDie maximale Abweichung zwischen {self.y_train} und',
                (IdealFunctionProvider(self.y_train).find()).columns[1],'ist:',
                 MaxDeltaFinder(self.y_train).find())
    
    def average_maxdelta(self):
                    
        '''
        Returns
        -------
        Shows the averaged max. delta..
        '''
        
        print('\nAn average value of 0.71 is used for the next mathematical values')
    
  
        
class TestDataProvider:
    
    '''
    Creates a class that finds the appropriate test data for the ideal 
    functions.
    '''
         
    def __init__(self, y_idealfunktion):
        
            
        '''
        Parameters
        ----------
        y_idealfunktion : (string)
            Name of ideal function y-column
            
        Returns
        -------
        Initializes new object TestDataProvider.
        '''
            
        self.y_idealfunktion = y_idealfunktion
             
    def find(self):
            
        '''
        Returns
        -------
        Finds a dataframe with the x+y values of the test data, the y values 
        from the selected ideal function, and the difference between the two y 
        values. All values above the maximum deviation are sorted out.
        '''
             
        df_ideal = DataTableProvider('ideal') .downlaod() 
        df_test  = DataTableProvider('test') .downlaod() 
        df_test.sort_values(by=['x'], inplace=True)                                
        df_merged_test = df_test.merge(df_ideal, on = 'x')                      # Merge the test data and ideal data, but only the common x values.
        df_merged_test = df_merged_test.filter(['x','y', self.y_idealfunktion]) # filers out all unnecessary y-columns from ideal data.
        df_merged_test.insert(loc=2, column = f'Diff {self.y_idealfunktion}',   # Insert a column named Diff y(1-4).
        value =abs(df_merged_test['y']-df_merged_test[self.y_idealfunktion]))   
        df_mask=df_merged_test[f'Diff {self.y_idealfunktion}']<= 0.71           # Creation of a mask containing only values of less than maximum deviation of a selected column.
        filtered_df = df_merged_test[df_mask]     
        return filtered_df                                                      # Activation of the mask. What remains are the index rows of the previously created column with the values less than maximum.
                                                                                    
    def show_dataframe(self):
            
        '''
        Returns
        -------
        Shows the filtered dataframe.
        '''
        
        print('\nFound test data with max. difference for',
                  TestDataProvider(self.y_idealfunktion).find().columns[3],':')
        print(TestDataProvider(self.y_idealfunktion).find())
        print('\n')
            
        
        
# 2.Visualisation envirement:
        
from matplotlib import pyplot as plt
from matplotlib import style    
        
class IdealGraphProvider:
    
    '''
    Creates a class wich displays a plot with train data and the appropriate
    ideal functions.
    '''
    
    def __init__(self, nrows = 4, ncolumns = 2, figsize = (10,10), 
                     title = 'Found ideal functions', font = 20):                
            
        '''
        Parameters
        ----------
        nrows : (integer)
            Quantity of rows in the figure
        ncolumns : (integer)
            Quantity of colums in the figure
        figsize : (integer)
            Size of figure
        title : (string)
            Title of figure
        font : (integer)
            Size of title in the figure
            
        Returns
        -------
        Initializes new object IdealGraphProvider.
        '''
        
        self.nrows = nrows
        self.ncolumns = ncolumns
        self.figsize = figsize
        self.title = title
        self.font = font
                    
            
    def show_idealfunctions(self):
                    
        '''
        Returns
        -------
        Shows a plot with train data corresponding ideal data.
        '''
            
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
        axs[0][1].plot(df_ideal['x'],df_ideal[IdealFunctionProvider('y1').
                                    return_columname()], color = 'black')
        axs[1][0].plot(df_train['x'],df_train['y2'])
        axs[1][1].plot(df_train['x'],df_ideal[IdealFunctionProvider('y2').
                                    return_columname()], color = 'black')
        axs[2][0].plot(df_train['x'],df_train['y3'])
        axs[2][1].plot(df_train['x'],df_ideal[IdealFunctionProvider('y3').
                                    return_columname()], color = 'black')
        axs[3][0].plot(df_train['x'],df_train['y4'])
        axs[3][1].plot(df_train['x'],df_ideal[IdealFunctionProvider('y4').
                                    return_columname()], color = 'black')
            
        axs[0][0].grid(visible=True, which='major', axis='both', 
                       color='LightGrey', linestyle='--', linewidth=1)          
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
            
        axs[0][0].legend(['train data y1'])                                     
        axs[0][1].legend(['ideal function to y1'])
        axs[1][0].legend(['train data y2'])
        axs[1][1].legend(['ideal function to y2'])
        axs[2][0].legend(['train data y3'])
        axs[2][1].legend(['ideal function to y3'])
        axs[3][0].legend(['train data y4'])
        axs[3][1].legend(['ideal function to y4'])
        plt.show()
                

     
class TestDataGraphProvider(IdealGraphProvider):
    
    '''
    Creates a class wich displays test data. In ddition, an inheritance of the 
    class 'IdealGraphProvider' has been established here built-in. 
    '''
    
    def __init__(self, y_ideal = 'y1', nrows = 1, ncolumns = 1, figsize = (10,10), 
                 title ='Test data', font = 20):
                    
        '''
        Parameters
        ----------
        y_ideal : (string)
            Name of train data y-column
        nrows : (integer)
            Quantity of rows in the figure
        ncolumns : (integer)
            Quantity of colums in the figure
        figsize : (integer)
            Size of figure
        title : (string)
            Title of figure
        font : (integer)
            Size of title in the figure
            
        Returns
        -------
        Initializes new object TestDataGraphProvider.
        '''
        
        super().__init__(nrows , ncolumns, figsize, title , font)
        self.y_ideal = y_ideal
        
    def show_testdata(self):
                    
        '''
        Returns
        -------
        Shows a scatter with test data.
        '''
        
        style.use('ggplot')
        fig, axs = plt.subplots(nrows=self.nrows, ncols=self.ncolumns, 
                   constrained_layout=True, figsize=self.figsize)
        fig.suptitle(self.title, fontsize = self.font)
        df_test = DataTableProvider('test').downlaod() 
        axs.set(xlabel='x - axis', ylabel='y - axis')
        axs.scatter(df_test['x'],df_test['y'],color= 'black', linewidth=0.1 )       
        axs.grid(visible=True, which='major', axis='both', color='white', 
                 linestyle='-', linewidth=1)
        axs.set_facecolor('LightGray')
        axs.legend(['Test data'], fontsize = 15, facecolor='white')                
        plt.show()
            
    def show_fitted_testdata(self):
                    
        '''
        Returns
        -------
        Shows the ideal function with found test data.
        '''
        
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
    
    '''
    Creates a class wich displays the tables in the database. In ddition, an 
    inheritance of the class 'DataTableProvider' has been established here 
    built-in. 
    '''
    
    def __intit__(self, tablename):
        super().__init__(tablename)
                            
        '''
        Parameters
        ----------
        tablename : (string)
            Name of data table 
            
        Returns
        -------
        Initializes new object HTMLProvider.
        '''
    
    def show(self):
                    
        '''
        Returns
        -------
        Shows the tables from database through html file.
        '''
        
        try:                                                                    # Exception in case of wrong name.
            df = pd.read_sql(f'select * from {self.tablename}',dbEngine)
            html = df.to_html()
            text_file = open(f'{self.tablename}.html', 'w')
            text_file.write(html)
            text_file.close()
            import webbrowser
            webbrowser.open(f'{self.tablename}.html')
        except :
            print(Fore.RED + Style.BRIGHT + "\nOperationalError:" + Style.RESET_ALL)
            print(("Problem in part 4 in my_code: \nTable doesn't exist!" 
                   "Please show in database for table names! "))
            
       
            
            


  
  
        
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    