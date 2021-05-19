"""
Activity 1: Facility Location
Author: Fabiana Ferreira Fonseca
PEE - COPPE/UFRJ
2021.1
"""
from pulp import *

# ------- Parameters -------
# Cost DC i -> PTT j
c_1_1 = 100
c_1_2 = 150
c_1_3 = 225
c_1_4 = 250
c_1_5 = 500
c_2_1 = 125
c_2_2 = 100
c_2_3 = 225
c_2_4 = 250
c_2_5 = 500
c_3_1 = 100
c_3_2 = 150
c_3_3 = 225
c_3_4 = 250
c_3_5 = 500
c_4_1 = 100
c_4_2 = 150
c_4_3 = 225
c_4_4 = 250
c_4_5 = 500
# PTT capacity
b_1 = 10000
b_2 = 15000
b_3 = 21000
b_4 = 25000
b_5 = 30000
# DC traffic
d_1 = 16000
d_2 = 12000
d_3 = 20000
d_4 = 18000

# Defines the cost reduction problem
prob = LpProblem("4_DCs_e_5_PTTs",LpMinimize)

x_1_1=LpVariable("X_DC_1_PTT_1",0,None,LpInteger)
x_1_2=LpVariable("X_DC_1_PTT_2",0,None,LpInteger)
x_1_3=LpVariable("X_DC_1_PTT_3",0,None,LpInteger)
x_1_4=LpVariable("X_DC_1_PTT_4",0,None,LpInteger)
x_1_5=LpVariable("X_DC_1_PTT_5",0,None,LpInteger)
x_2_1=LpVariable("X_DC_2_PTT_1",0,None,LpInteger)
x_2_2=LpVariable("X_DC_2_PTT_2",0,None,LpInteger)
x_2_3=LpVariable("X_DC_2_PTT_3",0,None,LpInteger)
x_2_4=LpVariable("X_DC_2_PTT_4",0,None,LpInteger)
x_2_5=LpVariable("X_DC_2_PTT_5",0,None,LpInteger)
x_3_1=LpVariable("X_DC_3_PTT_1",0,None,LpInteger)
x_3_2=LpVariable("X_DC_3_PTT_2",0,None,LpInteger)
x_3_3=LpVariable("X_DC_3_PTT_3",0,None,LpInteger)
x_3_4=LpVariable("X_DC_3_PTT_4",0,None,LpInteger)
x_3_5=LpVariable("X_DC_3_PTT_5",0,None,LpInteger)
x_4_1=LpVariable("X_DC_4_PTT_1",0,None,LpInteger)
x_4_2=LpVariable("X_DC_4_PTT_2",0,None,LpInteger)
x_4_3=LpVariable("X_DC_4_PTT_3",0,None,LpInteger)
x_4_4=LpVariable("X_DC_4_PTT_4",0,None,LpInteger)
x_4_5=LpVariable("X_DC_4_PTT_5",0,None,LpInteger)

# Objective function
prob += (
    c_1_1*x_1_1 + c_1_2*x_1_2 + c_1_3*x_1_3 + c_1_4*x_1_4 + c_1_5*x_1_5 + 
    c_2_1*x_2_1 + c_2_2*x_2_2 + c_2_3*x_2_3 + c_2_4*x_2_4 + c_2_5*x_2_5 +
    c_3_1*x_3_1 + c_3_2*x_3_2 + c_3_3*x_3_3 + c_3_4*x_3_4 + c_3_5*x_3_5 +
    c_4_1*x_4_1 + c_4_2*x_4_2 + c_4_3*x_4_3 + c_4_4*x_4_4 + c_4_5*x_4_5
) ,"Custo"

# PTTs' restrictions
prob += x_1_1 + x_2_1 + x_3_1 + x_4_1 <= b_1, "Capacidade_PTT_1"
prob += x_1_2 + x_2_2 + x_3_2 + x_4_2 <= b_2, "Capacidade_PTT_2"
prob += x_1_3 + x_2_3 + x_3_3 + x_4_3 <= b_3, "Capacidade_PTT_3"
prob += x_1_4 + x_2_4 + x_3_4 + x_4_4 <= b_4, "Capacidade_PTT_4"
prob += x_1_5 + x_2_5 + x_3_5 + x_4_5 <= b_5, "Capacidade_PTT_5"

# DCs restrictions
prob += x_1_1 + x_1_2 + x_1_3 + x_1_4 + x_1_5 == d_1, "Trafego_DC_1"
prob += x_2_1 + x_2_2 + x_2_3 + x_2_4 + x_2_5 == d_2, "Trafego_DC_2"
prob += x_3_1 + x_3_2 + x_3_3 + x_3_4 + x_3_5 == d_3, "Trafego_DC_3"
prob += x_4_1 + x_4_2 + x_4_3 + x_4_4 + x_4_5 == d_4, "Trafego_DC_4"

prob.writeLP("DC_PTT_Exercise1_Fabiana.lp")
prob.solve()

# Logging
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Result
print("O custo total da infraestrutura eh= ", value(prob.objective))
