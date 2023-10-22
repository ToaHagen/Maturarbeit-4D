#In diesem Programm wird das Video zur Zentralprojektion des Quadrates erstellt

#Bibliotheken importieren
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Importierung der Funktion für das Bild aus dem Programm SquareCProjection
from SquareCProjection import projection
#Funktion die für die Bilder des Videos aufgerufen wird
def animate(i):
    #vorheriges Bild löschen
    plt.cla()
    #Achsen gleichmässig machen
    plt.axis('equal')
    #Rand wird entfernt
    plt.axis('off')
    #Kontrolle der Bildgrösse
    plt.plot([-3,1.7],[0,0],color='white')
    #Funktion für das Bild
    projection(i,-2,-3,ax)

#Grundlegende Definition
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion zur erstellung des Bildes
                               interval=100, #Zeitabstand der Bilder in milisekunden (nicht im Video)
                               frames=361,  #Anzahl Bilder
                               repeat=False, blit=False) #weiter Definitionen

#Abspeicherung des Videos. Entkommentieren zum abspeichern
# writer = animation.FFMpegWriter(fps=10) #Bilder pro Sekunde
# anim.save('Saves/SquareCentralProjection.mp4', writer=writer)

#Animation anzeigen
plt.show()