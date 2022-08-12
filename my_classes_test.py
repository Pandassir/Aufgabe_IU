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

    
    
from my_classes import TrainDataProvider    
class Test_TrainDataProvider(unittest.TestCase):
    
    def setUp(self):                                                            # SetUp method to create same objekt for all methods.
        self.train1 = TrainDataProvider('y1')  
        self.train2 = TrainDataProvider('y2') 
        self.train3 = TrainDataProvider('y3')
        self.train4 = TrainDataProvider('y4')
    
    def test_create_dataframe_if_dataframe(self):      
        self.assertTrue(isinstance(self.train1.create_dataframe(), pd.DataFrame))
        self.assertTrue(isinstance(self.train2.create_dataframe(), pd.DataFrame))
        self.assertTrue(isinstance(self.train3.create_dataframe(), pd.DataFrame))
        self.assertTrue(isinstance(self.train4.create_dataframe(), pd.DataFrame))
        
    def test_create_dataframe_if_right_table(self):  
        self.assertEqual(list((self.train1.create_dataframe()).columns), 
                (['x','y1',]),'Dataframe train should have x,y1 as columns!')
        self.assertEqual(list((self.train2.create_dataframe()).columns), 
                (['x','y2',]),'Dataframe train should have x,y2 as columns!')
        self.assertEqual(list((self.train3.create_dataframe()).columns), 
                (['x','y3',]),'Dataframe train should have x,y3 as columns!')
        self.assertEqual(list((self.train4.create_dataframe()).columns), 
                (['x','y4',]),'Dataframe train should have x,y4 as columns!')
        
        
        
from my_classes import IdealFunctionProvider
class Test_IdealFunctionProvider(unittest.TestCase):
    
    def setUp(self):                                                            # SetUp method to create same objekt for all methods.
        self.ideal1 = IdealFunctionProvider('y1')  
        self.ideal2 = IdealFunctionProvider('y2') 
        self.ideal3 = IdealFunctionProvider('y3')
        self.ideal4 = IdealFunctionProvider('y4')
    
    def test_find_if_dataframe(self):
       
        self.assertTrue(isinstance(self.ideal1.find(), pd.DataFrame))      
        self.assertTrue(isinstance(self.ideal2.find(), pd.DataFrame))
        self.assertTrue(isinstance(self.ideal3.find(), pd.DataFrame))
        self.assertTrue(isinstance(self.ideal4.find(), pd.DataFrame))
    
    def test_find_if_right_table(self): 
       
        self.assertEqual(list((self.ideal1.find()).columns), 
                    (['x','y36']),'Dataframe train should have x,y36 as columns!')
        self.assertEqual(list((self.ideal2.find()).columns), 
                    (['x','y11']),'Dataframe train should have x,y11 as columns!')    
        self.assertEqual(list((self.ideal3.find()).columns), 
                    (['x','y2']),'Dataframe train should have x,y32 as columns!')
        self.assertEqual(list((self.ideal4.find()).columns), 
                    (['x','y33']),'Dataframe train should have x,y333 as columns!')
         
    def test_return_columnname_if_right(self):
        self.assertEqual(self.ideal1.return_columname(), 'y36', 'Should be y36!')
        self.assertEqual(self.ideal2.return_columname(), 'y11', 'Should be y11!')
        self.assertEqual(self.ideal3.return_columname(), 'y2', 'Should be y2!')
        self.assertEqual(self.ideal4.return_columname(), 'y33', 'Should be y33!')


from my_classes import MaxDeltaFinder
class Test_MaxDeltaFinder(unittest.TestCase):   
    
    def test_find_if_right(self):
        mdelta1 = MaxDeltaFinder('y1')
        mdelta2 = MaxDeltaFinder('y2')
        mdelta3 = MaxDeltaFinder('y3')
        mdelta4 = MaxDeltaFinder('y4')
        self.assertEqual(mdelta1.find(),0.7068154531926907, 'Should be 0.7068154531926907!' )
        self.assertEqual(mdelta2.find(),0.7025643272242058, 'Should be 0.7025643272242058!' )
        self.assertEqual(mdelta3.find(),0.7069316449789833, 'Should be 0.7069316449789833!' )
        self.assertEqual(mdelta4.find(),0.6999070199405059, 'Should be 0.6999070199405059!' )
    
    
    
from my_classes import TestDataProvider
class Test_TestDataProvider(unittest.TestCase):
    def setUp(self):                                                            # SetUp method to create same objekt for all methods.
        self.test1 = TestDataProvider('y36')
        self.test2 = TestDataProvider('y11')
        self.test3 = TestDataProvider('y2')
        self.test4 = TestDataProvider('y33')
    
    def test_find_if_dataframe(self):
        self.assertTrue(isinstance(self.test1.find(), pd.DataFrame))
        self.assertTrue(isinstance(self.test2.find(), pd.DataFrame))
        self.assertTrue(isinstance(self.test3.find(), pd.DataFrame))
        self.assertTrue(isinstance(self.test4.find(), pd.DataFrame))
    
    def test_find_if_right_table(self):
        self.assertEqual(list((self.test1.find()).columns), 
                    (['x','y','Diff y36', 'y36']),('Dataframe train should' 
                    'have x,,y,Diff y36, y36 as columns!'))
        self.assertEqual(list((self.test2.find()).columns), 
                    (['x','y','Diff y11', 'y11']),('Dataframe train should' 
                    'have x,,y,Diff y11, y11 as columns!'))
        self.assertEqual(list((self.test3.find()).columns), 
                    (['x','y','Diff y2', 'y2']),('Dataframe train should' 
                    'have x,,y,Diff y2, y2 as columns!'))
        self.assertEqual(list((self.test4.find()).columns), 
                    (['x','y','Diff y33', 'y33']),('Dataframe train should' 
                    'have x,,y,Diff y33, y33 as columns!'))


if __name__ == '__main__':
    unittest.main()