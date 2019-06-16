import xlrd
def getPlanilhas():
    book1  = xlrd.open_workbook("panilhas/Vazão 03-18.xls")
    book2  = xlrd.open_workbook("panilhas/Vazão 04-18.xls")
    book3  = xlrd.open_workbook("panilhas/Vazão 05-18.xls")
    book4  = xlrd.open_workbook("panilhas/Vazão 06-18.xls")
    book5  = xlrd.open_workbook("panilhas/Vazão 07-18.xls")
    book6  = xlrd.open_workbook("panilhas/Vazão 08-18.xls")
    book7  = xlrd.open_workbook("panilhas/Vazão 09-18.xls")
    book8  = xlrd.open_workbook("panilhas/Vazão 10-18.xls")
    book9  = xlrd.open_workbook("panilhas/Vazão 11-18.xls")
    book10 = xlrd.open_workbook("panilhas/Vazão 12-18.xls")
    book11 = xlrd.open_workbook("panilhas/Vazão 01-19.xls")
    book12 = xlrd.open_workbook("panilhas/Vazão 02-19.xls")
    book13 = xlrd.open_workbook("panilhas/Volume do RAP Prazeres.xls")
    l=[book1,book2,book3,book4,book5,book6,book7,book8,book9,book10,book11,book12,book13]
    return l
