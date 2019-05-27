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
        v1 = sh.cell_value(rowx=rx,colx=0)
        v2 += sh.cell_value(rowx=rx,colx=1)
        v3 += sh.cell_value(rowx=rx,colx=2)
        v4 += sh.cell_value(rowx=rx,colx=3)
    print(md+' Total : ',v2)
    print(mi+' Total : ',v3)
    print(ma+' Total : ',v4) 