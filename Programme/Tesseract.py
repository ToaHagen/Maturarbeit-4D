#Mit diesem Programm wird eine Funktion erstellt, mit der ein Tesserakt abgbildet, gedreht und bewegt werden kann.

#Importierung der Bibliotheken
import numpy as np
import matplotlib.pyplot as plt

#Funktion zur Erzeugung eines Tesseraktes
def getRawTesseract():
    tesseract=[]
    for a in range(32):
        tesseract.append([])
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    tesseract[x*4+y*2+z].append([(-1)**x,(-1)**y,(-1)**z,(-1)**w])
                    tesseract[x*4+y*2+w+8].append([(-1)**x,(-1)**y,(-1)**z,(-1)**w])
                    tesseract[x*4+z*2+w+16].append([(-1)**x,(-1)**y,(-1)**z,(-1)**w])
                    tesseract[y*4+z*2+w+24].append([(-1)**x,(-1)**y,(-1)**z,(-1)**w])
    return(tesseract)

#Einfärbung des Tesseraktes
def getTesseract():
    tesseract=getRawTesseract()
    for b in range(32):
        if tesseract[b][0][3]==1 and tesseract[b][1][3]==1:
            tesseract[b].append('tab:blue')
        if tesseract[b][0][3]==-1 and tesseract[b][1][3]==-1:
            tesseract[b].append('tab:green')
        if tesseract[b][0][3] != tesseract[b][1][3]:
            tesseract[b].append('tab:orange')
    return(tesseract)

#Funktion für xy-Rotation
def rotatePointXY(p,a):
    #Rotationsmatrix
    m=np.matrix([[np.cos(a),(-1)*np.sin(a), 0,0],
                 [np.sin(a),np.cos(a),      0,0],
                 [0,        0,              1,0],
                 [0,        0,              0,1]])
    return(list(np.asarray(m.dot(p)).flatten()))
def rotateLineXY(l,a):
    return([rotatePointXY(l[0],a),rotatePointXY(l[1],a),l[2]])
def rotateTesseractXY(t,a):
    d=map(rotateLineXY,t,np.full((32),a))
    return(list(d))

#Rotation XZ
def rotatePointXZ(p,a):
    m=np.matrix([[np.cos(a),0,(-1)*np.sin(a),   0],
                 [0,        1,0,                0],
                 [np.sin(a),0,np.cos(a),        0],
                 [0,        0,0,                1]])
    return(list(np.asarray(m.dot(p)).flatten()))
def rotateLineXZ(l,a):
    return([rotatePointXZ(l[0],a),rotatePointXZ(l[1],a),l[2]])
def rotateTesseractXZ(t,a):
    d=map(rotateLineXZ,t,np.full((32),a))
    return(list(d))

#Rotation YZ
def rotatePointYZ(p,a):
    m=np.matrix([[1,0,          0,              0],
                 [0,np.cos(a),  (-1)*np.sin(a), 0],
                 [0,np.sin(a),  np.cos(a),      0],
                 [0,0,          0,              1]])
    return(list(np.asarray(m.dot(p)).flatten()))
def rotateLineYZ(l,a):
    return([rotatePointYZ(l[0],a),rotatePointYZ(l[1],a),l[2]])
def rotateTesseractYZ(t,a):
    d=map(rotateLineYZ,t,np.full((32),a))
    return(list(d))

#Rotation XW
def rotatePointXW(p,a):
    m=np.matrix([[np.cos(a),0,0,(-1)*np.sin(a)],
                 [0,        1,0,0             ],
                 [0,        0,1,0             ],
                 [np.sin(a),0,0,np.cos(a)     ]])
    return(list(np.asarray(m.dot(p)).flatten()))
def rotateLineXW(l,a):
    return([rotatePointXW(l[0],a),rotatePointXW(l[1],a),l[2]])
def rotateTesseractXW(t,a):
    d=map(rotateLineXW,t,np.full((32),a))
    return(list(d))

