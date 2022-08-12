import unittest
import pandas as pd

  

from my_classes import DataTableProvider 
class Test_DataTableProvider(unittest.TestCase):
    
    def setUp(self):                                                            # SetUp method to create same objekt for all methods.
        self.table1 = DataTableProvider('train')  
        self.table2 = DataTableProvider('ideal') 
        self.table3 = DataTableProvider('test')                               

    def test_download_if_create_dataframe(self):
        self.assertTrue(isinstance(self.table1.downlaod(), pd.DataFrame))
        self.assertTrue(isinstance(self.table2.downlaod(), pd.DataFrame))
        self.assertTrue(isinstance(self.table3.downlaod(), pd.DataFrame))
        
    def test_download_if_right_table(self):
        self.assertEqual(list((self.table1.downlaod()).columns), 
                        (['x','y1','y2','y3','y4']),'Dataframe train should' \
                            ' have x,y1,y2,y3,y4 as columns!')
        self.assertEqual((self.table2.downlaod()).columns[50], 
                        ('y50'),'Dataframe train should' \
                            ' have x,y1-y50 as columns!')
        self.assertEqual(list((self.table3.downlaod()).columns), 
                        (['x','y']),'Dataframe train should' \
                            ' have x,y as columns!')
        
            

    def upload(self):
        pass
    
    
    
from my_classes import TrainDataProvider    
class Test_TrainDataProvider(unittest.TestCase):
    
    def setUp(self):                                                            # SetUp method to create same objekt for all methods.
        self.train1 = TrainDataProvider('y1')  
        self.train2 = TrainDataProvider('y2') 
        self.train3 = TrainDataProvider('y3')
        self.train4 = TrainDataProvider('y4')
    
    def test_create_dataframe_if_dataframe(self):      
        self.assertTrue(isinstance(self.train1.create_dataframe(), 
                                   pd.DataFrame))
        self.assertTrue(isinstance(self.train2.create_dataframe(), 
                                   pd.DataFrame))
        self.assertTrue(isinstance(self.train3.create_dataframe(), 
                                   pd.DataFrame))
        self.assertTrue(isinstance(self.train4.create_dataframe(), 
                                   pd.DataFrame))
        
        

    def test_create_dataframe_if_right_table(self):  
        self.assertEqual(list((self.train1.create_dataframe()).columns), 
                        (['x','y1',]),'Dataframe train should' \
                            ' have x,y1 as columns!')
        self.assertEqual(list((self.train2.create_dataframe()).columns), 
                        (['x','y2',]),'Dataframe train should' \
                            ' have x,y2 as columns!')
        self.assertEqual(list((self.train3.create_dataframe()).columns), 
                        (['x','y3',]),'Dataframe train should' \
                            ' have x,y3 as columns!')
        self.assertEqual(list((self.train4.create_dataframe()).columns), 
                        (['x','y4',]),'Dataframe train should' \
                            ' have x,y4 as columns!')
        
         
        
        
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    #def test_download_to_downloaderror(self):   #Wie testet man user defined exceptions?
        #class DownloadError(Exception):                                         # User-defined Exceptions in case of wrong chosen table.
            #def __init__(self):
                #my_message = ("Please downlaod in my_classes 'train-','ideal-'"
                #"or 'test' table from database. Change and try again!!!")
                #self.my_message = my_message
        #with self.assertRaises(DownloadError):
            #table1 = DataTableProvider('train')
            #table1.downlaod()
            
            
            
from my_classes import MaxDeltaFinder 
class TestMaxDeltaFinder(unittest.TestCase):  
    def test_find(self): #https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises
           try:
               MaxDeltaFinder('y1').find()
           except TypeError:
               self.fail(("Probleme in my_code/MaxDeltaFinder/find():"
                   "Bitte geben Sie eine Zahl ein!") )
        
        
        
        
        #with self.assertRaises(TypeError):
            #MaxDeltaFinder('y1').find()







df_train = DataTableProvider('train') .downlaod() 
df_ideal = DataTableProvider('ideal') .downlaod() 
df_test  = DataTableProvider('test') .downlaod() 
df_test.sort_values(by=['x'], inplace=True)
                              
from my_classes import IdealFunktionProvider 
class TestIdealFunktionProvider(unittest.TestCase):
    def test_find(self):
        inp = IdealFunktionProvider('y1').find()
        self.assertTrue(isinstance(inp, pd.DataFrame))
        
        
        
    def test_return_columnname(self):
        inp = IdealFunktionProvider('y1').return_columname()
        self.assertEqual(inp, 'y36', 'Should return x36.')   
    def test_columnname_y2(self):
        inp = IdealFunktionProvider('y2').return_columname()
        self.assertEqual(inp, 'y11', 'Should return x11.')
    def test_columnname_y3(self):
        inp = IdealFunktionProvider('y3').return_columname()
        self.assertEqual(inp, 'y2', 'Should return x2.')
    def test_columnname_y4(self):
        inp = IdealFunktionProvider('y4').return_columname()
        self.assertEqual(inp, 'y33', 'Should return x33.')
        
        
        


if __name__ == '__main__':
    unittest.main()