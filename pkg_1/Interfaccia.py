from pkg_1.Championship import *
import threading
import time
import sys

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
def menuChoice(data):
    valid = ['1', '2', '3', '4', '5', '6', '7','8','9','10','debug']
    userChoice = str(input(bcolors.OKBLUE+bcolors.BOLD+"\nInserisci il numero dell'operazione che vuoi effettuare: " + bcolors.ENDC))
    if userChoice in valid:
        inputCheck(userChoice,data)
        menuChoice(data)
    else:
        print(bcolors.FAIL+bcolors.BOLD+'Siamo spiacenti, questa operazione non è tra quelle elencate... La preghiamo di riprovare.'+bcolors.ENDC)
        print("\nOperazioni disponibili: ")
        print("1) Dato un campionato, stampare l’elenco delle squadre del campionato.\n"
              "2) Dati una giornata e un campionato, stampare la classifica per la giornata indicata e per ogni squadra"
                " il numero di partite giocate.\n"
              "3) Dati una giornata e un campionato, stampare la classifica per la giornata indicata considerando i risultati"
              " che si riferiscono al primo tempo e per ogni squadra il numero di partite giocate.\n"
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
        menuChoice(data)


def inputCheck(userChoice ,data):
    if userChoice == '1':
        print(bcolors.OKBLUE+bcolors.BOLD+"Hai scelto l'opzione 1: ")
        print("Dato un campionato, stampare l’elenco delle squadre del campionato."+ bcolors.ENDC)
        print("Campionati: E0, SC0, D1, SP1, I1, F1, N1, B1, P1, T1, G1")
        text = str(input(bcolors.OKBLUE+bcolors.BOLD+"\nInserisci Codice Campionato: "+ bcolors.ENDC))
        text = text.upper()
        try:
            camp = data[text]
            print("Numero Squadre: ", len(camp.teams))
            print(camp.teams)
        except Exception as e:
            print(bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + text + bcolors.FAIL + " non è nel nostro database...")
            print("Ricontrolla il codice del campionato inserito" + bcolors.ENDC)

    if userChoice == '2':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 2: ")
        print("Dati una giornata e un campionato, stampare la classifica per la giornata indicata e per ogni squadra il"
                " numero di partite giocate." + bcolors.ENDC)
        print("Campionati: E0, SC0, D1, SP1, I1, F1, N1, B1, P1, T1, G1")
        text = str(input(bcolors.OKBLUE + bcolors.BOLD + "\nInserisci Codice Campionato: " + bcolors.ENDC))
        text = text.upper()
        try:
            camp = data[text]
            print("Numero Squadre: ", len(camp.teams))
            if text == "SC0":  # caso particolare
                print("Numero giornate: ", 38)
            print("Numero giornate: ", len(camp.teams) * 2 - 2)
        except Exception as e:
            print(
                bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + text + bcolors.FAIL + " non è nel nostro database...")
            print("Ricontrolla il codice del campionato inserito" + bcolors.ENDC)
        try:
            text2 = int(input(bcolors.OKBLUE + bcolors.BOLD + "Inserisci Giornata: " + bcolors.ENDC))
            if text2 <= (len(camp.teams) * 2 - 2) or (text == "SC0" and text2 <= 38):
                print("Classifica")
                print("Teams | PG | Pti ")
                rank = camp.get_rankingday(text2, 2)
                i = 0
                for team in rank:
                    i += 1
                    print(i, team[0], team[1], team[2])
            else:
                raise Exception()
        except Exception as ex:
            print(bcolors.FAIL + "La giornata " + bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + str(
                text2) + bcolors.FAIL + " non appartiene al campionato "
                  + bcolors.FAIL + text + bcolors.FAIL)
            print("Ricontrolla il numero delle giornate prima di riprovare." + bcolors.ENDC)

    if userChoice == '3':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 3: ")
        print("Dati una giornata e un campionato, stampare la classifica per la giornata indicata considerando i risultati"
              " che si riferiscono al primo tempo e per ogni squadra il numero di partite giocate." + bcolors.ENDC)
        print("Campionati: E0, SC0, D1, SP1, I1, F1, N1, B1, P1, T1, G1")
        text = str(input(bcolors.OKBLUE+bcolors.BOLD+"\nInserisci Codice Campionato: "+ bcolors.ENDC))
        text = text.upper()
        try:
            camp = data[text]
            print("Numero Squadre: ", len(camp.teams))
            if text == "SC0":  # caso particolare
                print("Numero giornate: ", 38)
            print("Numero giornate: ", len(camp.teams) * 2 - 2)
        except Exception as e:
            print(bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + text + bcolors.FAIL + " non è nel nostro database...")
            print("Ricontrolla il codice del campionato inserito" + bcolors.ENDC)
        try:
            text2 = int(input(bcolors.OKBLUE + bcolors.BOLD + "Inserisci Giornata: " + bcolors.ENDC))
            if text2 <= (len(camp.teams) * 2 - 2) or (text == "SC0" and text2 <= 38):
                print("Classifica basata sui risultati del primo tempo")
                print("Teams | PG | Pti ")
                i = 0
                for team in camp.get_partialrankingday(text2):
                    i += 1
                    print(i, team[0], team[1], team[2])
            else:
                raise Exception()
        except Exception as e:
            print(bcolors.FAIL + "La giornata " + bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + str(
                text2) + bcolors.FAIL + " non appartiene al campionato "
                  + bcolors.FAIL + text + bcolors.FAIL)
            print("Ricontrolla il numero delle giornate prima di riprovare." + bcolors.ENDC)

    if userChoice == '4':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 4: ")
        print("Date una giornata e una squadra, stampare gli ultimi cinque risultati per la squadra indicata."
              + bcolors.ENDC)
        print("Campionati: E0, SC0, D1, SP1, I1, F1, N1, B1, P1, T1, G1")
        text = str(input(bcolors.OKBLUE+bcolors.BOLD+"\nInserisci Codice Campionato: "+ bcolors.ENDC))
        text = text.upper()
        text2 = int(input(bcolors.OKBLUE+bcolors.BOLD+"Inserisci Giornata: "+ bcolors.ENDC))
        text3 = str(input(bcolors.OKBLUE + bcolors.BOLD + "Inserisci Squadra: " + bcolors.ENDC))
        team = text3.capitalize()
        try:
            camp = data[text]
            print("Last 5 matches to day",text2)
            history = camp.get_historyTeam(text2, team)
            print(team, end= " ")
            for elem in history:
                if elem == 'W':
                    print(bcolors.OKGREEN+elem, end=" ")
                elif elem =='A':
                    print(bcolors.FAIL+elem, end=" ")
                elif elem == 'D':
                    print(bcolors.ENDC+elem, end=" ")
        except Exception as e:
            print(e, e.with_traceback(tb=None))
            print(bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + text + bcolors.FAIL + " non è nel nostro database...")
            print("Ricontrolla il codice del campionato inserito" + bcolors.ENDC)

    if userChoice == '5':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 5: ")
        print("Dato un giorno, stampare i risultati di tutte le eventuali partite giocate il giorno indicato."
              + bcolors.ENDC)
        try:
            date = input(bcolors.OKBLUE+"Inserisci Data yyyy-mm-dd: "+ bcolors.ENDC)
            matches = []
            #TO FIX
            for elem in data:
                camp = data[elem._key]
                temp = camp.getMatches(date)
                if temp is not -1:
                    matches += temp
            if len(matches) is 0:
                print(bcolors.BOLD+bcolors.WARNING+"Nessuna partita giocata in questa data"+bcolors.ENDC)
            else:
                for elem in matches:
                    print(elem)
        except TypeError as e:
            print(e, e.with_traceback(sys.exc_info()), bcolors.FAIL+"The insert date is not correct"+bcolors.ENDC)
        except Exception:
            print(bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + "Ops.. Qualcosa è andato storto...")
            print("Ricontrolla la data inserita" + bcolors.ENDC)

    if userChoice == '6':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 6: ")
        print("Dati una giornata e un intero k, stampare le k squadre tra tutti i campionati che hanno segnato più goal."
              + bcolors.ENDC)
        text = int(input(bcolors.OKBLUE+bcolors.BOLD+"\nInserisci Un intero k : "+ bcolors.ENDC))
        try:
            result = data.getTeamMoreGoal(text)
            for elem in result:
                print(elem[0], elem[3])
        except Exception as e:
            print(e)
            print(bcolors.BOLD + bcolors.FAIL + "Ops... Qualcosa è andato storto"+ bcolors.ENDC)

    if userChoice == '7':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 7: ")
        print("Dati una giornata e un intero k, stampare le k squadre tra tutti i campionati che hanno subito meno goal."
            + bcolors.ENDC)
        text = int(input(bcolors.OKBLUE+bcolors.BOLD+"\nInserisci Un intero k : "+ bcolors.ENDC))
        try:
            result = data.getTeamLessGoal(text)
            for elem in result:
                print(elem[0], elem[4])
        except Exception as e:
            print(e)
            print(bcolors.BOLD + bcolors.FAIL + "Ops... Qualcosa è andato storto"+ bcolors.ENDC)

    if userChoice == '8':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 8: ")
        print("Dati una giornata e un intero k, stampare le k squadre tra tutti i campionati con la migliore differenza"
              "reti." + bcolors.ENDC)
        text = int(input(bcolors.OKBLUE+bcolors.BOLD+"\nInserisci Un intero k : "+ bcolors.ENDC))
        try:
            result = data.getTeamDiffGoal(text)
            for elem in result:
                print(elem[0], elem[5])
        except Exception as e:
            print(e)
            print(bcolors.BOLD + bcolors.FAIL + "Ops... Qualcosa è andato storto"+ bcolors.ENDC)

    if userChoice == '9':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 9: ")
        print("Dati una giornata e un campionato, stampare la squadra tra tutti i campionati con il maggior numero di"
              "vittorie, la squadra con il maggior numero di vittorie in casa, la squadra con il maggior numero di vittorie in"
              "trasferta." + bcolors.ENDC)
        try:
            TeamWin, TeamHomeWin, TeamAwayWin = data.getTeamWins()
            print("Team: ", TeamWin[0], "- Numero Vittorie: ", TeamWin[6])
            print("Team: ", TeamHomeWin[0], "- Numero Vittorie Casa: ", TeamHomeWin[7])
            print("Team: ", TeamAwayWin[0], "- Numero Vittorie Trasferta: ", TeamAwayWin[8])

        except Exception as e:
            print(e)
            print(bcolors.BOLD + bcolors.FAIL + "Ops... Qualcosa è andato storto"+ bcolors.ENDC)

    if userChoice == '10':
        print(bcolors.OKBLUE+bcolors.BOLD+"\nTi ringraziamo per aver usufruito del nostro servizio.\nTorna a trovarci.\n" + bcolors.ENDC)
        exit()

    if userChoice == 'debug':
        print(bcolors.OKBLUE + bcolors.BOLD + "Hai scelto l'opzione 'debug'." + bcolors.ENDC)
        print("Campionati: E0, SC0, D1, SP1, I1, F1, N1, B1, P1, T1, G1")
        try:
            text = str(input(bcolors.OKBLUE + bcolors.BOLD + "\nInserisci Codice Campionato: " + bcolors.ENDC))
            text = text.upper()
            camp = data[text]
            for day in camp:
                if text=="SC0":
                    if day <= len(camp.teams) * 3 - 3:
                        print("Day", day)
                    else:
                        print("Partita Rinviata", day - (len(camp.teams) * 3 - 3))
                else:
                    if day <= len(camp.teams) * 2 - 2:
                        print("Day", day)
                    else:
                        print("Partita Rinviata", day - (len(camp.teams) * 2 - 2))
                for match in camp[day]:
                    print("match", match, "Dati Partita: ", camp[day][match])
        except Exception as e:
            print(bcolors.BOLD + bcolors.UNDERLINE + bcolors.FAIL + text + bcolors.FAIL + " non è nel nostro database...")
            print("Ricontrolla il codice del campionato inserito" + bcolors.ENDC)

def caricamentoDatabase():
    text = "Caricamento"
    temp = ""
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write('{0}\r'.format("../"))
        #sys.stdout.write("/")
        for i in range(len(text)):
            temp += text[i]
            sys.stdout.flush()
            sys.stdout.write('{0}'.format(".."+temp))
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write('{0}'.format("|"))
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write('{0}\r'.format(""))
            sys.stdout.flush()
            time.sleep(0.1)
        temp=""


threadingLock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        threadingLock.acquire()
        caricamentoDatabase()
        threadingLock.release()

### INTERFACCIA ###
print("*** Benvenuto nel nostro Centro Scommesse ***\n")
print("Operazioni disponibili: ")
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

thread1 = MyThread()
thread1.start()
data = DataList()
menuChoice(data)
