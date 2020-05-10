#! python3

import webbrowser, requests, bs4, os

# méthode de d'affichage des traits raciaux
def traits_perso():  
    os.system("cls")
    print("\n\nLa race choisie est : " + race_choisie+ "\n")
    re_info_supp = requests.get(AideDD + url_race[int(choix)])
    re_info_supp.raise_for_status()
    soup_info_supp = bs4.BeautifulSoup(re_info_supp.text, "lxml")
    premier_traits = soup_info_supp.find("article")
    limite = premier_traits.h4
    limite_auteur = premier_traits.find(class_ = "auteur")

    premier_traits = premier_traits.find(string ="Traits")
    premier_traits = premier_traits.next_element
    print(premier_traits.next_element)
    while limite != premier_traits.next_sibling:
        premier_traits = premier_traits.next_sibling
        traits = premier_traits.getText()
        print("\n")
        print(traits)
        if premier_traits.next_sibling == limite_auteur:
            break
#Démarrage

print("Bienvenue dans l'outil d'aide à la création de personnage pour D&D\n")
print("Quelle race voulez-vous jouer?")

# récupération du site
AideDD = "https://www.aidedd.org"
re = requests.get(AideDD)
re.raise_for_status()
soup = bs4.BeautifulSoup(re.text,"lxml")

# Selection et recup de la page de règles
selection = soup.select("li a")[1]
recup = selection.get("href")
page_regles = AideDD + recup
re_regles = requests.get(page_regles)
re_regles.raise_for_status()
soup_regles = bs4.BeautifulSoup(re_regles.text, "lxml")

# Selection et recupération de la page des races
select_regles = soup_regles.select("li > a")[8]
recup_races = select_regles.get("href")
page_races = AideDD + recup_races
re_races = requests.get(page_races)
re_races.raise_for_status()

# positionnement dans l'arbre du site
soup_races = bs4.BeautifulSoup(re_races.text, "lxml")
infos_races = soup_races.find_all("ul")
infos_races = infos_races[1]
infos_races = infos_races.find_all("ul")
infos_races = infos_races[1]
infos_races = infos_races.find_all("a")

# récupération url et nom des races

url_race = [""]* len(infos_races)
nom_race = [""] * len(infos_races)
compteur = 0
for i in infos_races:
    url_race[compteur] = infos_races[compteur].get("href")
    compteur += 1

compteur = 0
test = infos_races
for i in infos_races:
    test1 = test[compteur]
    test1 = test1.find(class_ = "text")
    nom_race[compteur] = test1.get_text()
    compteur += 1

# affichage nom des races
def affichage_races():
    compteur = 0
    for i in nom_race:
        print(str(compteur)+ " : " + i )
        compteur +=1
    print("\nPour plus d'informations sur une race commencez par saisir un ? \n")
    print("""Si vous avez déjà fait votre choix saisissez la valeur associée à la race.
    (ex : 3 pour Nain)""")
affichage_races()
race_choisie = None
while race_choisie == None:
    choix = input()
    if choix == "?":
        print("""Sur quelle race souhaitez vous des renseignements supplémentaires?
    (Veuillez entrer la valeur associée à la race de votre choix.)""")
        choix = input()
        re_info_supp = requests.get(AideDD + url_race[int(choix)])
        re_info_supp.raise_for_status()
        soup_info_supp = bs4.BeautifulSoup(re_info_supp.text, "lxml")
        info_supp_race = soup_info_supp.find(class_ = "content")
        if int(choix) > 8:
            info_supp_race = info_supp_race.find_all("p")
            info_supp_race = info_supp_race[1]
            print("\n" + nom_race[int(choix)])
            print()
            print(info_supp_race.getText())
            print("\nSaisissez un ? pour encore plus d'informations\n")
            print("Saisissez \"b\" pour revenir au menu de sélection des races.")
            choix2 = input()
            if choix2 == "?":
                webbrowser.open(AideDD + url_race[int(choix)])
                print("Voulez-vous jouer cette race? [o = oui | n = non]")
                choix2 = input()
                if choix2 == "o":
                    race_choisie = nom_race[int(choix)]
                elif choix2 == "n":
                    os.system("cls")
                    affichage_races()
                elif choix2 == "b":
                    os.system("cls")
                    affichage_races()
            elif choix2 == "b":
                os.system("cls")
                affichage_races()
        else:
            info_supp_race = info_supp_race.p
            print("\n" +nom_race[int(choix)])
            print()
            print(info_supp_race.getText())
            print("\nSaisissez un ? pour encore plus d'informations\n")
            print("Saisissez \"b\" pour revenir au menu de sélection des races.")
            choix2 = input()
            if choix2 == "?":
                webbrowser.open(AideDD + url_race[int(choix)])
                print("Voulez-vous jouer cette race? [o = oui | n = non]")
                choix2 = input()
                if choix2 == "o":
                    race_choisie = nom_race[int(choix)]
                elif choix2 == "n":
                    os.system("cls")
                    affichage_races()
                elif choix2 == "b":
                    os.system("cls")
                    affichage_races()
                
            elif choix2 == "b":
                os.system("cls")
                affichage_races()
    else:
        race_choisie = nom_race[int(choix)]
        
