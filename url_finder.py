#This is the Ultimate Pentest tool coded by Arty06

#Imports
import os
import argparse
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import threading

#Clear terminal
os.system('cls||clear')


#=================================================Arguments======================================================
#Création des arguments
if __name__ == "__main__":
    #Description globale du tool
    parser = argparse.ArgumentParser(description="Ultimate Pentest Tool,un couteau suisse python pour le Pentest ;)")

    #es différents Arg
    parser.add_argument("-m", type=int, help="Le mode que vous souhaitez utiliser: 1)Recherche de toutes les URL relatives à un site |2) Endpoint Checker")
    parser.add_argument("-u", type=str, help="L'URL de base que vous souhaitez tester")

    #"Création" des arguments
    args = parser.parse_args()

#================================================================================================================





#==================================================URL dans 1 site (mode = 1)===============================================

if args.m == 1:

    #Déclaration de variables pour Ping les sites
    user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/109.0.0.0 Safari/537.36"]
    user_agent = user_agent[0]
    headers = {'user-Agent':user_agent}
    link_tab = []


    def enumerate_urls(url):
        # Envoi une requête GET à l'URL donnée et récupère le contenu de la page
        page = requests.get(url)
        # Analyse le contenu de la page avec BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')
        # Récupère tous les liens de la page
        links = soup.find_all('a')
        # Boucle sur les liens et affiche les URLs relatives
        print("===========================================================All found URL=================================================")

        #Recherche des sites
        for link in links:
            href = link.get('href')
            if href.startswith('/'):
                print(Fore.BLUE + url + href)
                final_url = url + href
                link_tab.append(final_url)

        print("=================================================================Testing all the URL================================================")



        if len(link_tab) == 0:
            print(Fore.RED + "None URL found")
            quit

        #Boucle pour tester les sites
        for i in range(0,len(link_tab)):
            url_to_test = link_tab[i]
            r = requests.get(url_to_test, headers=headers)
            #print(r)
            #Vérification du status
            if r.status_code == 200:
                print(Fore.GREEN + url_to_test)
            else:
                print(Fore.RED + url_to_test)


        #print(link_tab)

    # Appel de la fonction en passant l'URL d'un site comme argument
    enumerate_urls(args.u)
    #retour à la couleur normal
    print(Fore.WHITE + "")

#========================================================================================================================



#=================================================Mode2: Endpoint Checker=================================================
elif args.m == 2:

    init()
    #Définition des variables
    i = 0
    t = 0
    accept_tab = []

    

    choice = int(input(Fore.CYAN + Style.BRIGHT + "Wich mode would you like to choose ?\n1-Many endpoints on 1 website\n2-1 endpoint on many websites\n"))



    if choice == 1:

