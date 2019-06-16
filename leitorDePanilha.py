import xlrd
#print ("Número de abas: ", book.nsheets)
#print ("Nomes das Planilhas:", book.sheet_names())
def getValeus(book):
    sh = book.sheet_by_index(0)
    #print(sh.name, sh.nrows, sh.ncols)
    h=sh.cell_value(rowx=0,colx=0)
    md=sh.cell_value(rowx=0,colx=1)
    mi=sh.cell_value(rowx=0,colx=2)
    ma=sh.cell_value(rowx=0,colx=3)
    v2 = 0
    v3 = 0
    v4 = 0
    for rx in range(1,sh.nrows):
        #print(sh.row(rx))
        c1=sh.cell_value(rowx=rx,colx=0)
        c2=sh.cell_value(rowx=rx,colx=1)
        c3=sh.cell_value(rowx=rx,colx=2)
        c4=sh.cell_value(rowx=rx,colx=3)
        print(' Coluna : ',c1)
        print(' Coluna : ',c2)
        print(' coluna : ',c3)
        print(' coluna : ',c4)
    input("") 