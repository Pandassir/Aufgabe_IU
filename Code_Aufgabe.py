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

''' Least Square für  y1 bzw. der V-Form:'''
x = df.iloc[:]['x']
y = df.iloc[:]['y1']


z = np.polyfit(x, y, 200)
p = np.poly1d(z)

xp = np.linspace(-19, 19, 100)
plt.plot(x, y, '.', xp, p(xp))
plt.show()

''' Least Square für  y2 bzw. der Geraden:'''
x = df.iloc[:]['x']
y = df.iloc[:]['y2']


z = np.polyfit(x, y, 200)
p = np.poly1d(z)

xp = np.linspace(-19, 19, 10)
plt.plot(x, y, '.', xp, p(xp))
plt.show()

''' Least Square für  y3 bzw. der Sinus-Kurve:'''
x = df.iloc[:]['x']
y = df.iloc[:]['y3']


z = np.polyfit(x, y, 200)
p = np.poly1d(z)

xp = np.linspace(-16, 16, 10000)
plt.plot(x, y, '.', xp, p(xp))
plt.show()

''' Least Square für  y4 bzw. der flacheb V-Form:'''   
x = df.iloc[:]['x']
y = df.iloc[:]['y4']


z = np.polyfit(x, y, 200)
p = np.poly1d(z)


xp = np.linspace(-19, 19, 50)
plt.plot(x, y, '.', xp, p(xp))
plt.show()

#3.1 Visualisierung der berechneten Funktionen:
'''Zur Visualisierung wurde folgende Quelle verwendet:
    https://www.youtube.com/watch?v=BIO7_uro2CQ'''

x = df.iloc[:]['x']
y = df.iloc[:]['y1']

fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
fig.suptitle('Datenplot und erhaltene Funktion')
axs[0][0].set_title('Funktion y1')
axs[0][1].set_title('Funktion y2')
axs[1][0].set_title('Funktion y3')
axs[1][1].set_title('Funktion y4')
#axs[2][0].set_title('Datensatz y3')
#axs[2][1].set_title('Fubktion y3')
#axs[3][0].set_title('Datensatz y4')
#axs[3][1].set_title('Funktion y4')

axs[0][0].plot(x,y)
axs[0][1].plot(x,y)
axs[1][0].plot(x,y)
axs[1][1].plot(x,y)
#axs[2][0].set_title('Datensatz y3')
#axs[2][1].set_title('Fubktion y3')
#axs[3][0].set_title('Datensatz y4')
#axs[3][1].set_title('Funktion y4')

