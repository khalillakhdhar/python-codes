n=int(input("donner la taille du tableau"))
tab=[]
s=0
for i in range(n):
    x=float(input("donner un chiffre"))
    tab.append(x)
    s+=x
moyenne=s/n
print("la moyenne des éléments du tableau est %s et le maximum est %s"%(moyenne, max(tab)))

def Max(tab):
    max=0
    for t in tab:
        if t>max:
            max=t
    return max

        
    