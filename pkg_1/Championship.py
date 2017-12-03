from pkg_1.Book import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Championship():

    def __init__(self, name):
        self.name = name
        self.teams = []
        self.sheet= Book()._getSheet(self.name)
        if len(self.teams)==0:
            self._set_teams_championship()

    def _set_teams_championship(self):
        """This method set all the team in a championship """
        for k in self._team_generator():
            if k[1]==0 and k[2] == self.sheet.nrows-1:
                lastdate = k[0]
            if k[1]==0 and k[2]<self.sheet.nrows-1:
                if k[0] >= lastdate-1:
                    lastdate = k[0]
                else:
                    return
            if k[1]==1:
                self._setTeam(k[0])
            if k[1]==2:
                self._setTeam(k[0])

    def _setTeam(self, match):
        self.teams.append(match)


    def _getTeams(self):
        return self.teams


    def _set_day_season(self):
        teams = 0
        days = 1
        n_match = 0
        rec = 0
        giornata = {}
        giornata["giornata" + str(days)] = {}
        for k in self._read_sheet():
            if k[1] == 0 and k[2] == 1:
                lastdate = k[0]
                teams+=2
                n_match += 1
                giornata["giornata" + str(days)][str(n_match) + "match"] = None
            if k[1] == 0 and k[2] > 1:
                if k[0] <= lastdate + 1 and teams <=len(self.teams):
                    n_match += 1
                    teams+=2
                    giornata["giornata" + str(days)][str(n_match) + "match"] = None
                    lastdate = k[0]
                else:
                    if len(giornata["giornata" + str(days)])<len(self.teams)//4:
                        rec+=1
                        giornata["giornata" + "recuperata"+str(rec)] = {}
                        for l in range(len(giornata["giornata" + str(days)].values())):
                            l += 1
                            giornata["giornata" + "recuperata"+ str(rec)][str(l) + "match"]=giornata["giornata" + str(days)][str(l)+"match"]
                        teams = 0
                        n_match = 1
                        lastdate = k[0]
                    else:
                        teams = 0
                        n_match = 1
                        days += 1
                        giornata["giornata" + str(days)] = {}
                        lastdate = k[0]

            if k[1] == 1:
                giornata["giornata" + str(days)][str(n_match) + "match"] = (k[0],)
            if k[1] == 2:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (k[0],)
            if k[1] == 3:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)
            if k[1] == 4:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)
            if k[1] == 6:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)
            if k[1] == 7:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)

        return giornata

    def _read_sheet(self):
        for i in range(self.sheet.nrows - 1):
            i += 1
            j = 0
            for values in self.sheet.row_values(rowx=i, start_colx=1, end_colx=10):
                yield values, j, i
                j += 1


    def _team_generator(self):
        for i in range(self.sheet.nrows-1, 1, -1):
            j=0
            for values in self.sheet.row_values(rowx=i,start_colx=1,end_colx=4):
                yield  values,j,i
                j+=1



"""
giornata =camp._set_day_season()
rec = 0
for i in range(len(giornata.keys())):
    i+=1
    if i <= 38:
        print("\ngiornata", i)
        for k in range(len(giornata["giornata"+str(i)])):
            k+=1
            print("Numero Match", k)
            print(giornata["giornata"+str(i)][str(k)+"match"])
    else:
        rec+=1
        print("\n")
        for j in range(len(giornata["giornata" + "recuperata"+str(rec)])):
            j+=1
            print("partita recuperata", rec)
            print(giornata["giornata" + "recuperata"+str(rec)][str(j) + "match"])

"""
