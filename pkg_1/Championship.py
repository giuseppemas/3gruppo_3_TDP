from pkg_1.Book import *

class Championship():

    class DaySeason():
        pass


    def __init__(self, name):
        self.name = name
        self.teams = []
        self.n_teams = 0
        self.sheets = Book()

    def _first_iteration(self):
        sheet = self.sheets._getSheet(self.name)
        days = 1
        n_match = 0
        giornata = {}
        giornata["giornata" + str(days)] = {}
        for k in self.sheets.inverse_read_sheet(self.name):
            #first iteration
            if k[1]==0 and k[2] == sheet.nrows-1:
                lastdate = k[0]
                n_match += 1
                giornata["giornata" + str(days)][str(n_match) + "match"] = (int(lastdate), )
            if k[1]==0 and k[2]<sheet.nrows-1:
                if k[0] >= lastdate-1:
                    n_match += 1
                    lastdate = k[0]
                    giornata["giornata" + str(days)][str(n_match) + "match"] = (int(lastdate),)
                else:
                    return
            if k[1]==1:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (k[0],)
            if k[1]==2:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (k[0],)
                self._setTeam(giornata["giornata"+str(days)][str(n_match)+"match"])
            if k[1]==3:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)
            if k[1]==4:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)
            if k[1]==6:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)
            if k[1]==7:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)


    def _set_day_season(self):
        self._first_iteration()
        teams = 0
        days = 1
        n_match = 0
        giornata = {}
        giornata["giornata" + str(days)] = {}
        for k in self.sheets.read_sheet(self.name):
            if k[1] == 0 and k[2] == 1:
                lastdate = k[0]
                n_match += 1
                giornata["giornata" + str(days)][str(n_match) + "match"] = None
            if k[1] == 0 and k[2] > 1:
                if k[0] <= lastdate + 1 and teams <= self.n_teams//2:
                    n_match += 1
                    giornata["giornata" + str(days)][str(n_match) + "match"] = None
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
                teams+=2
            if k[1] == 3:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)
            if k[1] == 4:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)
            if k[1] == 6:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)
            if k[1] == 7:
                giornata["giornata" + str(days)][str(n_match) + "match"] += (int(k[0]),)

        print("squadre", teams)
        return giornata

    def _setTeam(self,match):
        self.teams.append(match[1])
        self.teams.append(match[2])
        self.n_teams +=2



    def _getTeams(self):
        return self.teams


###PROVA###
print("PROVA")
camp = Championship("N1")

print("Squadre")
camp._first_iteration()
print(camp.teams)
print("Numero Squadre",camp.n_teams)

