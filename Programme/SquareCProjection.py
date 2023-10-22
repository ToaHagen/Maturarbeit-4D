#Dieses Programm erzeugt eine Funktion mit der die Zentralprojektion eines Quadrates gezeichnet werden kann
#Diese Funktion kann in andere Programme importiert werden

#Importierung der Funktionen
import numpy as np
import matplotlib.pyplot as plt

#Definition des Quadrates
square=[[[[1,1],[1,-1],'tab:blue'],[[1,-1],[-1,-1],'tab:orange'],[[-1,-1],[-1,1],'tab:green'],[[-1,1],[1,1],'tab:red']],
        [[[1,1],'tab:blue'],[[1,-1],'tab:orange'],[[-1,-1],'tab:green'],[[-1,1],'tab:red'] ]]

#Funktionen für die Rotation
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

#Funktione für die Zeichnung
def plotLine(l,frame):
    frame.plot([l[0][0],l[1][0]],[l[0][1],l[1][1]],color=l[2],linewidth=3)
def plotCorner(c,frame):
    frame.plot(c[0][0],c[0][1],color=c[1],marker='o')
def plotSquare(s,frame):
    [plotLine(x,frame)for x in s[0]]
    [plotCorner(y,frame)for y in s[1]]

#Sortieren der Linien + Ecken
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

#Funktione für die Zentralprojektion
def projectCentralPoint(p,v,c) :
    b=[p[1]*(v-c)/(v-p[0]),#Formel
       p[0]]
    return(b)
def projectCentralLine(l,v,c) :
    k=[projectCentralPoint(l[0],v,c),projectCentralPoint(l[1],v,c),l[2]]
    return(k)
def projectCentralCorner(e,v,c):
    d=[projectCentralPoint(e[0],v,c),e[1]]
    return(d)
def projectCentralSquare(s,v,c) :
    z=[list(map(projectCentralLine,s[0],np.full(4,v),np.full(4,c))),
       list(map(projectCentralCorner,s[1],np.full(4,v),np.full(4,c)))]
    return(z)

#Erstellung und Zeichnung der Leinwand
def canvas(s,v,c,frame):
    #Leinwand zeichnen
    frame.plot([c,c],[1.5,-1.5],color='gray')
    #Quadrat projizieren
    t=projectCentralSquare(s,v,c)
    #Die Komponenten des Quadrates werden nach ihrer Z Achse sotiert damit das Leinwandbild richtig angefertigt wird
    t=[sortLine(t[0]),sortCorner(t[1])]
    #Malen
    for x in range(4):
        frame.plot([c,c],[t[0][x][0][0],t[0][x][1][0]],color=t[0][x][2],linewidth=2)
    for x in range(4):
        frame.plot([v,s[1][x][0][0]],[0,s[1][x][0][1]],color=s[1][x][1],linewidth=1,linestyle='--')
        frame.plot(c,t[0][x][0][0],color=t[0][x][2],marker='o',markersize=7)
    frame.plot(v,0,marker='o',color='black')

#Funktion für die Erstellung des Bildes
def projection(angle,           #Winkel
               canvasDistance,  #Abstand der Leinwand
               viewDistance,    #Abstand des Beobachtungspunktes
               frame):          #Auswahl des Bildes in das gezeichnet werden soll
    #Quadrat rotieren
    s=rotateSquare(square,(np.pi)*angle/180)
    #Leinwand und Abbild zeichnen
    canvas(s,viewDistance,canvasDistance,frame)
    #Quadrat zeichnen
    plotSquare(s,frame)

#Beispiel:
#Grundlegende Definition
#fig, ax = plt.subplots()
#Entfernung von Rahmen
#fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
#plt.axis('off')
#Axen sind gleichmässig (1 ist auf beiden Axen gleich lang)
#plt.axis('equal')
#Aufruf der Funktion für das Bild
#projection(30,-2,-3,ax)
#plt.show()