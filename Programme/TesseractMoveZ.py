#Programm für Animation der Translation eines Tesseraktes in z-Dimension

#Importierung der Bibliotheken
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Funktionen für Tesserakt wird aus Programm Tesserakt importiert
from Tesseract import *
#Standard Tesserakt wird verwendet
tess=getTesseract()
def animate(i):
    #Löschung des vorherigen Bildes
    plt.cla()
    #Gleichmässige Achsen
    plt.axis('equal')
    #Entfernung des Randes
    plt.axis('off')
    #Grösse des Bildes kontrollieren
    plt.plot([-3,3],[0,0],color='white')
    tesseract(0,0,-0.1*i,0, (20+0),250,0,0,0,0, 4,8,"cc",ax,tess)

#Definition des Grundlegendes Bildes    
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion
                               interval=100,#Zeit zwischen Bildern in ms
                               frames=60,   #Anzahl Bilder
                               repeat=False, blit=False)

#Für die Speicherung des Videos. Entkommentieren zum abspeichern
# writer = animation.FFMpegWriter(fps=10) 
# anim.save('Saves/TesseraktMoveZ.mp4', writer=writer)

plt.show()