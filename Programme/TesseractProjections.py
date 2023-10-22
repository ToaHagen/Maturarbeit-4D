#Mit diesem Programm wurden 4 Bilder erstellt um die Unterschiede zwischen den Projektionen zu zeigen

#Importierung der Bibliotheken
import matplotlib.pyplot as plt
#Funktionen für Tesserakt wird aus Programm Tesserakt importiert
from Tesseract import *
#Grundlegende Definitionen
fig, ax = plt.subplots()
#Einstellungen für Rahmen und Achsen
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
plt.axis('equal')
plt.axis('off')

#Erstellung des Bildes
tesseract(0,0,0,0, -20,70,0, 20,10,0, 4,8,
          "cc",
          ax)
#Durch die Auswahl von pp,cp,pc oder cc kann die Projektion verändert werden
plt.show()