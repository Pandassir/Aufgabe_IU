'''
Description of main code:

1__Dataframes__:    
1.1 Show training data y1,y2,y3,y4
1.2 Show column name of the found ideal function 
1.3 Show ideal function data for y1,y2,y3,y4
1.4 Show found test data for each found ideal function

2__Visualisation__:
2.1 Trainingsdaten vs. Idealfunktionen
2.2 Testdaten anzeigen
2.3 Gefittete Testdaten vs. Idealfunktionen

3__Upload results__:
3.1 Gefittete Testdaten vs. Idealfunktionen Dataframes an sqlite uploaden

4.__Visualisation of Sqlite tables__: 
4.1 Tabellen aus der Datenbamk anzeigem
'''




# 1. Display dataframes and necessary information:
    
# 1.1 Display each train dataset:
from my_classes import TrainDataProvider
#TrainDataProvider('y1').show_dataframe()
#TrainDataProvider('y2').show_dataframe()
#TrainDataProvider('y3').show_dataframe()
#TrainDataProvider('y4').show_dataframe()

# 1.2 Display each found ideal function for each train dataset:
from my_classes import IdealFunktionProvider
#IdealFunktionProvider('y1').show_columnname()
#IdealFunktionProvider('y2').show_columnname()
#IdealFunktionProvider('y3').show_columnname()
#IdealFunktionProvider('y4').show_columnname()

# 1.3 Display each ideal function dataset:
#IdealFunktionProvider('y1').show_dataframe()
#IdealFunktionProvider('y2').show_dataframe()
#IdealFunktionProvider('y3').show_dataframe()
#IdealFunktionProvider('y4').show_dataframe()

# 1.4 Display test data dataset:
from my_classes import TestDataProvider
#TestDataProvider(IdealFunktionProvider('y1').return_columname()).show_dataframe()
#TestDataProvider(IdealFunktionProvider('y2').return_columname()).show_dataframe()
#TestDataProvider(IdealFunktionProvider('y3').return_columname()).show_dataframe()
#TestDataProvider(IdealFunktionProvider('y4').return_columname()).show_dataframe()