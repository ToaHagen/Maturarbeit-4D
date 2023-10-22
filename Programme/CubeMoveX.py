#In diesem Programm wird die Animation der Translation eines Würfels in x-Dimension erstellt

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
    plt.plot([-2,5.5],[0,0],color='white')

    #Malen des Bildes
    cube(0.1*i, #Translation in x-Dimension
         0,0, 0,0,0, 4,"c",Cube)

#Definition des Grundlegendes Bildes    
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion für das Bild
                               interval=100,#Zeit zwischen Bildern in ms
                               frames=30,   #Anzahl Bilder
                               repeat=False, blit=False)

#Für die Speicherung des Videos. Entkommentieren zum abspeichern
# writer = animation.FFMpegWriter(fps=10) 
# anim.save('Saves/CubeMoveX.mp4', writer=writer)

plt.show()