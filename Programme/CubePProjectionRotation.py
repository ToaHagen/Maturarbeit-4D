#Mit diesem Programm werden Bilder und Animationen erstellt bei denen ein Würfel auf eine Leinwand Parallelprojiziert wird
#In der Animation drehen sich Würfel und Leinwand gemeinsam

#Importierung der Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Definition des Würfels
Cube=[[[[1,1,1],  [1,1,-1],   'tab:blue'],
      [[1,-1,1],  [1,-1,-1],  'tab:blue'],
      [[-1,1,1],  [-1,1,-1],  'tab:blue'],
      [[-1,-1,1], [-1,-1,-1], 'tab:blue'],
      [[1,1,1],   [1,-1,1],   'tab:orange'],
      [[1,1,-1],  [1,-1,-1],  'tab:orange'],
      [[-1,1,1],  [-1,-1,1],  'tab:orange'],
      [[-1,1,-1], [-1,-1,-1], 'tab:orange'],
      [[1,1,1],   [-1,1,1],   'tab:green'],
      [[1,1,-1],  [-1,1,-1],  'tab:green'],
      [[1,-1,1],  [-1,-1,1],  'tab:green'],
      [[1,-1,-1], [-1,-1,-1], 'tab:green']],
      [[[1,1,1],  'tab:cyan'],
      [[1,1,-1],  'tab:olive'],
      [[1,-1,1],  'tab:purple'],
      [[1,-1,-1], 'tab:red'],
      [[-1,1,1],  'tab:red'],
      [[-1,1,-1], 'tab:purple'],
      [[-1,-1,1], 'tab:olive'],
      [[-1,-1,-1],'tab:cyan']]]
#Rotation in XY-Dimensionen
def rotatePointXY(point,a):
    m=np.matrix([[np.cos(a),(-1)*np.sin(a), 0],
                 [np.sin(a),np.cos(a),      0],
                 [0,        0,              1]])
    return(list(np.asarray(m.dot(point)).flatten()))
def rotateLineXY(line,a):
    return([rotatePointXY(line[0],a),rotatePointXY(line[1],a),line[2]])
def rotateCornerXY(corner,a):
    return([rotatePointXY(corner[0],a),corner[1]])
def rotateCubeXY(cube,a):
    return([list(map(rotateLineXY,cube[0],np.full(12,a))), list(map(rotateCornerXY,cube[1],np.full(8,a)))])
#Rotation YZ
def rotatePointYZ(point,a):
    m=np.matrix([[1, 0,          0],
                 [0, np.cos(a),  (-1)*np.sin(a)],
                 [0, np.sin(a),  np.cos(a)]])
    return(list(np.asarray(m.dot(point)).flatten()))
def rotateLineYZ(line,a):
    return([rotatePointYZ(line[0],a),rotatePointYZ(line[1],a),line[2]])
def rotateCornerYZ(corner,a):
    return([rotatePointYZ(corner[0],a),corner[1]])
def rotateCubeYZ(cube,a):
    return([list(map(rotateLineYZ,cube[0],np.full(12,a))), list(map(rotateCornerYZ,cube[1],np.full(8,a)))])
#Rotation XZ
def rotatePointXZ(point,a):
    m=np.matrix([[np.cos(a), 0, (-1)*np.sin(a)],
                 [0,         1, 0],
                 [np.sin(a), 0, np.cos(a)]])
    return(list(np.asarray(m.dot(point)).flatten()))
def rotateLineXZ(line,a):
    return([rotatePointXZ(line[0],a),rotatePointXZ(line[1],a),line[2]])
def rotateCornerXZ(corner,a):
    return([rotatePointXZ(corner[0],a),corner[1]])
def rotateCubeXZ(cube,a):
    return([list(map(rotateLineXZ,cube[0],np.full(12,a))), list(map(rotateCornerXZ,cube[1],np.full(8,a)))])
#Erstellung der Leinwand mit Abbild
def canvasPoint(point,d):
    return([point[0],point[1],d])
def canvasLine(line,d):
    return([canvasPoint(line[0],d),canvasPoint(line[1],d),line[2]])
def canvasCorner(corner,d):
    return([canvasPoint(corner[0],d),corner[1]])
def canvasRay(corner,d):
    return([corner[0],canvasPoint(corner[0],d),corner[1]])
def createCanvas(cube,d):
    canvas=[]
    canvas.append(list(map(canvasLine,cube[0],np.full((12),d))))
    canvas.append(list(map(canvasCorner,cube[1],np.full((8),d))))
    canvas.append(list(map(canvasRay,cube[1],np.full((8),d))))
    canvas.append([[2,2,5],[2,-2,5],[-2,-2,5],[-2,2,5]])
    return(canvas)
    
#Würfel und Leinwand rotieren
def turnCube(cube,a):
    return(rotateCubeXZ(cube,a))
def turnCanvas(canvas,a):
    return([list(map(rotateLineXZ,canvas[0],np.full(12,a))),
            list(map(rotateCornerXZ,canvas[1],np.full(12,a))),
            list(map(rotateLineXZ,canvas[2],np.full(12,a))),
            list(map(rotatePointXZ,canvas[3],np.full(4,a)))
            ])
