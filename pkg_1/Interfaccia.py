from pkg_1.Championship import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

### FUNZIONI UTILI PER L'INTERFACCIA ###
def menuChoice():
    valid = ['1','10',]
    userChoice = str(input("Inserisci il numero dell'operazione che vuoi effettuare: "))
    if userChoice in valid:
        inputCheck(userChoice)
        menuChoice()
    else:
        print('Siamo spiacenti, questa operazione non è tra quelle elencate... La preghiamo di riprovare.')
        menuChoice()


def inputCheck(userChoice):
    if userChoice == '1':
        text = str(input("Inserisci Codice Campionato: "))
        try:
            camp = Championship(text)
            print("Numero Squadre", len(camp.teams))
            print(camp.teams)
        except Exception as e:
            print(
                bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + text + bcolors.FAIL + " non è nel nostro database...")
            print("Ricontrolla il codice del campionato inserito" + bcolors.ENDC)

    if userChoice == '10':
        print("Ti ringraziamo per aver usufruito del nostro servizio.\nTorna a trovarci.\n")
        exit()



### INTERFACCIA ###
print("*** Benvenuto nel nostro Centro Scommesse ***\n")
print("Operazioni possibili: ")
print("1) Dato un campionato, stampare l’elenco delle squadre del campionato.\n"
      "2) Dati una giornata e un campionato, stampare la classifica per la giornata indicata e per ogni squadra il"
      "numero di partite giocate.\n"
      "3) Dati una giornata e un campionato, stampare la classifica per la giornata indicata considerando i risultati"
      "che si riferiscono al primo tempo e per ogni squadra il numero di partite giocate.\n"
      "4) Date una giornata e una squadra, stampare gli ultimi cinque risultati per la squadra indicata.\n"
      "5) Dato un giorno, stampare i risultati di tutte le eventuali partite giocate il giorno indicato.\n"
      "6) Dati una giornata e un intero k, stampare le k squadre tra tutti i campionati che hanno segnato più goal.\n"
      "7) Dati una giornata e un intero k, stampare le k squadre tra tutti i campionati che hanno subito meno goal.\n"
      "8) Dati una giornata e un intero k, stampare le k squadre tra tutti i campionati con la migliore differenza"
      "reti.\n"
      "9) Dati una giornata e un campionato, stampare la squadra tra tutti i campionati con il maggior numero di"
      "vittorie, la squadra con il maggior numero di vittorie in casa, la squadra con il maggior numero di vittorie in"
      "trasferta.\n"
      "10) Uscire dall'applicazione del Centro Scommesse.\n")
menuChoice()
