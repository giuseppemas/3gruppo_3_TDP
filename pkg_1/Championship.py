from pkg_1.Book import *
import copy
from  TdP_collections.hash_table.sorted_table_map import SortedTableMap, MapBase


class DataList(MapBase):
    def __init__(self):
        self._listChampionships = []

    def _setList(self):
        names = ["E0","SC0","D1","SP1","I1","F1","N1","B1","P1","T1","G1"]
        for value in names:
            self._listChampionships.append(self._Item(value,Championship(value)))

class Championship(SortedTableMap):
    """Class contains Days of season and Matches postponed"""

    class DayofSeason(SortedTableMap):
        """Class contains matches' number and data"""
        def __init__(self):
            super().__init__()
            self._ranking = []
            self._partialrank = []

    def __init__(self,name):
        super().__init__()
        self.name = name
        self.teams = []
        self.sheet = Book()._getSheet(self.name)
        if len(self.teams)==0:
            self._set_teams_championship()
            self._set_day_season()

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
        nextday=False
        rec = len(self.teams)*2-2
        self[days] = self.DayofSeason()
        for k in self._read_sheet():
            if k[1] == 0 and k[2] == 1:  #k[0] value, k[1] column index, k[2] row index
                lastdate = k[0]
                n_match += 1
                self[days][n_match] = []
            if k[1] == 0 and k[2] > 1:
                if k[0] <= lastdate + 1 and teams <len(self.teams):
                    n_match += 1
                    self[days][n_match] = []
                    lastdate = k[0]
                    nextday=False
                else:
                    if len(self[days])<len(self.teams)//4:
                        rec+=1
                        self[rec] = self.DayofSeason()
                        for l in range(len(self[days])):
                            l += 1
                            self[rec][l] = self[days][l]
                        teams = 0
                        n_match = 1
                        lastdate = k[0]

                    else:
                        nextday=True
                        teams = 0
                        n_match = 1
                        days += 1
                        self[days]= self.DayofSeason()
                        self[days][n_match] = ()
                        lastdate = k[0]
            #print("days", days, "n_match", n_match)
            if k[1]==0:
                self[days][n_match] = [int(k[0])]
            elif k[1]==8:
                self[days][n_match] += [k[0]]
                teams+=2
                self._set_partialranking(days,n_match,nextday)
                self._set_ranking(days,n_match, nextday)
            else:
                if type(k[0])!=type(""):
                    self[days][n_match] += [int(k[0])]
                else:
                    self[days][n_match] += [k[0]]

    def get_rankingday(self,day):
        self.sort_rank(day)
        return self[day]._ranking

    def get_ranking(self):
        self.get_rankingday(len(self.teams)*2-2)

    def get_partialrankingday(self,day):
        return self[day]._partialrank

    def get_partialranking(self):
        self.get_partialrankingday(len(self.teams)*2-2)

    def _set_ranking(self, day, match, nextday):
        if day-1==0:
            if self[day][match][5]=='H':
                self[day]._ranking.append([self[day][match][1], 1, 3, self[day][match][3]])
                self[day]._ranking.append([self[day][match][2], 1, 0, self[day][match][4]])
            elif self[day][match][5]=='D':
                self[day]._ranking.append([self[day][match][1], 1, 1, self[day][match][3]])
                self[day]._ranking.append([self[day][match][2], 1, 1, self[day][match][4]])
            else:
                self[day]._ranking.append([self[day][match][1], 1, 0, self[day][match][3]])
                self[day]._ranking.append([self[day][match][2], 1, 3, self[day][match][4]])
        else:
            if nextday:
                #print("LEN",len(self[day]._ranking), "Day", day)
                if len(self[day]._ranking)==0:
                    self[day]._ranking = copy.deepcopy(self[day-1]._ranking)
            if self[day][match][5] == 'H':
                i=0
                for elem in self[day]._ranking:
                    if elem[0] == self[day][match][1]:
                        elem[1]+=1
                        elem[2]+=3
                        elem[3]+=self[day][match][3]
                        self[day]._ranking[i]=elem
                    if elem[0] == self[day][match][2]:
                        elem[1]+=1
                        elem[3] += self[day][match][4]
                        self[day]._ranking[i] = elem
                    i+=1
            elif self[day][match][5] == 'D':
                i = 0
                for elem in self[day]._ranking:
                    if elem[0] == self[day][match][1]:
                        elem[1] += 1
                        elem[2] += 1
                        elem[3] += self[day][match][3]
                        self[day]._ranking[i] = elem
                    if elem[0] == self[day][match][2]:
                        elem[1] += 1
                        elem[2] += 1
                        elem[3] += self[day][match][4]
                        self[day]._ranking[i] = elem
                    i += 1
            else:
                i = 0
                for elem in self[day]._ranking:
                    if elem[0] == self[day][match][1]:
                        elem[1] += 1
                        elem[3] += self[day][match][3]
                        self[day]._ranking[i] = elem
                    if elem[0] == self[day][match][2]:
                        elem[1] += 1
                        elem[2] += 3
                        elem[3] += self[day][match][4]
                        self[day]._ranking[i] = elem
                    i += 1

    def _set_partialranking(self,day, match,nextday):
        if day-1==0:
            if self[day][match][8]=='H':
                self[day]._partialrank.append([self[day][match][1], 1, 3, self[day][match][6]])
                self[day]._partialrank.append([self[day][match][2], 1, 0, self[day][match][7]])
            elif self[day][match][8]=='D':
                self[day]._partialrank.append([self[day][match][1], 1, 1, self[day][match][6]])
                self[day]._partialrank.append([self[day][match][2], 1, 1, self[day][match][7]])
            else:
                self[day]._partialrank.append([self[day][match][1], 1, 0, self[day][match][6]])
                self[day]._partialrank.append([self[day][match][2], 1, 3, self[day][match][7]])
        else:
            if nextday:
                #print("LEN",len(self[day]._partialrank), "Day", day)
                if len(self[day]._partialrank)==0:
                    self[day]._partialrank = copy.deepcopy(self[day-1]._partialrank)
            if self[day][match][8] == 'H':
                i=0
                for elem in self[day]._partialrank:
                    if elem[0] == self[day][match][1]:
                        elem[1]+=1
                        elem[2]+=3
                        elem[3] += self[day][match][6]
                        self[day]._partialrank[i]=elem
                    if elem[0] == self[day][match][2]:
                        elem[1]+=1
                        elem[3] += self[day][match][7]
                        self[day]._partialrank[i] = elem
                    i+=1
            elif self[day][match][8] == 'D':
                i = 0
                for elem in self[day]._partialrank:
                    if elem[0] == self[day][match][1]:
                        elem[1] += 1
                        elem[2] += 1
                        elem[3] += self[day][match][6]
                        self[day]._partialrank[i] = elem
                    if elem[0] == self[day][match][2]:
                        elem[1] += 1
                        elem[2] += 1
                        elem[3] += self[day][match][7]
                        self[day]._partialrank[i] = elem
                    i += 1
            else:
                i = 0
                for elem in self[day]._partialrank:
                    if elem[0] == self[day][match][1]:
                        elem[1] += 1
                        elem[3] += self[day][match][6]
                        self[day]._partialrank[i] = elem
                    if elem[0] == self[day][match][2]:
                        elem[1] += 1
                        elem[2] += 3
                        elem[3] += self[day][match][7]
                        self[day]._partialrank[i] = elem
                    i += 1

    def sort_rank(self, day):
        self[day]._ranking._quickSortHelper(0, len(self[day]._ranking)-1)


    def _quickSortHelper(self, first, last):
        if first < last:
            splitpoint = self._partition(first, last)

            self._quickSortHelper(first, splitpoint - 1)
            self._quickSortHelper( splitpoint + 1, last)

    def _partition(self, first, last):
        pivotvalue = self[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and self[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while self[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = self[leftmark]
                self[leftmark] = self[rightmark]
                self[rightmark] = temp

        temp = self[first]
        self[first] = self[rightmark]
        self[rightmark] = temp

        return rightmark

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

def choicecamp(text, listaCampionati):
    for item in listaCampionati:
        if item._key==text:
            camp = item._value
            return camp
text = str(input("Inserisci Codice Campionato: "))

camp = Championship(text)
print("Numero Squadre", len(camp.teams))
print(camp.teams)
for day in camp:
    if day <= len(camp.teams)*2-2:
        print("Day", day)
    else:
        print("Partita Rinviata", day-(len(camp.teams)*2-2))
    for match in camp[day]:
        print("match", match, "Dati Partita: ", camp[day][match])

print("Inserisci giornata")
day = input()
print("RANK")
print("Team | MP | Score | G")
for team in camp[int(day)]._ranking:
    print(team)
print("Partial Rank")
for team in camp[int(day)]._partialrank:
    print(team)