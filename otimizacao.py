from guroby import *
import openPanilhas, leitorDePanilha

try:
    modelo = Model('otimizacaoEnergia')

    #VARIAVEIS
    demanda = [63971,63971,63971,63971,63971,63971,63971,63971,63971,63971,63971,63971]
    tempo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    custo_bomba_ligada               = leitorDePanilha.getCustoDaBombaLigada()
    acionamento_de_bomba             = leitorDePanilha.getAcionamentoDaBomba()
    vazao_da_bomba                   = leitorDePanilha.getVazaoDaBomba()
    vazao_da_bomba_para_reservatorio = leitorDePanilha.getVazaoDaBombaParaReservatorio()
    volume_minimo_reservatorio       = 1
    volume_maximo_reservatorio       = 1
    volume_do_reservatorio_inicio    = 1
    volume_do_reservatorio_final_do_periodo_t = 1
    fracao_de_t = []
    custo_transferir_agua            = leitorDePanilha.getCustoParaTransferirAgua()
    #a bomba começa desligada
    estado_inicial_da_bomba = 0

    # VARIAVEIS GUROBI


    Yjt = modelo.addVar(vtype = GRB.BINARY, name="Yjt")

    #aciona a bomba
    ALFAjt = modelo.addVar(vtype = GRB.BINARY, name="alfajt")


    #demanda do centro consumidor - no caso da gente vai ser continua
    Dkt = modelo.addVars(demanda ,vtype = GRB.CONTINUOUS, name = "Dkt")
    # custo para manter a bomba ligada no tempo t
    Ctj = modelo.addVars(custo_bomba_ligada,vtype = GRB.CONTINUOUS, name = "Ctj")

    SCjt = modelo.addVars(acionamento_de_bomba,vtype = GRB.CONTINUOUS, name = "SCjt")

    Vjt = modelo.addVars(vazao_da_bomba,vtype = GRB.CONTINUOUS, name = "Vjt")

    Wjlt = modelo.addVars(vazao_da_bomba_para_reservatorio,vtype = GRB.CONTINUOUS, name = "Wjlt")

    Hjmin = modelo.addVar(volume_minimo_reservatorio ,vtype = GRB.CONTINUOUS, name = "Hjmin")

    Hjmax = modelo.addVar(volume_maximo_reservatorio ,vtype = GRB.CONTINUOUS, name = "Hjmax")

    Hjzero = modelo.addVar(volume_do_reservatorio_inicio ,vtype = GRB.CONTINUOUS, name = "Hjzero")

    #talvez não use Gama
    #Restricao 9
    GAMAjlt = modelo.addVars(custo_transferir_agua,vtype = GRB.CONTINUOUS, name = "GAMAjlt")
    #Restricao 9
    Xjzero = modelo.addVar(estado_inicial_da_bomba ,vtype = GRB.BINARY, name = "Xjzero")

    Ijt = modelo.addVar(volume_do_reservatorio_final_do_periodo_t ,vtype = GRB.CONTINUOUS, name = "Ijt")

    Xjt = modelo.addVars(fracao_de_t,vtype = GRB.CONTINUOUS, name = "Xjt")


    #Objetivo
    modelo.setObjective( quicksum(Ctj[t]*Xjt[t] + SCjt[t]*ALFAjt[t]  for t in tempo) , GRB.MINIMIZE) 

    # restricao 2 do modelo

    modelo.addConstrs(Ijt = Ijt[t-1] + Vjt[t] + Xjt[t] - quicksum(Wjlt[t] for t in tempo) - "demandadocentroconsumidor"))
    # restricao 3 do modelo
    modelo.addConstrs(Xjt[t] <= Yjt[t]  for t in tempo)

    #restricao 4 do modelo
    modelo.addConstrs(ALFAjt[t]  >= (Yjt[t] - Xjt[t-1])  for t in tempo)

    #restricao 5 do modelo
    modelo.addConstrs(Xjt[t] <= Yjt[t]  for t in tempo)
        #GRB.LESS_EQUAL
    #restricao 6 do modelo
    modelo.addConstrs(Hjmin,GRB.LESS_EQUAL,Ijt[t],GRB.LESS_EQUAL,Hjmax  for t in tempo)

    #restricao 7 do modelo
    modelo.addConstrs(Xjt > 0)

    #restricao 8 do modelo
    modelo.addConstrs(Xjzero = fracao_de_t)
    #restricao 9 do modelo
    modelo.addConstrs(Ijt[0] = Hjzero)







    #Restricao


    #RUN
    modelo.optimize()

    print('')
    print('Optimization complete')
    #Printar Resultados
    for v in m.getVars():
        print('Obj: %g' % m.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))