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

print(solve_data(42812))