traits_perso()

print("\n\n\nAppuyer sur une touche pour passer à la suite.")
input()
os.system("cls")
print("\nVeuillez choisir votre classe :")

# Selection et recupération de la page des classes
select_regles = soup_regles.select("li > a")[9]
recup_classe = select_regles.get("href")
page_classe = AideDD + recup_classe
re_classe = requests.get(page_classe)
re_classe.raise_for_status()

#positionnement dans l'abre
soup_classe = bs4.BeautifulSoup(re_classe.text, "lxml")
infos_classes = soup_classe.find_all("ul")
infos_classes = infos_classes[1]
infos_classes = infos_classes.find_all("ul")
infos_classes = infos_classes[2]
infos_classes = infos_classes.find_all("a")

# récupération des noms et URL de classe
url_classe = [""]* len(infos_classes)
nom_classe = [""] * len(infos_classes)
compteur = 0
for i in infos_classes:
    url_classe[compteur] = infos_classes[compteur].get("href")
    compteur += 1

compteur = 0
for i in infos_classes:
    test1 = infos_classes[compteur]
    test1 = test1.find(class_ = "text")
    nom_classe[compteur] = test1.get_text()
    compteur += 1

# affichage des classes

def affichage_classes():
    compteur = 0
    print(("Vous etes un "+ str(race_choisie)).rjust(80))
    for i in nom_classe:
        print(str(compteur)+ " : " + i )
        compteur +=1
    print("\nPour plus d'informations sur une classe commencez par saisir un ? \n")
    print("""Si vous avez déjà fait votre choix saisissez la valeur associée à la classe.
    (ex : 3 pour Druide)""")
affichage_classes()
classe_choisie = None
while classe_choisie == None:
    choix = input()
    if choix == "?":
        print("""Sur quelle classe souhaitez vous des renseignements supplémentaires?
    (Veuillez entrer la valeur associée à la classe de votre choix.)""")
        choix = input()
        re_info_supp = requests.get(AideDD + url_classe[int(choix)])
        re_info_supp.raise_for_status()
        soup_info_supp = bs4.BeautifulSoup(re_info_supp.text, "lxml")
        info_supp_classe = soup_info_supp.find(class_ = "content")
        info_supp_classe = info_supp_classe.p
        print("\n" +nom_classe[int(choix)])
        print()
        print(info_supp_classe.getText())
        print("\nSaisissez un ? pour encore plus d'informations\n")
        print("Saisissez \"b\" pour revenir au menu de sélection des classes.")
        choix2 = input()
        if choix2 == "?":
            webbrowser.open(AideDD + url_classe[int(choix)])
            print("Voulez-vous jouer cette classe? [o = oui | n = non]")
            choix2 = input()
            if choix2 == "o":
                classe_choisie = nom_classe[int(choix)]
            elif choix2 == "n":
                os.system("cls")
                affichage_classes()
            elif choix2 == "b":
                os.system("cls")
                affichage_classes()
            
        elif choix2 == "b":
            os.system("cls")
            affichage_classes()
    else:
        classe_choisie = nom_classe[int(choix)]

os.system("cls")
print("Vous etes un : " + str(race_choisie) +" "+ str(classe_choisie))
print("\nVeuillez choisir votre historique.")

