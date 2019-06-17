import xlrd

#custo_bomba_ligada
cbl = []
#acionamento_de_bomba
ab = []
#vazao_da_bomba
vb = []
#vazao_da_bomba_para_reservatorio
vbr=[]
#fracao_de_t
fdt = []
#custo_transferir_agua
cta =[]
def getOpen(book):
        sh = book.sheet_by_index(0)
        #print(sh.name, sh.nrows, sh.ncols)
        h=sh.cell_value(rowx=0,colx=0)
        md=sh.cell_value(rowx=0,colx=1)
        mi=sh.cell_value(rowx=0,colx=2)
        ma=sh.cell_value(rowx=0,colx=3)

        count = 1
        sc=0
        for rx in range(1,sh.nrows):
                #print(sh.row(rx))
                #c1=sh.cell_value(rowx=rx,colx=0)
                c2=sh.cell_value(rowx=rx,colx=1)
                #c3=sh.cell_value(rowx=rx,colx=2)
                #c4=sh.cell_value(rowx=rx,colx=3)
                #print(' Coluna : ',c1)
                print(' Coluna : ',c2)
                #print(' coluna : ',c3)
                #print(' coluna : ',c4)
                sc+=int(c2)
                if count == 4:
                        setVazaoDaBomba(sc/4)
                        sc=0
                        count=0
                count+=1
        setVazaoDaBombaParaReservatorio(243.89)

def getOpenCusto(book=xlrd.open_workbook("panilha/Total e consumoKwh.xls")):
    sh = book.sheet_by_index(0)
    #print(sh.name, sh.nrows, sh.ncols)
    m=sh.cell_value(rowx=0,colx=0)
    ct=sh.cell_value(rowx=0,colx=1)
    cp=sh.cell_value(rowx=0,colx=2)
    cfP=sh.cell_value(rowx=0,colx=3)
    ct=sh.cell_value(rowx=0,colx=4)

    for rx in range(1,sh.nrows):
        #print(sh.row(rx))
        #c1=sh.cell_value(rowx=rx,colx=0)
        c2=sh.cell_value(rowx=rx,colx=1)
        #c3=sh.cell_value(rowx=rx,colx=2)
        #c4=sh.cell_value(rowx=rx,colx=3)
        #c5=sh.cell_value(rowx=rx,colx=4)
        #print(' Coluna : ',c1)
        print(' Coluna : ',c2)
        #print(' coluna : ',c3)
        #print(' coluna : ',c4)
        #print(' coluna : ',c5)
        setCustoDaBombaLigada(int(c2)*0.10)
        setAcionamentoDaBomba(int(c2)*0.10)
        setCustoParaTransferirAgua(int(c1))
        #####################
def setCustoDaBombaLigada(x):
        global cbl
        cbl.append(x)
def setAcionamentoDaBomba(x):
        global ab
        ab.append(x)
def setVazaoDaBomba(x):
        global vb
        vb.append(x)
def setVazaoDaBombaParaReservatorio(x):
        global vbr
        vbr.append(x)
def setFracaoDeTempo(x):
        global fdt
        fdt.append(x)
def setCustoParaTransferirAgua(x):
        global cta
        cta.append(x)

        #################

def getCustoDaBombaLigada():
        return global cbl 
def getAcionamentoDaBomba():
        return global ab   
def getVazaoDaBomba():
        return global vb
def getVazaoDaBombaParaReservatorio():
        return global vbr
def getCustoParaTransferirAgua():
        return global cta