#from gurobipy import *
import traceback
import openPanilhas, leitorDePanilha

l = openPanilhas.getPlanilhas()
for x in range(len(l)):
    leitorDePanilha.getValeus(l[x])