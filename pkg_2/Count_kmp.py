import time

def compute_kmp_fail(P):

    m = len(P)
    fail = [0]*m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

def find_kmp(T,P):

    n,m = len(T), len(P)
    count = 0
    confronti = 0
    if m == 0: return n+1
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            confronti += 1
            if k == m - 1:
                count += 1
                k = -1
                #return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    print("Numero di confronti: ", confronti)
    return count

def find_brute(T,P):

    n, m = len(T), len(P)
    count = 0
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            count += 1
    return count

print("Efficienza della soluzione proposta (count_ kmp):\n")

T1 = "In un mondo sempre più orientato all’innovazione ed in un sistema che " \
    "si affida sempre di più alle nuove tecnologie è giusto chiedersi quanto queste" \
    "ultime siano sicure. Al giorno d’oggi si sente spesso parlare di cyber-security e" \
    "non suscitano più molto stupore notizie di violenti attacchi informatici verso" \
    "l’ennesima azienda o istituzione di turno. Sembra essersi ormai consolidata" \
    "l’idea che forse non siamo ancora pronti a proteggerci da un simile passo" \
    "verso il futuro. " \
    "Internet rappresenta attualmente la tecnologia più potente e diffusa in" \
    "grado di collegare miliardi di dispositivi fra di loro, per questo motivo è anche" \
    "quella più a rischio. Esistono diverse minacce nel web. Alcune sono volte" \
    "a sottrarre informazioni riservate ed altre cercano di controllare i dispositivi" \
    "della rete per poter utilizzare le loro risorse di calcolo." \
    "In questo secondo caso rientrano gli attacchi Denial-of-Service1 (DoS)," \
    "dove il sistema scelto come bersaglio dell’attacco, viene inondato di richieste" \
    "finché non è più in grado di servirle. In questo modo il servizio offerto non" \
    "è più disponibile e viene negato anche al resto degli utenti che vorrebbero" \
    "usufruirne. I primi attacchi DoS erano caratterizzati da un unico attaccante" \
    "dotato di una enorme capacità di calcolo che, ripetendo la stessa richiesta" \
    "con un tasso elevatissimo, era in grado di saturare le risorse della vittima [1]." \
    "In italiano letteralmente “negazione del servizio”: è un attacco in cui si fa in modo di" \
    "saturare le risorse di un sistema informatico che fornisce servizi a dei clienti." \
    "Questi attacchi sono relativamente facili da rilevare perchè esiste un singolo" \
    "nodo della rete che svolge un’attività manifestatamente insolita." \
    "Una variante particolarmente critica per i sistemi informatici sono gli" \
    "attacchi Distributed DoS (DDoS), caratterizzati da una rete di dispositivi" \
    "molto vasta. Questi dispositivi sono nodi compromessi, detti zombie, che in" \
    "qualche modo sono stati violati e che non sono a conoscenza delle richieste" \
    "che inviano alla vittima. La capacità di calcolo dei singoli nodi è limitata," \
    "ma la potenza di questo attacco risiede nell’azione sincronizzata di questo" \
    "“esercito” di zombie che, dato il grande numero di richieste inviate, riesce a" \
    "saturare le risorse del sistema. I nodi di questa rete sono quindi degli automi" \
    "che eseguono, senza volere, i comandi di chi coordina l’attacco (il botmaster)" \
    "e per questo motivo sono detti bots2 e la rete che compongono è denominata" \
    "appunto botnet." \
    "In [2] [3] sono presenti tutte le varianti più pericolose degli attacchi DDoS" \
    "a livello applicazione. In [4] sono mostrati i dati dell’ultimo semestre e si" \
    "traccia un bilancio finale dove emerge chiaramente quanto sia seria e delicata" \
    "la questione che stiamo trattando. In [5] [6] è presente una panoramica delle" \
    "soluzioni disponibili per difendersi da queste minacce." \
    "Per un sistema non è difficile rilevare una crescita anomala del tasso di" \
    "richieste in entrata. In altri termini, non è difficile accorgersi che in qualche" \
    "modo le risorse stanno per essere saturate ed è presente un’anomalia infatti," \
    "in presenza di un attacco DDoS, si registra un’attività molto intensa data" \
    "dal fatto che il numero di utenti diventa molto grande. Buona parte di questi" \
    "utenti saranno dei bots che inviano in modo automatico le loro richieste. A" \
    "differenza di quanto detto per gli attacchi DoS, un attacco distribuito non" \
    "ha un centro e quindi non possiamo identificare un unico nodo che svolge" \
    "un’attività anomala verso il sistema, ma ci saranno molti nodi che apparentemente" \
    "svolgono un’attività lecita. La vera sfida è capire se l’anomalia" \
    "è causata da un attacco DDoS e, in tal caso, riuscire a discriminare i bots" \
    "dagli utenti reali. Nasce quindi il problema di identificare correttamente la" \
    "botnet durante un attacco DDoS, in modo da bloccare gli utenti malevoli e" \
    "permettere agli utenti reali di poter accedere ai servizi offerti."

T = "bacaabaccabacbaabb"
P = "abacab"

N = 1

inizio = time.clock()
for i in range(N):
    value = T.count(P)
fine = time.clock()
tempo_count = (fine - inizio)
print("Tempo impiegato da count: ",tempo_count, "secondi,   Output: ", value)

inizio = time.clock()
for i in range(N):
    value = find_kmp(T,P)
fine = time.clock()
tempo_count_kmp = (fine - inizio)
print("Tempo impiegato da find_kmp: ",tempo_count_kmp, "secondi,   Output: ", value)

inizio = time.clock()
for i in range(N):
    value = find_brute(T,P)
fine = time.clock()
tempo_brute = (fine - inizio)
print("Tempo impiegato da find_brute: ",tempo_brute, "secondi,   Output: ", value)

print("\nRapporto delle prestazioni con Count di str:\n ")
print("Count: ", tempo_brute/tempo_count*100, "% \nfind_kmp: ", tempo_brute/tempo_count_kmp*100, "% \nfind_brute: ", tempo_brute/tempo_brute*100, " %\n")

print("\nRapporto delle prestazioni fra Knuth-Morris-Pratt e Brute Force:\n ")
print("find_kmp: ", tempo_brute/tempo_count_kmp*100, "% \nfind_brute: ", tempo_brute/tempo_brute*100, " %")