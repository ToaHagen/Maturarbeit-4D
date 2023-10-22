#In diesem Programm wird die Animation erstellt, in der ein Würfel anfangs wegen der grossen Entfernung wie ein Quadrat aussieht

#Importierung der Bibliotheken
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Importierung der Funktion für den Würfel aus dem Programm Cube
from Cube import cube
#Alternative Definition des Würfels mit anderen Farben
Cube=[[[[1,1,1],  [1,1,-1],   'tab:orange'],
      [[1,-1,1],  [1,-1,-1],  'tab:orange'],
      [[-1,1,1],  [-1,1,-1],  'tab:orange'],
      [[-1,-1,1], [-1,-1,-1], 'tab:orange'],
      [[1,1,1],   [1,-1,1],   'tab:blue'],
      [[1,1,-1],  [1,-1,-1],  'tab:green'],
      [[-1,1,1],  [-1,-1,1],  'tab:blue'],
      [[-1,1,-1], [-1,-1,-1], 'tab:green'],
      [[1,1,1],   [-1,1,1],   'tab:blue'],
      [[1,1,-1],  [-1,1,-1],  'tab:green'],
      [[1,-1,1],  [-1,-1,1],  'tab:blue'],
      [[1,-1,-1], [-1,-1,-1], 'tab:green']],
      [[[1,1,1],  'tab:blue'],
      [[1,1,-1],  'tab:green'],
      [[1,-1,1],  'tab:blue'],
      [[1,-1,-1], 'tab:green'],
      [[-1,1,1],  'tab:blue'],
      [[-1,1,-1], 'tab:green'],
      [[-1,-1,1], 'tab:blue'],
      [[-1,-1,-1],'tab:green']]]
def animate(i):
    #Löschung des vorherigen Bildes
    plt.cla()
    #Gleichmässige Achsen
    plt.axis('equal')
    #Entfernung des Randes
    plt.axis('off')
    #Grösse des Bildes kontrollieren
    plt.plot([-2.5,2.5],[0,0],color='white')


    t=i
    #Animation der Teile des Videos
    if t <= 10:
        #Nur Quadrat
        cube(0,0,0, 0,0,0, 0,"p",Cube)
    elif t <= 30:
        #Quadrat wird zu Würfel
        cube(0,0,0, 0,0,0, (10000/((((t-10)/2)**5)+1)+8),"c",Cube)
    elif t<= 60:
        #Würfel wird gedreht
        cube(0,0,0, t-30,0,0, 8,"c",Cube)
    elif t<= 100:
        #Würfel wird gedreht
        cube(0,0,0, 30,-t+60,0, 8,"c",Cube)

#Definition des Grundlegendes Bildes    
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion
                               interval=100,#Zeit zwischen Bildern in ms
                               frames=100,  #Anzahl Bilder
                               repeat=False, blit=False)

#Für die Speicherung des Videos. Entkommentieren zum abspeichern
# writer = animation.FFMpegWriter(fps=10) #Bilder pro Sekunde 
# anim.save('Saves/SquareToCube.mp4', writer=writer)

#Animation zeigen
plt.show()