#___________________________________________________________________________Mode 1______________________________________________________________________




        #On travail avec le fichier contenannt les endpoint
        list = open('endpoint/list1.txt', 'r+')

        #La variable fichier contient tous les mots
        contenu = list.readlines()
        #Un tableau s'est créé,|0 = première ligne,1 = 2e ligne...

        print(Fore.RED + Style.BRIGHT +"By default, the list of endpoints is a small random list, if you want to modify these values, you just have to modify the `list.txt` file!\n")
            

        #URL à tester
        base_URL = input(Fore.CYAN + Style.BRIGHT + "Wich URL would you like to test ?\n")
        user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/109.0.0.0 Safari/537.36"]
        user_agent = user_agent[0]
        headers = {'user-Agent':user_agent}

        #Boucle pour aller chercher tout les mots + regarder si l'URL existe
        #Pour avor la bonne longueur
        for i in range(0,len(contenu)):
            line = contenu[i]
            line = line.replace("\n","")
            modify_URL = base_URL + line

            
            r = requests.get(modify_URL, headers=headers)
            #print(r)
    #---------------------------------------------Endpoint valide--------------------------------------------------------
            if r.status_code == 200 and modify_URL != base_URL:
                print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")
                print("Trying ",modify_URL)
                print(Fore.GREEN + Style.BRIGHT + "URL tested: ",modify_URL,"\n","Status:", r)

                #Faire la barre de progression
                total = len(contenu)
                percentage = i * 100 / total
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")

                accept_tab.append(modify_URL)
                print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")


    #-----------------------------------------------Endpoint non valide-------------------------------------------------------------------

            else:
                print(Fore.RED + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")
                print(Fore.RED + Style.BRIGHT + "URL tested: ",modify_URL,"\n","Status:", r,"\nNot valid endpoint")
                #Faire la barre de progression
                total = len(contenu)
                percentage = i * 100 / total
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")



                accept_tab.append(modify_URL)
                print(Fore.RED+ Style.BRIGHT + "=======================================================================================================================================================================================\n\n")


        #Fin du scan
        print(Fore.RED + Style.BRIGHT + "SCAN COMPLETED")



        #---------------------------------------------------------------------------------------RECAP-----------------------------------------------------------------------------
        print(Fore.GREEN + Style.BRIGHT + "\n\n==============================================================================================RECAP===========================================================================================\n\n")
        print("The valid endpoints are:\n\n")
        for t in range(0,len(accept_tab)):
            print(Fore.RED + Style.BRIGHT + accept_tab[t],"")

        save = input(Fore.CYAN + Style.BRIGHT + "\n\n\nDo you want to save endpoints to a file? (Note: endpoints will be added, if any already exist in the file, they will be stored in: `endpoints.txt) (y/n)")

        #Nom avec site checked (base URl)

        name = "\n\n========================================================================== " + base_URL + " ==========================================================================\n\n"

        if save == "y":
            with open("endpoint/endpoints_mode1.txt", "a") as file:
                #Délimitation pour l'URL analysée (checked)
                file.write(name) 
                for t in range(0,len(accept_tab)):
                    file.write(accept_tab[t])
                    file.write("\n")
                file.close()
            print(Fore.RED + Style.BRIGHT + "\nThe results have been saved into `endpoints_mode1.txt' !")
            


        #On close le fichier
        list.close()

#__________________________________________________________________________________________________________________________________________________________________________________________________________________



#______________________________________________________________________=Mode 2______________________________________________________________________

    elif choice == 2:
            #On travail avec le fichier contenannt les endpoint
        list = open('endpoint/list2.txt', 'r+')

        #La variable fichier contient tous les mots
        contenu = list.readlines()
        #Un tableau s'est créé,|0 = première ligne,1 = 2e ligne...

        print(Fore.RED + Style.BRIGHT +"By default, the list of endpoints is a small random list, if you want to modify these values, you just have to modify the `list.txt` file!\n")
            

        #URL à tester
        base_endpoint = input(Fore.CYAN + Style.BRIGHT + "Quelle est l'endpoint que vous souhaitez tester ?\n")
        user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/109.0.0.0 Safari/537.36"]
        user_agent = user_agent[0]
        headers = {'user-Agent':user_agent}

        #Boucle pour aller chercher tout les mots + regarder si l'URL existe
        #Pour avor la bonne longueur
        for i in range(0,len(contenu)):
            line = contenu[i]
            line = line.replace("\n","")
            modify_endpoint =  line + base_endpoint

            
            r = requests.get(modify_endpoint, headers=headers)


    #-----------------------------------------------------Endpoint valide------------------------------------------------------

            if r.status_code == 200 and modify_endpoint != base_endpoint:
                print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")
                print("Trying ",modify_endpoint)
                print(Fore.GREEN + Style.BRIGHT + "URL testée: ",modify_endpoint,"\n","Status:", r)

                #Faire la barre de progression
                total = len(contenu)
                percentage = i * 100 / total
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")

                accept_tab.append(modify_endpoint)
                print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")


    #-----------------------------------------------------------Endpoint non valide--------------------------------------------------------------
            else:
                print(Fore.RED + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")
                print("Trying ",modify_endpoint)
                print(Fore.RED + Style.BRIGHT + "URL testée: ",modify_endpoint,"\n","Status:", r,"\nNot valid endpoint")

                #Faire la barre de progression
                total = len(contenu)
                percentage = i * 100 / total
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")

                accept_tab.append(modify_endpoint)
                print(Fore.RED + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")

        print(Fore.RED + Style.BRIGHT + "SCAN COMPLETED")



        #---------------------------------------------------------------------------------------RECAP-----------------------------------------------------------------------------
        print(Fore.GREEN + Style.BRIGHT + "\n\n==============================================================================================RECAP===========================================================================================\n\n")
        print("Les endpoints valides sont les suivants:\n\n")
        for t in range(0,len(accept_tab)):
            print(Fore.RED + Style.BRIGHT + accept_tab[t],"")

        save = input(Fore.CYAN + Style.BRIGHT + "\n\n\nDo you want to save endpoints to a file? (Note: endpoints will be added, if any already exist in the file, they will be stored in: `endpoints.txt) (y/n)")

        #Nom avec site checked (base URl)
        name = "\n\n========================================================================== " + base_endpoint + " ==========================================================================\n\n"

        if save == "y":
            with open("endpoint/endpoints_mode2.txt", "a") as file:
                #Délimitation pour l'URL analysée (checked)
                file.write(name) 
                for t in range(0,len(accept_tab)):
                    file.write(accept_tab[t])
                    file.write("\n")
                file.close()
            print(Fore.RED + Style.BRIGHT + "\nResults have been save into `endpoints_mode2.txt' !")
            


        #On close le fichier
        list.close()

#===========================================================================================================================

#==========================================================Bruteforce endpoint checker (-m 3)=================================================================
elif args.m == 3:

        #On travail avec le fichier contenannt les endpoint
        list = open('endpoint_bruteforce/rockyou.txt', 'r', encoding="UTF-8")

        #La variable fichier contient tous les mots
        contenu = list.readlines()
        #Un tableau s'est créé,|0 = première ligne,1 = 2e ligne...

        print(Fore.RED + Style.BRIGHT +"This mode will try every endpoints possible for the endpoint you gave with the 'rockyou.txt' list\n")
            

        #URL à tester
        base_endpoint = args.u
        user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/109.0.0.0 Safari/537.36"]
        user_agent = user_agent[0]
        headers = {'user-Agent':user_agent}

        #Boucle pour aller chercher tout les mots + regarder si l'URL existe
        #Pour avor la bonne longueur
        for i in range(0,len(contenu)):
            line = contenu[i]
            line = line.replace("\n","")
            modify_endpoint =  base_endpoint + line
            #print(modify_endpoint)
            
            #On fait la request
            r = requests.get(modify_endpoint, headers=headers)

            if r.status_code == 200:
                print(Fore.GREEN + Style.BRIGHT + "=============================================================================================================================================================================\n\n")
                print("Trying ",modify_endpoint)
                print(Fore.GREEN + Style.BRIGHT + "URL testée: ",modify_endpoint,"\n","Status:", r)

                #Faire la barre de progression
                total = len(contenu)
                percentage = i * 100 / total
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")
                accept_tab = []
                accept_tab.append(modify_endpoint)
                print(Fore.GREEN + Style.BRIGHT + "=============================================================================================================================================================================\n\n")

            else:
                print(Fore.RED + Style.BRIGHT + "=============================================================================================================================================================================\n\n")
                print("Trying ",modify_endpoint)
                print(Fore.RED + Style.BRIGHT + "URL testée: ",modify_endpoint,"\n","Status:", r,"\nNot valid endpoint")

                #Faire la barre de progression
                total = len(contenu)
                percentage = i * 100 / total
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")

                accept_tab.append(modify_endpoint)
                print(Fore.RED + Style.BRIGHT + "=============================================================================================================================================================================\n\n")


        print(Fore.RED + Style.BRIGHT + "SCAN COMPLETED")

        #---------------------------------------------------------------------------------------RECAP-----------------------------------------------------------------------------
        print(Fore.GREEN + Style.BRIGHT + "\n\n==============================================================================================RECAP===========================================================================================\n\n")
        print("Les endpoints valides sont les suivants:\n\n")
        for t in range(0,len(accept_tab)):
            print(Fore.RED + Style.BRIGHT + accept_tab[t],"")

#=========================================================================================================================================