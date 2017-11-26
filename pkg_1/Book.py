import xlrd

class Book:
    def __init__(self):
        self.book = xlrd.open_workbook(filename="all-euro-data-2016-2017.xls")

    def read_sheet(self, campionato):
        sheet = self.book.sheet_by_name(campionato)
        print(sheet.nrows)
        d = {}
        for i in range(sheet.nrows):
            for values in sheet.row_values(rowx=i,start_colx=1,end_colx=10):
                if i == 0:
                    pass
                else:
                     pass
                print(values, end=" ")
            print("\n")

###########
book = Book()
book.read_sheet("I1")