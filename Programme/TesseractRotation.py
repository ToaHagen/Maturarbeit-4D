#Programm zu Translation eines Tesseraktes in w-Dimension

#Importierung der Bibliotheken
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Funktionen für Tesserakt wird aus Programm Tesserakt importiert
from Tesseract import *
#Standard Tesserakt wird verwendet
tess=getTesseract()
#Alternative Einfärbungen des Tesseraktes
# tess=getRawTesseract()
# for b in range(32):
#         if tess[b][0][3]==1 and tess[b][1][3]==1 and tess[b][0][2]==-1 and tess[b][1][2]==-1:
#             tess[b].append('tab:blue')
#         elif tess[b][0][3]==-1 and tess[b][1][3]==-1 and tess[b][0][2]==-1 and tess[b][1][2]==-1:
#             tess[b].append('tab:green')
#         elif tess[b][0][3] != tess[b][1][3] and tess[b][0][2]==-1 and tess[b][1][2]==-1:
#             tess[b].append('tab:orange')
#         else :
#             tess[b].append('tab:gray')
#Alternative Einfärbungen des Tesseraktes
# tess=getRawTesseract()
# for b in range(32):
#         if tess[b][0][3]==1 and tess[b][1][3]==1 and tess[b][0][0]==1 and tess[b][1][0]==1:
#             tess[b].append('tab:blue')
#         elif tess[b][0][3]==-1 and tess[b][1][3]==-1 and tess[b][0][0]==1 and tess[b][1][0]==1:
#             tess[b].append('tab:green')
#         elif tess[b][0][3] != tess[b][1][3] and tess[b][0][0]==1 and tess[b][1][0]==1:
#             tess[b].append('tab:orange')
#         else :
#             tess[b].append('tab:gray')
def animate(i):
    #Löschung des vorherigen Bildes
    plt.cla()
    #Gleichmässige Achsen
    plt.axis('equal')
    #Entfernung des Randes
    plt.axis('off')
    #Grösse des Bildes kontrollieren
    plt.plot([-2.5,2.5],[0,0],color='white')
    plt.plot([0,0],[-2.3,2],color='white')

    #Erstellen des Bildes
    # Durch setzen des i kann die Rotation gewählt werden
    tesseract(0,0,0,0, 
              0,    #Rotation xy
              -20,    #Rotation xz
              20,    #Rotation yz
              -i,    #Rotation xw
              0,    #Rotation yw
              0,    #Rotation zw
              4,8,"cc",ax,tess)

#Definition des Grundlegendes Bildes    
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion
                               interval=100,#Zeit zwischen Bildern in ms
                               frames=360,   #Anzahl Bilder
                               repeat=False, blit=False)

#Für die Speicherung des Videos. Entkommentieren zum abspeichern
# writer = animation.FFMpegWriter(fps=10) 
# anim.save('Saves/TesseraktRotationXW.mp4', writer=writer)

plt.show()