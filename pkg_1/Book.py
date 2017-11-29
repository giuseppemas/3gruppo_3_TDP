import xlrd

class Book:
    def __init__(self):
        self.book = xlrd.open_workbook(filename="all-euro-data-2016-2017.xls")

    def read_sheet(self, championship):
        sheet = self._getSheet(championship)
        for i in range(sheet.nrows-1):
            i+=1
            j=0
            for values in sheet.row_values(rowx=i,start_colx=1,end_colx=10):
                yield values,j,i
                j+=1
    def inverse_read_sheet(self, championship):
        sheet = self._getSheet(championship)
        for i in range(sheet.nrows-1, 1, -1):
            j=0
            for values in sheet.row_values(rowx=i,start_colx=1,end_colx=10):
                yield  values,j,i
                j+=1

    def _getSheet(self, championship):
        return self.book.sheet_by_name(championship)


    def teams(self, championship):
        n_teams = self.giornate(championship)
        TEAMS = []
        for k in range(n_teams[1]//2):
            k+=1
            temp = n_teams[0]["giornata1"][str(k)+"match"]
            TEAMS.append(temp[0])
            TEAMS.append(temp[1])
        return TEAMS


    def giornate(self, championship):
        teams=0
        days=1
        n_match = 0
        giornata = {}
        giornata["giornata"+str(days)]= {}
        for k in self.read_sheet(championship):
            if k[1]==0 and k[2]==1:
                lastdate = k[0]
                teams += 2
                n_match += 1
                giornata["giornata" + str(days)][str(n_match) + "match"] = None
            if k[1]==0 and k[2]>1:
                if k[0]<= lastdate+1:
                    teams+=2
                    n_match +=1
                    giornata["giornata"+str(days)][str(n_match)+"match"]= None
                    lastdate= k[0]
                else:
                    teams = 0
                    n_match=1
                    days+=1
                    giornata["giornata" + str(days)]={}
                    teams+=2
                    lastdate = k[0]
            if k[1]==1:
                giornata["giornata"+str(days)][str(n_match)+"match"] = (k[0],)
            if k[1]==2:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (k[0],)
            if k[1]==3:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)
            if k[1]==4:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)
            if k[1]==6:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)
            if k[1]==7:
                giornata["giornata"+str(days)][str(n_match)+"match"] += (int(k[0]),)

        print("squadre",teams)
        return giornata,teams



###########
def solve_data(days):
    y = days//365
    anno = 1900 + y
    months = days-(y*365)
    month = months//30
    day = days - (month*30 + (y*365))
    return day,month,anno