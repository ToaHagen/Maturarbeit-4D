#In diesem Programm wird das Bild eines Würfels erzeugt, der zentralprojiziert wird.
#Anschliessend wird aus der Rotation des Würfels eine Animation gemacht

#Importierung der Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#Definitione des Würfels
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
#Funktione für die Rotation XY
def rotatePointXY(point,a):
    #Rotationsmatrix
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
#Leinwand und Abbild erstellen
def canvasPoint(point,v,c):
    return([point[0]* (v-c)/(v-point[2]), #Formel für Zentralprojektion
            point[1]* (v-c)/(v-point[2]),
            c])
def canvasLine(line,v,c):
    return([canvasPoint(line[0],v,c),canvasPoint(line[1],v,c),line[2]])
def canvasCorner(corner,v,c):
    return([canvasPoint(corner[0],v,c),corner[1]])
def canvasRay(corner,v,c):
    return([corner[0],[0,0,v],corner[1]])
def createCanvas(cube,v,c):
    canvas=[]
    canvas.append(list(map(canvasLine,cube[0],np.full((12),v),np.full((12),c))))
    canvas.append(list(map(canvasCorner,cube[1],np.full((12),v),np.full((8),c))))
    canvas.append(list(map(canvasRay,cube[1],np.full((12),v),np.full((8),c))))
    canvas.append([[2,2,c],[2,-2,c],[-2,-2,c],[-2,2,c]])
    canvas.append([[0,0,v],'k'])
    return(canvas)
    
#Funktionen für die Rotation von Würfel und Leinwand gemeinsam
def turnCube(cube,a):
    return(rotateCubeXZ(cube,a))
def turnCanvas(canvas,a):
    return([list(map(rotateLineXZ,canvas[0],np.full(12,a))),
            list(map(rotateCornerXZ,canvas[1],np.full(12,a))),
            list(map(rotateLineXZ,canvas[2],np.full(12,a))),
            list(map(rotatePointXZ,canvas[3],np.full(4,a))),
            rotateCornerXZ(canvas[4],a)
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
def projectCentralPoint(p,v) :
    return([p[0]*v/(v-p[2]),p[1]*v/(v-p[2])])
def projectCentralLine(line,v) :
    return([projectCentralPoint(line[0],v),projectCentralPoint(line[1],v),line[2]])
def projectCentralCorner(corner,v):
    return([projectCentralPoint(corner[0],v),corner[1]])
def projectCentralCube(cube,viewdistance):
    return([list(map(projectCentralLine,cube[0],np.full(12,viewdistance))),
            list(map(projectCentralCorner,cube[1],np.full(8,viewdistance)))])
def projectCentralCanvas(canvas,viewdistance):
    return([list(map(projectCentralLine,canvas[0],np.full(12,viewdistance))),
            list(map(projectCentralCorner,canvas[1],np.full(8,viewdistance))),
            list(map(projectCentralLine,canvas[2],np.full(12,viewdistance))),
            list(map(projectCentralPoint,canvas[3],np.full(4,viewdistance))),
            projectCentralCorner(canvas[4],viewdistance)
            ])
#Funktinen für das Zeichnen
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
    
    plotCorner(canvas[4])
#Funktion zur Erstellung des Bildes
def image(t):
    # Rotation von Würfel und Leinwand
    a=50 #50
    #Abstand der Leinwad bei der Projektion von Würfel und Leinwand zum angezeigten Bild 
    v=-14 #-12 #-500

    # Der Würfel wird gedreht
    c=rotateCubeXY(Cube,(np.pi)*  t  /180) #(30)    #Nummer des Bildes beinflusst Rotation des Würfels
    c=rotateCubeYZ(c,(np.pi)*30/180) #30
    c=rotateCubeXZ(c,(np.pi)*-15/180) #20 #-15

    # Die Komponenten des Würfels werden nach ihrer Z Achse sotiert damit das Leinwandbild richtig angefertigt wird
    c=[sortLine(c[0],-1),sortCorner(c[1])]

    # Das Abbild des Würfels wird gemacht
    Canvas=createCanvas(c, #Würfel
                        12,#Abstand Beobachtungspunkt
                        5) #Abstand Leinwand

    # Leinwand und Würfel werden im Raum gedreht, so das beides sichtbar ist
    Canvas=turnCanvas(Canvas,(np.pi)*a/180)
    c=turnCube(c,(np.pi)*a/180)

    # Die Komponenten des Würfels werden nach der Z Achse sotiert
    c=[sortLine(c[0],1),sortCorner(c[1])]

    # Würfel und Leinwand werden für den Beobachter perspektivisch projiziert
    Canvas=projectCentralCanvas(Canvas,v)
    c=projectCentralCube(c,v)

    # Alles wird der Reihe nach gemalt
    if a in range(-90,90) or a in range(270,450): 
        plotCanvas(Canvas)
        plotCube(c)
    else :
        plotCube(c)
        plotCanvas(Canvas)
def animate(i):
    #Vorheriges Bild wird gelöscht
    plt.cla()
    #Rand wird entfernt
    plt.axis('off')
    #Axen sind gleich
    plt.axis('equal')
    #Kontrolle der Bildgrösse
    plt.plot([0,2],[0,0],color='white')
    #Erstellung des Bildes
    image(i)

#Grundlegende Definitionen
fig, ax = plt.subplots()
#Entfernung des Rahmens
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
#Animation 
anim = animation.FuncAnimation(plt.gcf(), 
                               animate,     #Funktion die für jedes Bild aufgerufen wird
                               interval=100, #Zeitabstand zwischen Bilder in milisekunden (nicht für speicherung des Videos)
                               frames=360,  #Anzahl Bilder in der Animation
                               repeat=False, blit=False) #weitere Definitionen

#Speicherung der Animation. Entkommentieren zum abspeichern
#writer = animation.FFMpegWriter(fps=10) #Anzahl Bilder pro Sekunde im gespeicherten Video
#anim.save('Saves/CubeCentralProjection.mp4', writer=writer)

#Animataion anzeigen
plt.show()