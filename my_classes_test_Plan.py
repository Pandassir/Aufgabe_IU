


#class DataTableProvider: 
    
#def downlaod(self):        --> erhalte einen dataframe --> teste, ob Dataframe erhalten!, evt, ob der rivhtige erhalten, teste Exception
#def upload_as(self, name): --> hat es wirklich geuploaded? --> Mocken?!, teste Exception
    

#class TrainDataProvider(DataTableProvider):
#def create_dataframe(self):--> erhalte enen dataframe --> teste, on Dataframe erhalten, evt. ob der richtige erhalten
#def show_dataframe(self):  --> erhalte ein print , teste Exception
       
#class IdealFunktionProvider(TrainDataProvider):
#def find(self):            --> erhalte einen Dataframe --> teste, ob Dataframe erhalten, evt. ob richtigeb erhalten
#def show_dataframe(self):  --> erhalte ein print (nicht testen)
#def return_columname(self):--> erhalte y- Wert --> teste, ob richtigen y-Wert erhalten
#def show_columnname(self): --> erhalte ein print (nicht testen)

#class MaxDeltaFinder(TrainDataProvider):
#def find(self):            --> erhalte max delta für jeden y-Wert --> teste auf Zahlenwert max delta
#def show_maxdelta(self):   --> erhalte ein print (nicht testen)
#def average_maxdelte(self):--> erhalte einen Zahlenwert, teste auf Zahlenwert

#class TestDataProvider:
#def find(self):            --> erhalte gefilterten Dataframe, teste ob genau der df erhalten wird! evt mocken?
#def show_dataframe(self):  --> erhalte ein print (nicht testen)
#def return_dataframe(self):--> erhalte einen Dataframe --> teste, ob Dataframe erhalten, evt. ob richtigeb erhalten

#class IdealGraphProvider:
#def show_idealfunctions(self): --> erhalte ein plot --> teste, ob plot erhalten

#class TestDataGraphProvider(IdealGraphProvider):
#def show_testdata(self):        --> erhalte ein plot --> teste, ob plot erhalten
#def show_fitted_testdata(self): --> erhalte ein plot --> teste, ob plot erhalten

#class HTMLProvider(DataTableProvider):
#def show(self): --> erhalte html --> teste, ob html erhalten, teste Exception
        
        
    
