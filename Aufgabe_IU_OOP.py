
# 1. Download der gegebenen Daten aus MySQL:
    
from klassen import Datentabelle
''' die Abkürzung df steht für Dataframe'''       
df_train = Datentabelle('train').downlaod()                                     # Die Traingsdatentabelle wird gedownlodet
df_ideal = Datentabelle('ideal').downlaod()                                     # Die Idealdatentabelle wird gedownloadet
df_test = Datentabelle('test').downlaod()                                       # Die Testdatentabelle wird gedownloadet


# 2. Aufbereitung Trainingsdatensatz:

from klassen import TrainDataProvider
'''Erstellung organisierter Dataframes mit x und einem y-Wert'''
df_train_xy1 = TrainDataProvider('y1').create()                                 # Dataframe besteht aus x und y vom Trainingsdatensatz
df_train_xy2 = TrainDataProvider('y2').create()                                 # Dataframe besteht aus x und y vom Trainingsdatensatz
df_train_xy3 = TrainDataProvider('y3').create()                                 # Dataframe besteht aus x und y vom Trainingsdatensatz
df_train_xy4 = TrainDataProvider('y4').create()                                 # Dataframe besteht aus x und y vom Trainingsdatensatz


# 3. Finden der Idealen Funktionen:
    
from klassen import IdealFunktionProvider
''' Der Finder soll zu den Trainingsdaten die idealen Funktionen finden'''
df_ideal_y1_y36 = IdealFunktionProvider('y1').find()                            # Dataframe besteht aus x und y vom gefundenen Idealdatensatz
df_ideal_y2_y11 = IdealFunktionProvider('y2').find()                            # Dataframe besteht aus x und y vom gefundenen Idealdatensatz
df_ideal_y3_y2  = IdealFunktionProvider('y3').find()                            # Dataframe besteht aus x und y vom gefundenen Idealdatensatz
df_ideal_y4_y33 = IdealFunktionProvider('y4').find()                            # Dataframe besteht aus x und y vom gefundenen Idealdatensatz

def show_dataframe():
    IdealFunktionProvider('y1').show_dataframe()                                # Zeigt den gefundenen Dataframe an
    IdealFunktionProvider('y2').show_dataframe()                                # Zeigt den gefundenen Dataframe an
    IdealFunktionProvider('y3').show_dataframe()                                # Zeigt den gefundenen Dataframe an
    IdealFunktionProvider('y4').show_dataframe()                                # Zeigt den gefundenen Dataframe an

IdealFunktionProvider('y1').show_columnname()                                   # Zeigt den Namen der passenden idealen Funktion an
IdealFunktionProvider('y2').show_columnname()                                   # Zeigt den Namen der passenden idealen Funktion an
IdealFunktionProvider('y3').show_columnname()                                   # Zeigt den Namen der passenden idealen Funktion an
IdealFunktionProvider('y4').show_columnname()                                   # Zeigt den Namen der passenden idealen Funktion an


from klassen import MaxDeltaFinder
md1 = MaxDeltaFinder('y1').find()                                               # Findet die maximale Abweichung zwischen y1-Traingsdatensatz und dem dazugehörigen Idealdatensatz
md2 = MaxDeltaFinder('y2').find()                                               # Findet die maximale Abweichung zwischen y2-Traingsdatensatz und dem dazugehörigen Idealdatensatz
md3 = MaxDeltaFinder('y3').find()                                               # Findet die maximale Abweichung zwischen y3-Traingsdatensatz und dem dazugehörigen Idealdatensatz
md4 = MaxDeltaFinder('y4').find()                                               # Findet die maximale Abweichung zwischen y4-Traingsdatensatz und dem dazugehörigen Idealdatensatz 

MaxDeltaFinder('y1').show_maxdelta()                                            # Zeigt die Abweichung an
MaxDeltaFinder('y2').show_maxdelta()                                            # Zeigt die Abweichung an
MaxDeltaFinder('y3').show_maxdelta()                                            # Zeigt die Abweichung an
MaxDeltaFinder('y4').show_maxdelta()                                            # Zeigt die Abweichung an

md_avrg = (md1+md2+md3+md4)/4                                                   # #Zeigt die durchschnittliche Abweichung an
print('\nFür die weitere Bearbeitung wurde folgender Durchschnittswert', 
      'verwendet:', md_avrg)

from klassen import TrainDataFinder







class OutputDataGraphProvider:
    pass