#Rotation YW
def rotatePointYW(p,a):
    m=np.matrix([[1,0,          0,0             ],
                 [0,np.cos(a),  0,(-1)*np.sin(a)],
                 [0,0,          1,0             ],
                 [0,np.sin(a),  0,np.cos(a)     ]])
    return(list(np.asarray(m.dot(p)).flatten()))
def rotateLineYW(l,a):
    return([rotatePointYW(l[0],a),rotatePointYW(l[1],a),l[2]])
def rotateTesseractYW(t,a):
    d=map(rotateLineYW,t,np.full((32),a))
    return(list(d))

#Rotation ZW
def rotatePointZW(p,a):
    m=np.matrix([[1,0,0,        0             ],
                 [0,1,0,        0             ],
                 [0,0,np.cos(a),(-1)*np.sin(a)],
                 [0,0,np.sin(a),np.cos(a)     ]])
    return(list(np.asarray(m.dot(p)).flatten()))
def rotateLineZW(l,a):
    return([rotatePointZW(l[0],a),rotatePointZW(l[1],a),l[2]])
def rotateTesseractZW(t,a):
    d=map(rotateLineZW,t,np.full((32),a))
    return(list(d))

#Funktion für die Translation in X-Dimension
def movePointX(p,d):
    return([p[0]+d,p[1],p[2],p[3]])
def moveLineX(l,d):
    return([movePointX(l[0],d),movePointX(l[1],d),l[2]])
def moveTesseractX(t,d):
    return(map(moveLineX,t,np.full((32),d)))

#Translation Y
def movePointY(p,d):
    return([p[0],p[1]+d,p[2],p[3]])
def moveLineY(l,d):
    return([movePointY(l[0],d),movePointY(l[1],d),l[2]])
def moveTesseractY(t,d):
    return(map(moveLineY,t,np.full((32),d)))

#Translation Z
def movePointZ(p,d):
    return([p[0],p[1],p[2]+d,p[3]])
def moveLineZ(l,d):
    return([movePointZ(l[0],d),movePointZ(l[1],d),l[2]])
def moveTesseractZ(t,d):
    return(map(moveLineZ,t,np.full((32),d)))

#Translation W
def movePointW(p,d):
    return([p[0],p[1],p[2],p[3]+d])
def moveLineW(l,d):
    return([movePointW(l[0],d),movePointW(l[1],d),l[2]])
def moveTesseractW(t,d):
    return(map(moveLineW,t,np.full((32),d)))

#Zentralprojektion 4D zu 3D
def projectCentralPoint4DTo3D(p,v) :
    b=[p[0]*v/(v-p[3]),p[1]*v/(v-p[3]),p[2]*v/(v-p[3]),p[3]]
    return(b)
def projectCentralLine4DTo3D(l,v) :
    k=[projectCentralPoint4DTo3D(l[0],v), projectCentralPoint4DTo3D(l[1],v),l[2]]
    return(k)
def projectCentralTesseract4DTo3D(t,v) :
    d=map(projectCentralLine4DTo3D,t,np.full((32),v))
    return(list(d))

#Parallelprojetkion 4D zu 3D
def projectParallelPoint4DTo3D(p) :
    b=[p[0],p[1],p[2],p[3]]
    return(b)
def projectParallelLine4DTo3D(l) :
    k=[projectParallelPoint4DTo3D(l[0]), projectParallelPoint4DTo3D(l[1]),l[2]]
    return(k)
def projectParallelTesseract4DTo3D(t) :
    d=map(projectParallelLine4DTo3D,t)
    return(list(d))

#Zentralprojektion 3D zu 2D
def projectCentralPoint3DTo2D(p,v) :
    b=[p[0]*v/(v-p[2]),p[1]*v/(v-p[2]),p[3]]
    return(b)
