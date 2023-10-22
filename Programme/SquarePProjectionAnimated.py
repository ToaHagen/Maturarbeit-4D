#In diesem Programm wird das Video zur Parallelprojektion des Quadrates erstellt

#Importierung der Bibliotheken
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Importierung der Funktion für das Bild aus dem Programm SquarePProjection
from SquarePProjection import projection 
#Funktion die für jedes Bild des Videos aufgerufen wird
def animate(i): # i ist die Nummer des Bildes im Video
    #Löschung des vorherigen Bildes
    plt.cla()
    #Gleichmässige Achsen
    plt.axis('equal')
    #Entfernung des Randes
    plt.axis('off')
    #Grösse des Bildes kontrollieren
    plt.plot([-3,1.7],[0,0],color='white')
    #Bild mit importierter Funktion erstellen
    projection(i, #Winkel entspricht der Bildnummer
               3, #Abstand der Leinwand
               ax)#Grundlegendes Bild weitergeben

#Definition des Grundlegendes Bildes    
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #aufgerufene Funktionen
                               interval=100, #Zeit zwischen Bildern in milisekunden (nicht für das gespeicherte Video)
                               frames=361,  #Amzahl Bilder
                               repeat=False,blit=False) #Weitere Einstellungen 

#Für die Speicherung des Videos. Entkommentieren zum abspeichern
#writer = animation.FFMpegWriter(fps=10) #Bilder pro Sekunde 
#anim.save('Saves/SquarePProjection.mp4', writer=writer)

#Animation anzeigen
plt.show()