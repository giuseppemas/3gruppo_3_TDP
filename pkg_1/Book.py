import xlrd

class Book:

    def __init__(self):
        self.book = xlrd.open_workbook(filename="all-euro-data-2016-2017.xls")

    def _getSheet(self, championship):
        return self.book.sheet_by_name(championship)


###########
def solve_data(days):
    y = days//365
    anno = 1900 + y
    months = days-(y*365)
    month = months//30
    day = days - (month*30 + (y*365))
    return day,month,anno