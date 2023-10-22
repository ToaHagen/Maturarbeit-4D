#In diesem Programm wird die Animation erstellt, in der ein Tesserakt anfangs wegen der grossen Entfernung wie ein Würfel aussieht

#Importierung der Bibliotheken
import matplotlib.animation as animation
#Funktionen für Tesserakt wird aus Programm Tesserakt importiert
from Tesseract import *
#Standard Tesserakt wird verwendet
tess=getTesseract()
# Alternative Einfärbung des Tesseraktes
# tess=getRawTesseract()
# for b in range(32):
#         if tess[b][0][3]==1 and tess[b][1][3]==1 and tess[b][0][2]==1 and tess[b][1][2]==1:
#             tess[b].append('tab:green')
#         elif tess[b][0][3]==-1 and tess[b][1][3]==-1 and tess[b][0][2]==1 and tess[b][1][2]==1:
#             tess[b].append('tab:blue')
#         elif tess[b][0][3] != tess[b][1][3] and tess[b][0][2]==1 and tess[b][1][2]==1:
#             tess[b].append('tab:orange')
#         else:
#             tess[b].append('tab:gray')
def animate(i):
    #Löschung des vorherigen Bildes
    plt.cla()
    #Gleichmässige Achsen
    plt.axis('equal')
    #Entfernung des Randes
    plt.axis('off')
    #Grösse des Bildes kontrollieren
    plt.plot([-3,3],[0,0],color='white')
    t=i
    #Animation der Teile des Videos
    if t <= 10:
        # Würfel ist sichtbar
        tesseract(0,0,0,0, 30,-40,0,0,0,0, 0,8,"pc",ax,tess)
    elif t <= 30:
        #Verwandlung des Würfels in Tesserakt
        tesseract(0,0,0,0, 30,-40,0,0,0,0, -(10000/((((t-10)/2)**5)+1)+4),8,"cc",ax,tess)

#Definition des Grundlegendes Bildes    
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion
                               interval=100,#Zeit zwischen Bildern in ms
                               frames=30,   #Anzahl Bilder
                               repeat=False, blit=False)


#Für die Speicherung des Videos. Entkommentieren zum abspeichern
# writer = animation.FFMpegWriter(fps=10) 
# anim.save('Saves/CubeToTesserakt.mp4', writer=writer)

plt.show()