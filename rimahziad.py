
def aff(liste, liste2):
    for i in range(0, len(liste)):
        print("'X ^ ", liste[i], "' : ", liste2[i])

liste=[]
liste2=[]
l=[(1,2),(3,2),(0,3)]
for i in range(0,len(l)):
        x=l[i][0]
        y=l[i][1]
        t=1
        for j in range(0,len(liste)):
            if(liste[j]==x):
                    liste2[j]=liste2[j]+x
                    j=len(liste)
                    t=0
        if (t==1):
                        liste.append(x)
                        liste2.append(y)
aff(liste,liste2)
print("______________")