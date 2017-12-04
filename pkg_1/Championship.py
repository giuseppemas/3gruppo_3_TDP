from pkg_1.Book import *
from  TdP_collections.hash_table.sorted_table_map import SortedTableMap, MapBase


class DataList(MapBase):
    def __init__(self):
        self._listChampionships = []

    def _setList(self):
        names = ["E0","SC0","D1","SP1","I1","F1","N1","B1","P1","T1","G1"]
        for value in names:
            self._listChampionships.append(self._Item(value,Championship(value)))

class Championship(SortedTableMap):

    class DayofSeason(SortedTableMap):

        def __init__(self):
            super().__init__()


    def __init__(self,name):
        super().__init__()
        self.name = name
        self.teams = []
        self.sheet = Book()._getSheet(self.name)
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
        rec = len(self.teams)*2-2
        self[days] = self.DayofSeason()
        for k in self._read_sheet():
            if k[1] == 0 and k[2] == 1:
                lastdate = k[0]
                teams+=2
                n_match += 1
                self[days][n_match] = ()
            if k[1] == 0 and k[2] > 1:
                if k[0] <= lastdate + 1 and teams <=len(self.teams):
                    n_match += 1
                    teams+=2
                    self[days][n_match] = ()
                    lastdate = k[0]
                else:
                    if len(self[days])<len(self.teams)//4:
                        rec+=1
                        self[rec] = self.DayofSeason()
                        for l in range(len(self[days])):
                            l += 1
                            self[rec][l]= self[days][l]
                        teams = 0
                        n_match = 1
                        lastdate = k[0]
                    else:
                        teams = 0
                        n_match = 1
                        days += 1
                        self[days]= self.DayofSeason()
                        self[days][n_match] = ()
                        lastdate = k[0]

            #print("days", days, "n_match", n_match)
            if k[1]==0:
                self[days][n_match] = (k[0],)
            else:
                self[days][n_match] += (k[0],)

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


text = str(input("Inserisci Codice Campionato: "))
camp = Championship(text)
print("Numero Squadre", len(camp.teams))
print(camp.teams)
camp._set_day_season()
for day in camp:
    if day <= len(camp.teams)*2-2:
        print("Day", day)
    else:
        print("Partita Rinviata", day-(len(camp.teams)*2-2))
    for match in camp[day]:
        print("match", match, "Data", camp[day][match])

