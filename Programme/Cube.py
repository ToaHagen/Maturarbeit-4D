#Mit diesem Programm wird eine Funktion erstellt, mit der ein Würfel abgbildet, gedreht und bewegt werden kann

#Importierung der Bibliotheken
import numpy as np
import matplotlib.pyplot as plt

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

#Funktion für die Rotation in XY-Dimensionen
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

#Funktion für die Translation in X-Dimension
def movePointX(point,d):
    return([point[0]+d,point[1],point[2]])
def moveLineX(line,d):
    return([movePointX(line[0],d),movePointX(line[1],d),line[2]])
def moveCornerX(corner,d):
    return([movePointX(corner[0],d),corner[1]])
def moveCubeX(cube,d):
    return([list(map(moveLineX,cube[0],np.full(12,d))), list(map(moveCornerX,cube[1],np.full(8,d)))])

#Translation Y
def movePointY(point,d):
    return([point[0],point[1]+d,point[2]])
def moveLineY(line,d):
    return([movePointY(line[0],d),movePointY(line[1],d),line[2]])
def moveCornerY(corner,d):
    return([movePointY(corner[0],d),corner[1]])
def moveCubeY(cube,d):
    return([list(map(moveLineY,cube[0],np.full(12,d))), list(map(moveCornerY,cube[1],np.full(8,d)))])

#Translation Z
def movePointZ(point,d):
    return([point[0],point[1],point[2]+d])
def moveLineZ(line,d):
    return([movePointZ(line[0],d),movePointZ(line[1],d),line[2]])
def moveCornerZ(corner,d):
    return([movePointZ(corner[0],d),corner[1]])
def moveCubeZ(cube,d):
    return([list(map(moveLineZ,cube[0],np.full(12,d))), list(map(moveCornerZ,cube[1],np.full(8,d)))])

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
    zValues=[]
    y=[]
    for i in range(len(x)):
        zValues.append(x[i][0][2])
    for i in range(len(x)):
        a=np.argmin(zValues)
        zValues[a]=1000
        y.append(x[a]) 
    return (y)

#Funktionen für die Zentralprojektion
def projectCentralPoint(p,v) :
    return([p[0]*v/(v-p[2]),p[1]*v/(v-p[2])])
def projectCentralLine(line,v) :
    return([projectCentralPoint(line[0],v),projectCentralPoint(line[1],v),line[2]])
def projectCentralCorner(corner,v):
    return([projectCentralPoint(corner[0],v),corner[1]])
def projectCentralCube(cube,viewdistance):
    return([list(map(projectCentralLine,cube[0],np.full(12,viewdistance))),
            list(map(projectCentralCorner,cube[1],np.full(8,viewdistance)))])

#Funktionen für die Parallelprojektion
def projectParallelPoint(p) :
    return([p[0],p[1]])
def projectParallelLine(line) :
    return([projectParallelPoint(line[0]),projectParallelPoint(line[1]),line[2]])
def projectParallelCorner(corner):
    return([projectParallelPoint(corner[0]),corner[1]])
def projectParallelCube(cube):
    return([list(map(projectParallelLine,cube[0])),
            list(map(projectParallelCorner,cube[1]))])

#Funktionen fürs Zeichen
def plotLine(line):
    plt.plot([line[0][0],line[1][0]],[line[0][1],line[1][1]],color=line[2],linewidth=5)
def plotCorner(corner):
    plt.plot(corner[0][0],corner[0][1],color=corner[1],marker='o',markersize=7)
def plotCube(cube):
    [plotLine(x)for x in cube[0]]
    [plotCorner(y)for y in cube[1]]

#Funktion für das Bild des Würfels
def cube(x,         #Translation X
         y,         #Translation Y
         z,         #Translation Z
         xy,        #Rotation XY
         xz,        #Rotation XZ
         yz,        #Rotation YZ
         v,         #Abstand des Beobachtungspunktes
         mode,      #Auswahl der Projektion c:Zentralprojektion, p:Parallelprojektion
         c=Cube):   #Möglichkeit den Standardwürfel zu ersetzen

    # Der Würfel wird gedreht
    c=rotateCubeXY(c,(np.pi)*xy/180) #(30)
    c=rotateCubeXZ(c,(np.pi)*xz/180) #20 #-15
    c=rotateCubeYZ(c,(np.pi)*yz/180) #30

    # Der Würfel wird bewegt
    c=moveCubeX(c,x)
    c=moveCubeY(c,y)
    c=moveCubeZ(c,z)

    # Die Komponenten des Würfels werden nach ihrer Z Achse sotiert, damit sie sich richtig überschneiden
    c=[sortLine(c[0],-1),sortCorner(c[1])]

    # Würfel wird projiziert
    if mode == "c":
        c=projectCentralCube(c,v)
    if mode == "p":
        c=projectParallelCube(c)

    # Alles wird der Reihe nach gemalt
    plotCube(c)

#Beispiel:
#Grundlegende Definitionen
#fig, ax = plt.subplots()
#Entfernung von Rahmen
#fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
#plt.axis('off')
#Axen sind gleichmässig (1 ist auf beiden Axen gleich lang)
#plt.axis('equal')
#Kontrolle der Bildgrösse
#plt.plot([-4,4],[-1.3,-1.3],color='white') 

# Malen
#cube(0,0,0, 0,0,0, 4,"c")
#plt.show()