import pkg_1.xlrd as xlrd
import datetime
class Book:

    def __init__(self):
        self.book = xlrd.open_workbook(filename="all-euro-data-2016-2017.xls")

    def _getSheet(self, championship):
        return self.book.sheet_by_name(championship)


###########
def daysToDate(days):
    return datetime.date(1899,12,30) + datetime.timedelta(days)