def projectCentralLine3DTo2D(l,v) :
    k=[projectCentralPoint3DTo2D(l[0],v), projectCentralPoint3DTo2D(l[1],v),l[2]]
    return(k)
def projectCentralTesseract3DTo2D(t,v) :
    d=map(projectCentralLine3DTo2D,t,np.full((32),v))
    return(list(d))

#Zentralprojektion 3D zu 2D
def projectParallelPoint3DTo2D(p) :
    b=[p[0],p[1],p[3]]
    return(b)
def projectParallelLine3DTo2D(l) :
    k=[projectParallelPoint3DTo2D(l[0]), projectParallelPoint3DTo2D(l[1]),l[2]]
    return(k)
def projectParallelTesseract3DTo2D(t) :
    d=map(projectParallelLine3DTo2D,t)
    return(list(d))

#Linien und sortieren für Überscheneidungen
def sort(x):
    s=[]
    y=[]
    for i in range(len(x)):
        s.append(((x[i][0][2]+(x[i][1][2]))/2))
    for i in range(len(x)):
        a=np.argmin(s)
        s[a]=1000
        y.append(x[a]) 
    return (y)

# Funktion zum zeichenen
def plotLine(l,frame):
    frame.plot([l[0][0],l[1][0]],[l[0][1],l[1][1]],marker='',color=l[2], linewidth=4)

#Funktion für das Abbilden des Tesserakts
def tesseract(x,    #Translation x
              y,    #Translation y
              z,    #Translation z
              w,    #Translation w
              xy,   #Rotation xy
              xz,   #Rotation xz
              yz,   #Rotation yz
              xw,   #Rotation xw
              yw,   #Rotation yw
              zw,   #Rotation zw
              firstDistance,    #Abstand des Beobachtungspunktes bei der ersten Projektion 4D zu 3D
              secondDistance,   #Abstand des Beobachtungspunktes bei der zweiten Projektion 4D zu 3D
              mode,             #Art der Projektionen: c:Zentralprojektion, p:Parallelprojektion (z.B: cp, Zentralprojektion-Parallelprojektion)
              frame,            #Grundlegende Bild in dem gemahlt wird
              t=getTesseract()):#Standarttesserakt kann ausgetauscht werden

    #Rotationen mit W-Dimension
    t=rotateTesseractXW(t,np.pi*xw/180)
    t=rotateTesseractYW(t,np.pi*yw/180)
    t=rotateTesseractZW(t,np.pi*zw/180)

    #Rotationen ohne W-Dimension
    t=rotateTesseractXY(t,np.pi*xy/180)
    t=rotateTesseractXZ(t,np.pi*xz/180)
    t=rotateTesseractYZ(t,np.pi*yz/180)

    #Translationen
    t=moveTesseractX(t,x)
    t=moveTesseractY(t,y)
    t=moveTesseractZ(t,z)
    t=moveTesseractW(t,w)

    #Projektion 4D zu 3D
    if mode == "cp" or mode == "cc": 
        t=projectCentralTesseract4DTo3D(t,firstDistance)
    if mode == "pp" or mode == "pc": 
        t=projectParallelTesseract4DTo3D(t)

    #Sortieren nach z-Achse, für richtige Überschneidungen
    t=sort(t)

    #Projektion 3D zu 2D
    if mode == "cc" or mode == "pc": 
        t=projectCentralTesseract3DTo2D(t,secondDistance)
    if mode == "cp" or mode == "pp":
        t=projectParallelTesseract3DTo2D(t)

    #Malen des Tesserakts
    [plotLine(x,frame)for x in t]

#Beispiel:
#Grundlegende Definitionen
#fig, ax = plt.subplots()
#Entfernung von Rahmen
#fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
#plt.axis('off')
#Axen sind gleichmässig (1 ist auf beiden Axen gleich lang)
#plt.axis('equal')

#Zeichnen des Tesserakts
#tesseract(0,0,0,0,20,250,0,0,0,0,4,8,"cp",ax)
#plt.show()