# Selection et recupération de la page des historique
select_regles = soup_regles.select("li > a")[10]
recup_infos_historique = select_regles.get("href")
page_infos_historique = AideDD + recup_infos_historique
re_infos_historique = requests.get(page_infos_historique)
re_infos_historique.raise_for_status()


# positionnement dans l'arbre du site
soup_historique = bs4.BeautifulSoup(re_infos_historique.text, "lxml")
infos_historique = soup_historique.find_all("ul")
infos_historique = infos_historique[1]
infos_historique = infos_historique.find_all("ul")
infos_historique = infos_historique[3]
infos_historique = infos_historique.find_all("a")


# récupération url et nom des historique

url_historique = [""]* len(infos_historique)
nom_historique = [""] * len(infos_historique)
compteur = 0
for i in infos_historique:
    url_historique[compteur] = infos_historique[compteur].get("href")
    compteur += 1

compteur = 0
test = infos_historique
for i in infos_historique:
    test1 = test[compteur]
    test1 = test1.find(class_ = "text")
    nom_historique[compteur] = test1.get_text()
    compteur += 1

# affichage des historique

def affichage_historique():
    compteur = 0
    print(("Vous etes un "+ str(race_choisie)+" "+ str(classe_choisie)).rjust(80))
    for i in nom_historique:
        print(str(compteur)+ " : " + i )
        compteur +=1
    print("\nPour plus d'informations sur une historique commencez par saisir un ? \n")
    print("""Si vous avez déjà fait votre choix saisissez la valeur associée à la historique.
    (ex : 3 pour Charlatan)""")
affichage_historique()
historique_choisie = None
while historique_choisie == None:
    choix = input()
    if choix == "?":
        print("""Sur quelle historique souhaitez vous des renseignements supplémentaires?
    (Veuillez entrer la valeur associée à la historique de votre choix.)""")
        choix = input()
        re_info_supp = requests.get(AideDD + url_historique[int(choix)])
        re_info_supp.raise_for_status()
        soup_info_supp = bs4.BeautifulSoup(re_info_supp.text, "lxml")
        info_supp_historique = soup_info_supp.find(class_ = "content")
        if int(choix) > 12:
            info_supp_historique = info_supp_historique.find_all("p")
            info_supp_historique = info_supp_historique[1]
            print("\n" + nom_historique[int(choix)])
            print()
            print(info_supp_historique.getText())
            print("\nSaisissez un ? pour encore plus d'informations\n")
            print("Saisissez \"b\" pour revenir au menu de sélection des historique.")
            choix2 = input()
            if choix2 == "?":
                webbrowser.open(AideDD + url_historique[int(choix)])
                print("Voulez-vous jouer cette historique? [o = oui | n = non]")
                choix2 = input()
                if choix2 == "o":
                    historique_choisie = nom_historique[int(choix)]
                elif choix2 == "n":
                    os.system("cls")
                    affichage_historique()
                elif choix2 == "b":
                    os.system("cls")
                    affichage_historique()
            elif choix2 == "b":
                os.system("cls")
                affichage_historique()
        else:
            info_supp_historique = info_supp_historique.p
            print("\n" +nom_historique[int(choix)])
            print()
            print(info_supp_historique.getText())
            print("\nSaisissez un ? pour encore plus d'informations\n")
            print("Saisissez \"b\" pour revenir au menu de sélection des historique.")
            choix2 = input()
            if choix2 == "?":
                webbrowser.open(AideDD + url_historique[int(choix)])
                print("Voulez-vous jouer cette historique? [o = oui | n = non]")
                choix2 = input()
                if choix2 == "o":
                    historique_choisie = nom_historique[int(choix)]
                elif choix2 == "n":
                    os.system("cls")
                    affichage_historique()
                elif choix2 == "b":
                    os.system("cls")
                    affichage_historique()
                
            elif choix2 == "b":
                os.system("cls")
                affichage_historique()
    else:
        historique_choisie = nom_historique[int(choix)]
print("""Vous devez désormais choisir des traits de caractères, un idéal, un lien ainsi qu'un défaut à votre
personnage. Pour cela je dois encore reflechir à comment je m'y prends""")
      
print("Vous etes un : " + str(race_choisie) +" "+ str(classe_choisie) + " au passé de " + str(historique_choisie))
os.system("pause")
