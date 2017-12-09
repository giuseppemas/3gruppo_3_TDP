from pkg_1.Book import *
import copy
import datetime
from  TdP_collections.hash_table.sorted_table_map import SortedTableMap, MapBase



class DataList(MapBase):
    def __init__(self):
        self._listChampionships = []
        if len(self._listChampionships)==0:
            self._setList()

    def _setList(self):
        names = ["E0","SC0","D1","SP1","I1","F1","N1","B1","P1","T1","G1"]
        for value in names:
            self._listChampionships.append(self._Item(value,Championship(value)))

    def __len__(self):
        return len(self._listChampionships)

    def __iter__(self):
        return self._listChampionships.__iter__()

    def __getitem__(self, item):
        for k in self._listChampionships:
            if k._key == item:
                return k._value

    def __setitem__(self, key, value):
        for k in self._listChampionships:
            if k._key == key:
                k._value=value

    def __delitem__(self, key):
        for k in self._listChampionships:
            if k._key == key:
                del k

    def getTeamLessGoal(self, k , day):
        rank = []
        result = []
        for item in self._listChampionships:
            if item._key=="SC0":
                if 38 < day:
                    checkday = 38
                else:
                    checkday = day
            elif len(item._value.teams)*2-2 < day:
                checkday = len(item._value.teams)*2-2
            else:
                checkday=day
            rank += item._value.get_rankingday(checkday, 4)
        rank = self._sortRank(rank, 0, len(rank) - 1, 4)
        for j in range(k):
            result += [rank[j]]
        return result

    def getTeamMoreGoal(self, k, day):
        rank = []
        result = []
        for item in self._listChampionships:
            if item._key=="SC0":
                if 38 < day:
                    checkday = 38
                else:
                    checkday = day
            elif len(item._value.teams)*2-2 < day:
                checkday = len(item._value.teams)*2-2
            else:
                checkday=day
            rank += item._value.get_rankingday(checkday, 3)
        rank = self._sortRank(rank, 0, len(rank)-1, 3)
        for j in range(k):
            result += [rank[j]]
        return result

    def getTeamDiffGoal(self, k, day):
        rank = []
        result = []
        for item in self._listChampionships:
            if item._key=="SC0":
                if 38 < day:
                    checkday = 38
                else:
                    checkday = day
            elif len(item._value.teams)*2-2 < day:
                checkday = len(item._value.teams)*2-2
            else:
                checkday=day
            rank += item._value.get_rankingday(checkday, 5)
        rank = self._sortRank(rank, 0, len(rank) - 1, 5)
        for j in range(k):
            result += [rank[j]]
        return result

    def getTeamWins(self):
        i=0
        for item in self._listChampionships:
            if item._key == "SC0":
                day = 38
            else:
                day = len(item._value.teams) * 2 - 2
            if i==0:
                lastwin=item._value.get_rankingday(day,6)[0]
                lasthomewin=item._value.get_rankingday(day,7)[0]
                lastAwayWin=item._value.get_rankingday(day,8)[0]
                i+=1
            else:
                win = item._value.get_rankingday(day, 6)[0]
                homewin = item._value.get_rankingday(day, 7)[0]
                AwayWin = item._value.get_rankingday(day, 8)[0]
                if win[6]>lastwin[6]:
                    lastwin=win
                if homewin[7]>lasthomewin[7]:
                    lasthomewin=homewin
                if AwayWin[8]>lastAwayWin[8]:
                    lastAwayWin=AwayWin
        return lastwin,lasthomewin,lastAwayWin

    def _partition(self, rank, start, end, order):
        pos = start
        for i in range(start, end):
            if order==4:
                if rank[i][order] < rank[end][order]:
                    rank[i], rank[pos] = rank[pos], rank[i]
                    pos += 1
            else:
                if rank[i][order] > rank[end][order]:
                    rank[i], rank[pos] = rank[pos], rank[i]
                    pos += 1
        rank[pos], rank[end] = rank[end], rank[pos]
        return pos,rank

    def _sortRank(self, rank, start, end, order):
        if start < end:
            pos,rank= self._partition(rank, start, end, order)
            self._sortRank(rank, start, pos - 1, order)
            self._sortRank(rank, pos + 1, end, order)
        return rank


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
        toCheck = False
        rec = len(self.teams)*2-2
        self[days] = self.DayofSeason()
        temp = self.DayofSeason()
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
                    if len(self[days])<=len(self.teams)//4:
                        if len(temp) is not 0:
                            for i in temp:
                                self[days][i] = temp[i]
                            days += 1
                            rec-=1
                            nextday = True
                            self[days] = self.DayofSeason()
                            self[days][n_match] = ()
                            temp = self.DayofSeason()
                            toCheck = False
                        else:
                            temp=self.DayofSeason()
                            rec+=1
                            self[rec] = self.DayofSeason()
                            for l in range(len(self[days])):
                                l += 1
                                self[rec][l] = self[days][l]
                                temp[l]=self[days][l]
                            toCheck = True
                            self._checkBeforeDay(days, rec)
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
                #print(type(self._daysToDate(k[0])), self._daysToDate(k[0]))
                self[days][n_match] = [self._daysToDate(int(k[0]))]
            elif k[1]==8:
                self[days][n_match] += [k[0]]
                teams+=2
                self._set_partialranking(days,n_match,nextday)
                self._set_ranking(days,n_match, nextday)
                if toCheck:
                    isMatched=self._checkDay(days,n_match, rec, temp)
                    if not isMatched and nextday and len(temp)>=len(self.teams)//4:
                        #print("in if")
                        for i in temp:
                            self[days][i] = temp[i]
                        n_match = 1
                        days += 1
                        teams=0
                        self[days] = self.DayofSeason()
                        self[days][n_match] = ()
                        temp = self.DayofSeason()
                        #print("End", len(temp))
                        toCheck = False
                    elif isMatched:
                        temp = self.DayofSeason()
                        toCheck = False

            else:
                if type(k[0])!=type(""):
                    self[days][n_match] += [int(k[0])]
                else:
                    self[days][n_match] += [k[0]]

    def _checkDay(self, days, n_match, rec, temp):
        for i in self[rec]:
            if self[rec][i][1]==self[days][n_match][1] or self[rec][i][1]==self[days][n_match][2] or self[rec][i][2]==self[days][n_match][1] or self[rec][i][2]==self[days][n_match][2]:
                temp = self.DayofSeason()
                #print(len(temp))
                return True
            else:
                temp[len(temp)+1] = self[days][n_match]
                return False

    def _checkBeforeDay(self, day, rec):
        if len(self[day-1]) == len(self.teams)//2:
            return
        else:
            for i in self[day-1]:
                if self[rec][1][1] == self[day-1][i][1] or self[rec][1][1] == self[day-1][i][2] or self[rec][1][2] == self[day-1][i][1] or self[rec][1][2] == self[day-1][i][2]:
                    return
            self[day-1][len(self[day-1])+1]=self[rec][1]
            for k in self[rec]:
                if k<len(self[rec]):
                    self[rec][k]= self[rec][k+1]
            del self[rec][len(self[rec])]

    def get_rankingday(self,day, order):
        self._sortRank(day, 0, len(self[day]._ranking)-1, order,False)
        return self[day]._ranking

    def get_partialrankingday(self,day):
        self._sortRank(day, 0, len(self[day]._partialrank)-1,2,True)
        return self[day]._partialrank

    def get_historyTeam(self, day, team):
        history = []
        end = day-5
        if end<0:
            end = 0
        for days in range(day, end, -1):
            for match in self[days]:
                if team == self[days][match][1]:
                    if self[days][match][5] == 'H':
                        history += 'W'
                    elif self[days][match][5] == 'D':
                        history += 'D'
                    elif self[days][match][5] == 'A':
                        history += 'A'
                elif team == self[days][match][2]:
                    if self[days][match][5] == 'H':
                        history += 'A'
                    elif self[days][match][5] == 'D':
                        history += 'D'
                    elif self[days][match][5] == 'A':
                        history += 'W'
        return history

    def _set_ranking(self, day, match, nextday):
        if day-1==0:
            if self[day][match][5]=='H':
                self[day]._ranking.append([self[day][match][1], 1, 3, self[day][match][3], self[day][match][4], self[day][match][3]-self[day][match][4],1,1,0])
                self[day]._ranking.append([self[day][match][2], 1, 0, self[day][match][4], self[day][match][3], self[day][match][4]-self[day][match][3],0,0,0])
            elif self[day][match][5]=='D':
                self[day]._ranking.append([self[day][match][1], 1, 1, self[day][match][3], self[day][match][4], self[day][match][3]-self[day][match][4],0,0,0])
                self[day]._ranking.append([self[day][match][2], 1, 1, self[day][match][4], self[day][match][3], self[day][match][4]-self[day][match][3],0,0,0])
            elif self[day][match][5] == 'A':
                self[day]._ranking.append([self[day][match][1], 1, 0, self[day][match][3], self[day][match][4], self[day][match][3]-self[day][match][4],0,0,0])
                self[day]._ranking.append([self[day][match][2], 1, 3, self[day][match][4], self[day][match][3], self[day][match][4]-self[day][match][3],1,0,1])
        else:
            if nextday:
                if len(self[day]._ranking)==0:
                    self[day]._ranking = copy.deepcopy(self[day-1]._ranking)
                #print(self[day]._ranking)

            #print("LEN", len(self[day]._ranking), "Day", day)

            if self[day][match][5] == 'H':
                i=0
                for elem in self[day]._ranking:
                    if elem[0] == self[day][match][1]:
                        elem[1]+=1
                        elem[2]+=3
                        elem[3]+=self[day][match][3]
                        elem[4]+=self[day][match][4]
                        elem[5]= elem[3]-elem[4]
                        elem[6] +=1
                        elem[7] +=1
                        self[day]._ranking[i]=elem

                    if elem[0] == self[day][match][2]:
                        elem[1]+=1
                        elem[3] += self[day][match][4]
                        elem[4] += self[day][match][3]
                        elem[5] = elem[3] - elem[4]
                        self[day]._ranking[i] = elem
                    i+=1
            elif self[day][match][5] == 'D':
                i = 0
                for elem in self[day]._ranking:
                    if elem[0] == self[day][match][1]:
                        elem[1] += 1
                        elem[2] += 1
                        elem[3] += self[day][match][3]
                        elem[4] += self[day][match][4]
                        elem[5] = elem[3] - elem[4]
                        self[day]._ranking[i] = elem
                    if elem[0] == self[day][match][2]:
                        elem[1] += 1
                        elem[2] += 1
                        elem[3] += self[day][match][4]
                        elem[4] += self[day][match][3]
                        elem[5] = elem[3] - elem[4]
                        self[day]._ranking[i] = elem
                    i += 1
            elif self[day][match][5] == 'A':
                i = 0
                for elem in self[day]._ranking:
                    if elem[0] == self[day][match][1]:
                        elem[1] += 1
                        elem[3] += self[day][match][3]
                        elem[4] += self[day][match][4]
                        elem[5] = elem[3] - elem[4]
                        self[day]._ranking[i] = elem
                    if elem[0] == self[day][match][2]:
                        elem[1] += 1
                        elem[2] += 3
                        elem[3] += self[day][match][4]
                        elem[4] += self[day][match][3]
                        elem[5] = elem[3] - elem[4]
                        elem[6] += 1
                        elem[8] += 1
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
            elif self[day][match][8] == 'A':
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
            elif self[day][match][8] == 'A': #Special Case: Bastia-Lyon 16/04/17=42841 33°giornata 8° partita sann chiavat a mazzat partita interrotta
                i = 0
                for elem in self[day]._partialrank:
                    if elem[0] == self[day][match][1]:
                        elem[1] += 1
                        #print("Eccolo",day, match, self[day][match][6], type(self[day][match][6]))
                        #print("Eccolo2", elem[3], type(elem[3]))
                        elem[3] += self[day][match][6]
                        self[day]._partialrank[i] = elem
                    if elem[0] == self[day][match][2]:
                        elem[1] += 1
                        elem[2] += 3
                        elem[3] += self[day][match][7]
                        self[day]._partialrank[i] = elem
                    i += 1

    def _partition(self, day , start, end, order, partial):
        pos = start
        if partial:
            for i in range(start, end):
                if order == 4:
                    if self[day]._partialrank[i][order] < self[day]._partialrank[end][order]:
                        self[day]._partialrank[i], self[day]._partialrank[pos] = self[day]._partialrank[pos], self[day]._partialrank[i]
                        pos += 1
                else:
                    if self[day]._partialrank[i][order] > self[day]._partialrank[end][order]:
                        self[day]._partialrank[i], self[day]._partialrank[pos] = self[day]._partialrank[pos], self[day]._partialrank[i]
                        pos += 1

            self[day]._partialrank[pos], self[day]._partialrank[end] = self[day]._partialrank[end], self[day]._partialrank[pos]
        else:
            for i in range(start, end):
                if order==4:
                    if self[day]._ranking[i][order] < self[day]._ranking[end][order]:
                        self[day]._ranking[i], self[day]._ranking[pos] = self[day]._ranking[pos], self[day]._ranking[i]
                        pos += 1
                else:
                    if self[day]._ranking[i][order] > self[day]._ranking[end][order]:
                        self[day]._ranking[i], self[day]._ranking[pos] = self[day]._ranking[pos], self[day]._ranking[i]
                        pos += 1

            self[day]._ranking[pos], self[day]._ranking[end] = self[day]._ranking[end], self[day]._ranking[pos]
        return pos

    def _sortRank(self, day, start, end, order,partial):
        if start < end:
            pos = self._partition(day, start, end, order, partial)
            self._sortRank(day, start, pos - 1, order,partial)
            self._sortRank(day, pos + 1, end, order, partial)


    def getMatches(self, date):
        date = date.split("-")
        if len(date) is not 3:
            raise TypeError
        else:
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            return self._searchDay(date, 1, len(self))

    def _searchDay(self, date, start, end):
        matches = []
        if (start > end or start < 1 or end < 1):
            return -1
        middle = (start + end)//2
        if (date < self[middle][1][0]):
            return self._searchDay(date, start, middle - 1)
        if (date >= self[middle][1][0]):
            for match in self[middle]:
                if self[middle][match][0]==date:
                    matches+=[self[middle][match]]
            if len(matches) == 0:
                return self._searchDay(date, middle + 1, end)
            else:
                return matches

    def getTeamWins(self, day):
        win=self.get_rankingday(day, 6)[0]
        homewin=self.get_rankingday(day,7)[0]
        awaywin = self.get_rankingday(day,8)[0]
        return win,homewin,awaywin

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

    def _daysToDate(self, days):
        return datetime.date(1899, 12, 30) + datetime.timedelta(days)

"""
text = str(input("Inserisci Codice Campionato: "))
#data = DataList()
camp = Championship(text)
#camp = data[text]
print("Numero Squadre", len(camp.teams))
print(len(camp))
print(camp.teams)
for day in camp:
    if day <= len(camp.teams) * 2 - 2:
        print("Day", day)
    else:
        print("Partita Rinviata", day - (len(camp.teams) * 2 - 2))
    for match in camp[day]:
        print("match", match, "Dati Partita: ", camp[day][match])
"""
"""
text = str(input("Inserisci Codice Campionato: "))
camp = Championship(text)
while True:
    print("Inserisci giornata")
    day = int(input())
    order = int(input("Inserisci ordine"))
    print("RANK")
    print("Team | MP | Pti | GF | GS | DR")
    rank = camp.get_rankingday(day,order)
    for team in rank:
        print(team)

"""