#Linien und Ecken sortieren für Überscheneidungen
def sortLine(input,pole):
    zValues=[]
    output=[]
    for i in range(len(input)):
        zValues.append(((input[i][0][2])+(input[i][1][2]))/2)
    for i in range(len(input)):
        if pole > 0 :
            a=np.argmax(zValues)
            zValues[a]=-1000
        if pole < 0 :
            a=np.argmin(zValues)
            zValues[a]=1000
        output.append(input[a]) 
    return output
def sortCorner(x):
    s=[]
    y=[]
    for i in range(len(x)):
        s.append(x[i][0][2])
    for i in range(len(x)):
        a=np.argmax(s)
        s[a]=-1000
        y.append(x[a]) 
    return (y)
#Funktionen Projektion von Würfel und Leinwand mit Abbild zum 2D-Bild das angezeigt wird
def projectPerspectivePoint(p,v) :
    return([p[0]*v/(v-p[2]),p[1]*v/(v-p[2])])
def projectPerspectiveLine(line,v) :
    return([projectPerspectivePoint(line[0],v),projectPerspectivePoint(line[1],v),line[2]])
def projectPerspectiveCorner(corner,v):
    return([projectPerspectivePoint(corner[0],v),corner[1]])
def projectPerspectiveCube(cube,viewdistance):
    
    return([list(map(projectPerspectiveLine,cube[0],np.full(12,viewdistance))),
            list(map(projectPerspectiveCorner,cube[1],np.full(8,viewdistance)))])

def projectPerspectiveCanvas(canvas,viewdistance):
    return([list(map(projectPerspectiveLine,canvas[0],np.full(12,viewdistance))),
            list(map(projectPerspectiveCorner,canvas[1],np.full(8,viewdistance))),
            list(map(projectPerspectiveLine,canvas[2],np.full(12,viewdistance))),
            list(map(projectPerspectivePoint,canvas[3],np.full(4,viewdistance)))
            ])
#Funktionen für die Zeichnung
def plotLine(line):
    plt.plot([line[0][0],line[1][0]],[line[0][1],line[1][1]],color=line[2],linewidth=5)
def plotCorner(corner):
    plt.plot(corner[0][0],corner[0][1],color=corner[1],marker='o',markersize=7)
def plotCube(cube):
    [plotLine(x)for x in cube[0]]
    [plotCorner(y)for y in cube[1]]
def plotRay(ray):
    plt.plot([ray[0][0],ray[1][0]],[ray[0][1],ray[1][1]],color=ray[2],linewidth=1,linestyle='--')
def plotCanvas(canvas):
    field=np.array(canvas[3])
    plt.scatter(field[:, 0], field[:, 1], s = 0, color = 'red')
    plt.gca().add_patch(plt.Polygon(field[:, :2], color='lightgray'))
    [plotLine(a)for a in canvas[0]]
    [plotCorner(b)for b in canvas[1]]
    [plotRay(c)for c in canvas[2]]
def image(t):
    #Rotation von Würfel und Leinwand mit t dreht sie sich immer weiter
    a=50+t #50
    #Abstand des Beobachtungspunktes 
    v=-12 #-12 #-500 

    # Der Würfel wird gedreht
    c=rotateCubeXY(Cube,(np.pi)*0/180) #(30)
    c=rotateCubeYZ(c,(np.pi)*30/180) #30
    c=rotateCubeXZ(c,(np.pi)*-15/180) #20

    # Die Komponenten des Würfels werden nach ihrer Z Achse sotiert damit das Leinwandbild richtig angefertigt wird.
    c=[sortLine(c[0],-1),sortCorner(c[1])]

    # Das Leinwandbild des Würfels wird gemacht
    Canvas=createCanvas(c,5)

    # Leinwand und Würfel werden im Raum gedreht, so das beides gut sichtbar ist
    Canvas=turnCanvas(Canvas,(np.pi)*a/180)
    c=turnCube(c,(np.pi)*a/180)

    # Die Komponenten des Würfels werden nach der Z Achse sotiert
    c=[sortLine(c[0],1),sortCorner(c[1])]

    # Würfel und Leinwand werden für den Beobachter perspektivisch projiziert
    Canvas=projectPerspectiveCanvas(Canvas,v)
    c=projectPerspectiveCube(c,v) 

    # Alles wird der Reihe nach gemahlt
    if a in range(-90,90) or a in range(270,450): 
        plotCanvas(Canvas)
        plotCube(c)
    else :
        plotCube(c)
        plotCanvas(Canvas)
def animate(i):
    #Löschung des vorherigen Bildes 
    plt.cla()
    #Rand und Axen entfernen
    plt.axis('off')
    #Axen Verhältnis 1:1
    plt.axis('equal')
    #Erstellung des Bildes
    image(i)

#Grundlegende definitionen
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

#Animation
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion die bei jedem Bild aufgerufen wird.
                               interval=100,#Zeitabstand zwischen Bilder in milisekunden (nicht für speicherung des Videos)
                               frames=360,  #Anzahl Bilder in der Animation
                               repeat=False, blit=False) #Weitere Einstellungen

#Speicherung der Animation. Entkommentieren zum abspeichern
#writer = animation.FFMpegWriter(fps=10) #Bilder pro Sekunde
#anim.save('Saves/CubeParallelProjectionRotation.mp4', writer=writer)

#Animation anzeigen
plt.show()