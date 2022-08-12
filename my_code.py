'''
Description of main code:
1__Dataframes__:    
1.1 Show training data y1,y2,y3,y4
1.2 Show column name of the found ideal function 
1.3 Show ideal function data for y1,y2,y3,y4
1.4 Show found max. differences
1.5 Show found test data for each found ideal function
2__Visualisation__:
2.1 Train data vs. ideal functions
2.2 Show Test data 
2.3 Fitted test data vs. found ideal functions 
3__Upload results__:
3.1 Upload fitted test data table to sqlite
4.__Visualisation of Sqlite tables__: 
4.1 Show tables from sqlite
'''



''' 1. Display dataframes and necessary information:'''
    
# 1.1 Display each train dataset:
from my_classes import TrainDataProvider
TrainDataProvider('y1').show_dataframe()
TrainDataProvider('y2').show_dataframe()
TrainDataProvider('y3').show_dataframe()
TrainDataProvider('y4').show_dataframe()

# 1.2 Display each found ideal function for each train dataset:
from my_classes import IdealFunctionProvider
IdealFunctionProvider('y1').show_columnname()
IdealFunctionProvider('y2').show_columnname()
IdealFunctionProvider('y3').show_columnname()
IdealFunctionProvider('y4').show_columnname()

# 1.3 Display each ideal function dataset:
IdealFunctionProvider('y1').show_dataframe()
IdealFunctionProvider('y2').show_dataframe()
IdealFunctionProvider('y3').show_dataframe()
IdealFunctionProvider('y4').show_dataframe()

# 1.4 Display max. dirfference between train data and found ideal function:
from my_classes import MaxDeltaFinder
MaxDeltaFinder('y1').show_maxdelta()
MaxDeltaFinder('y2').show_maxdelta()
MaxDeltaFinder('y3').show_maxdelta()
MaxDeltaFinder('y4').show_maxdelta()
MaxDeltaFinder().average_maxdelta()

#axDeltaFinder().average_maxdelte()

# 1.5 Display found test data for each ideal function:
from my_classes import TestDataProvider
TestDataProvider(IdealFunctionProvider('y1').
                 return_columname()).show_dataframe()
TestDataProvider(IdealFunctionProvider('y2').
                 return_columname()).show_dataframe()
TestDataProvider(IdealFunctionProvider('y3').
                 return_columname()).show_dataframe()
TestDataProvider(IdealFunctionProvider('y4').
                 return_columname()).show_dataframe()


''' 2. Visualisation:'''

# 2.1 Train data vs. ideal function:
from my_classes import IdealGraphProvider
IdealGraphProvider().show_idealfunctions()

# 2.2 Test data:
from my_classes import TestDataGraphProvider
TestDataGraphProvider().show_testdata()

# 2.3 Fitted test data vs. ideal function:
TestDataGraphProvider(IdealFunctionProvider('y1').
                      return_columname()).show_fitted_testdata()
TestDataGraphProvider(IdealFunctionProvider('y2').
                      return_columname()).show_fitted_testdata()
TestDataGraphProvider(IdealFunctionProvider('y3').
                      return_columname()).show_fitted_testdata()
TestDataGraphProvider(IdealFunctionProvider('y4').
                      return_columname()).show_fitted_testdata()  
                   

'''3. Upload results:'''

test1 = TestDataProvider(IdealFunctionProvider('y1').
                         return_columname()).find()
test2 = TestDataProvider(IdealFunctionProvider('y2').
                         return_columname()).find()
test3 = TestDataProvider(IdealFunctionProvider('y3').
                         return_columname()).find()
test4 = TestDataProvider(IdealFunctionProvider('y4').
                         return_columname()).find()

from my_classes import DataTableProvider
DataTableProvider(test1).upload_as(f"fit{IdealFunctionProvider('y1').return_columname()}")
DataTableProvider(test2).upload_as(f"fit{IdealFunctionProvider('y2').return_columname()}")
DataTableProvider(test3).upload_as(f"fit{IdealFunctionProvider('y3').return_columname()}")
DataTableProvider(test4).upload_as(f"fit{IdealFunctionProvider('y4').return_columname()}")


''' 4. Display tables from sqlite:'''

from my_classes import HTMLProvider
HTMLProvider('train').show()
HTMLProvider('ideal').show()
HTMLProvider('test').show()
HTMLProvider(f"fit{IdealFunctionProvider('y1').return_columname()}").show()
HTMLProvider(f"fit{IdealFunctionProvider('y2').return_columname()}").show()
HTMLProvider(f"fit{IdealFunctionProvider('y3').return_columname()}").show()
HTMLProvider(f"fit{IdealFunctionProvider('y4').return_columname()}").show()










