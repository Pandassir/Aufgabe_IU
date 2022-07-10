#1. Traingsdaten einlesen
#2. Trainingsdaten aufbereiten(Rauschen entfernen mit least square)
#3. Kurven fitten
#4. Güte messen mit Testdaten 



#1. Einlesen der CSV-Datei:
    
''' laden der Bibliotheken zur Erstellumg der Dataframes'''
import pandas as pd
import numpy as np
print(pd.__version__)

''' Einlesem der CSV Datei'''
df = pd.read_csv("Datensatz/train.csv")

''' Dataframe amschauem'''
print(df)
print('Handelt es sich um einen Dataframe?:',(isinstance(df, pd.DataFrame)))




#2. Visualisierung der einzelnen Datensätze:
    
'''Den Datensatz visualisierem'''
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

'''Auswahl meines Styles'''
style.use('ggplot')

''' Erstellumg des Figure-Object und Axis-Object'''
fig, ax = plt.subplots(figsize=(6,4))

''' Als nächstes sollen die Kurven visualisiert werden. Dafür wird die
iloc-Methode verwendet. Siehe:https://www.delftstack.com/de/howto/python-pandas/how-to-get-a-value-from-a-cell-of-a-dataframe/
'''
ax.plot(df.iloc[:]['x'], df.iloc[:]['y1'], label="Y1-Datensatz", linewidth=1, color = 'blue')
ax.plot(df.iloc[:]['x'], df.iloc[:]['y2'], label="Y2-Datensatz", linewidth=1, color = 'black')
ax.plot(df.iloc[:]['x'], df.iloc[:]['y3'], label="Y3-Datensatz", linewidth=1, color = 'purple')
ax.plot(df.iloc[:]['x'], df.iloc[:]['y4'], label="Y4-Datensatz", linewidth=1, color = 'orange')

ax.legend()
ax.grid(True,color="grey")
plt.ylabel('y Achse')
plt.xlabel('x Achse')
plt.title('Trainingsdatensatz')
plt.show()


#3. Finden der geschlossenen Funktion:
    
    