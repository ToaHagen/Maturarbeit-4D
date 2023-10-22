#Mit diesem Programm werden Animationen für verschiedene Rotationen erstellt

#Importierung der Bibliotheken
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
#Weitere alternative Definition des Würfels mit teilweiser grauer Einfärbung
# Cube=[[[[1,1,1],  [1,1,-1],   'tab:orange'],
#       [[1,-1,1],  [1,-1,-1],  'tab:orange'],
#       [[-1,1,1],  [-1,1,-1],  'tab:gray'],
#       [[-1,-1,1], [-1,-1,-1], 'tab:gray'],
#       [[1,1,1],   [1,-1,1],   'tab:blue'],
#       [[1,1,-1],  [1,-1,-1],  'tab:green'],
#       [[-1,1,1],  [-1,-1,1],  'tab:gray'],
#       [[-1,1,-1], [-1,-1,-1], 'tab:gray'],
#       [[1,1,1],   [-1,1,1],   'tab:gray'],
#       [[1,1,-1],  [-1,1,-1],  'tab:gray'],
#       [[1,-1,1],  [-1,-1,1],  'tab:gray'],
#       [[1,-1,-1], [-1,-1,-1], 'tab:gray']],
#       [[[1,1,1],  'tab:blue'],
#       [[1,1,-1],  'tab:green'],
#       [[1,-1,1],  'tab:blue'],
#       [[1,-1,-1], 'tab:green'],
#       [[-1,1,1],  'tab:gray'],
#       [[-1,1,-1], 'tab:gray'],
#       [[-1,-1,1], 'tab:gray'],
#       [[-1,-1,-1],'tab:gray']]]
# Cube=[[[[1,1,1],  [1,1,-1],   'tab:orange'],
#       [[1,-1,1],  [1,-1,-1],  'tab:orange'],
#       [[-1,1,1],  [-1,1,-1],  'tab:orange'],
#       [[-1,-1,1], [-1,-1,-1], 'tab:orange'],
#       [[1,1,1],   [1,-1,1],   'tab:gray'],
#       [[1,1,-1],  [1,-1,-1],  'tab:gray'],
#       [[-1,1,1],  [-1,-1,1],  'tab:gray'],
#       [[-1,1,-1], [-1,-1,-1], 'tab:gray'],
#       [[1,1,1],   [-1,1,1],   'tab:blue'],
#       [[1,1,-1],  [-1,1,-1],  'tab:green'],
#       [[1,-1,1],  [-1,-1,1],  'tab:blue'],
#       [[1,-1,-1], [-1,-1,-1], 'tab:green']],
#       [[[1,1,1],  'tab:blue'],
#       [[1,1,-1],  'tab:green'],
#       [[1,-1,1],  'tab:blue'],
#       [[1,-1,-1], 'tab:green'],
#       [[-1,1,1],  'tab:blue'],
#       [[-1,1,-1], 'tab:green'],
#       [[-1,-1,1], 'tab:blue'],
#       [[-1,-1,-1],'tab:green']]]
def animate(i):
    #Löschung des vorherigen Bildes
    plt.cla()
    #Gleichmässige Achsen
    plt.axis('equal')
    #Entfernung des Randes
    plt.axis('off')
    #Grösse des Bildes kontrollieren
    plt.plot([-3,3],[0,0],color='white')

    #Erzeugen des Bildes
    cube(0,0,0, 
         #Durch setzten des i kann die art der Rotation definiert werden
         0, #Rotation xy
         i, #Rotation xz
         0, #Rotation yz
         4,"c",Cube)

#Definition des Grundlegendes Bildes    
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion für das Bild
                               interval=100,#Zeit zwischen Bildern in ms
                               frames=360,   #Anzahl Bilder
                               repeat=False, blit=False)

#Für die Speicherung des Videos. Entkommentieren zum abspeichern
# writer = animation.FFMpegWriter(fps=10) 
# anim.save('Saves/CubeRotation.mp4', writer=writer)

plt.show()