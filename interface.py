#from gurobipy import *
import traceback
import openPanilhas, leitorDePanilha
try:
    l = openPanilhas.getPlanilhas()
    for x in range(len(l)):
        leitorDePanilha.getValeus(l[x])
except AttributeError:
    print("Algum erro")
    traceback.print_exc()