rep=""
dict={}
lst=[]
while rep!="n":
    nom=input("donner un nom: ")
    tel=input("donner un numéro de téléphone: ")
    dict.update({'nom':nom,'tel':tel})
    lst.append(dict)
    rep=input("vous voulez continuer? (n pour quitter)")
print(lst)