import xlrd
import datetime
class Book:

    def __init__(self):
        self.book = xlrd.open_workbook(filename="all-euro-data-2016-2017.xls")

    def _getSheet(self, championship):
        return self.book.sheet_by_name(championship)


###########
def solve_data(days):
    return datetime.date(1900,1,1)+datetime.timedelta(days)

def _checkmatchpostponed(self, day, match):
    for i in range(len(self.teams) * 2 - 1, len(self) + 1):
        for k in self[i]:
            if self[i][k][9]:
                if self[i][k][0] < self[day][match][0]:
                    if self[i][k][5] == 'H':
                        t = 0
                        for elem in self[day]._ranking:
                            if elem[0] == self[i][k][1]:
                                elem[1] += 1
                                elem[2] += 3
                                self[day]._ranking[t] = elem
                            if elem[0] == self[i][k][2]:
                                elem[1] += 1
                                self[day]._ranking[t] = elem
                            t += 1
                        self[i][k][9] = False
                    elif self[day][match][5] == 'D':
                        t = 0
                        for elem in self[day]._ranking:
                            if elem[0] == self[i][k][1]:
                                elem[1] += 1
                                elem[2] += 1
                                self[day]._ranking[t] = elem
                            if elem[0] == self[i][k][2]:
                                elem[1] += 1
                                elem[2] += 1
                                self[day]._ranking[t] = elem
                            t += 1
                        self[i][k][9] = False
                    else:
                        t = 0
                        for elem in self[day]._ranking:
                            if elem[0] == self[i][k][1]:
                                elem[1] += 1
                                self[day]._ranking[t] = elem
                            if elem[0] == self[i][k][2]:
                                elem[1] += 1
                                elem[2] += 3
                                self[day]._ranking[t] = elem
                            t += 1
                        self[i][k][9] = False
                else:
                    return
