#Dieses Programm erzeugt eine Funktion mit der die Parallelprojektion eines Quadrates gezeichnet werden kann
#Diese Funktion kann in andere Programme importiert werden

#Importierung der Erweiterungen
import numpy as np
import matplotlib.pyplot as plt

#Definition des Quadrates mit Farben
square=[[[[1,1],[1,-1],'tab:blue'],[[1,-1],[-1,-1],'tab:orange'],[[-1,-1],[-1,1],'tab:green'],[[-1,1],[1,1],'tab:red']],
        [[[1,1],'tab:blue'],[[1,-1],'tab:orange'],[[-1,-1],'tab:green'],[[-1,1],'tab:red'] ]]

#Funktionen der Rotation
def rotatePoint(p,a):
    #Rotationsmatrix
    m=np.matrix([[np.cos(a),(-1)*np.sin(a)],
                 [np.sin(a),np.cos(a)]])
    return(list(np.asarray(m.dot(p)).flatten()))
def rotateLine(l,a):
    return([rotatePoint(l[0],a),rotatePoint(l[1],a),l[2]])
def rotateCorner(c,a):
    return([rotatePoint(c[0],a),c[1]])
def rotateSquare(t,a):
    d=[list(map(rotateLine,t[0],np.full(4,a))), list(map(rotateCorner,t[1],np.full(4,a)))] 
    return(d)

#Funktionen zum Zeichnen
def plotLine(l,frame):
    frame.plot([l[0][0],l[1][0]],[l[0][1],l[1][1]],color=l[2],linewidth=3)
def plotCorner(c,frame):
    frame.plot(c[0][0],c[0][1],color=c[1],marker='o')
def plotSquare(s,frame):
    [plotLine(x,frame)for x in s[0]]
    [plotCorner(y,frame)for y in s[1]]

#Sortieren der Linien und Punkte
def sortLine(x):
    s=[]
    y=[]
    for i in range(len(x)):
        s.append(((x[i][0][1])+(x[i][1][1]))/2)
    for i in range(len(x)):
        a=np.argmax(s)
        s[a]=-1000
        y.append(x[a]) 
    return (y)
def sortCorner(x):
    s=[]
    y=[]
    for i in range(len(x)):
        s.append(x[i][0][1])
    for i in range(len(x)):
        a=np.argmax(s)
        s[a]=-1000
        y.append(x[a]) 
    return (y)

#Funktionen fürs Projizieren
def projectParallelPoint(p) :
    b=[p[1],p[0]]
    return(b)
def projectParallelLine(l) :
    k=[projectParallelPoint(l[0]),projectParallelPoint(l[1]),l[2]]
    return(k)
def projectParallelCorner(c):
    d=[projectParallelPoint(c[0]),c[1]]
    return(d)
def projectParallelSquare(s) :
    z=[list(map(projectParallelLine,s[0])),list(map(projectParallelCorner,s[1]))]
    return(z)

#Erstellung + Zeichen der Leinwand + Abbild
def canvas(s,c,frame):
    #Leinwand zeichnen
    frame.plot([-c,-c],[2,-2],color='gray')
    #Quadrat Projizieren
    s=projectParallelSquare(s)
    #Die Komponenten des Würfels werden nach ihrer Z Achse sotiert damit das Leinwandbild richtig angefertigt wird. 
    #Damit die forderen die hinteren Ecken überdecken
    s=[sortLine(s[0]),sortCorner(s[1])]
    #Malen der Linien und Ecken
    for x in range(4):
        frame.plot([-c,-c],[s[0][x][0][0],s[0][x][1][0]],color=s[0][x][2],linewidth=2)
    for x in range(4):
        frame.plot([-c,s[0][x][0][1]],[s[0][x][0][0],s[0][x][0][0]],color=s[0][x][2],linewidth=1,linestyle='--')
        frame.plot(-c,s[0][x][0][0],color=s[0][x][2],marker='o',markersize=7)

#Funktion zur Zeichnung des ganzen Bildes
def projection(angle, #Winkel der Rotation
               canvasDistance,#Abstand der Leinwadn
               frame): #Auswahl des Bildes in das gezeichnet werden soll
    #Quadrat Rotieren
    s=rotateSquare(square,(np.pi)*angle/180)
    #Quadrat zeichnen
    plotSquare(s,frame)
    #Leinwand + Projektionn erstellen + Zeichnen
    canvas(s,canvasDistance,frame)
    
#Beispiel:
#Grundlegendes Bild erstellen
#fig, ax = plt.subplots()
#Entfernung von Rahmen
#fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
#plt.axis('off')
#Axen sind gleichmässig (1 ist auf beiden Axen gleich lang)
#plt.axis('equal')
#projection(30,3,ax)
#plt.show()