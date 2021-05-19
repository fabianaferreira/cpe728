"""
Activity 2: Facility Location
Author: Fabiana Ferreira Fonseca
PEE - COPPE/UFRJ
2021.1
"""
from pulp import *

# ------- Parameters -------
# DCs
dc_list = ["DC_1","DC_2", "DC_3", "DC_4"]
# PTTs
ptt_list = ["PTT_1","PTT_2","PTT_3"]
#PTTs capacity
cap_ptts = {"PTT_1": 20000, "PTT_2": 15000, "PTT_3": 21000}
# DCs traffic
traffic_dcs = {"DC_1": 16000, "DC_2": 12000, "DC_3": 30000, "DC_4": 20000}
#Costs - DC x PTT
cost_matrix = [ [100, 150, 225],[125, 100, 225], [400, 200, 100], [50, 80, 20] ]
# List to dictionary
costs = makeDict([dc_list,ptt_list], cost_matrix, 0)
# Fixed cost, which is used if the PTT is activated
fixed_costs = {"PTT_1": 1500, "PTT_2": 2000, "PTT_3": 2000}
# Delay matrix (it's defined in ms) - DC x PTT
delay_matrix = [ [2, 15, 20], [2, 8, 16], [5, 10, 100], [8, 15, 20] ]
# List to dictionary
delays = makeDict([dc_list, ptt_list], delay_matrix, 0)

# Budget definition (unit is the country's currency, I'm using BRL)
budget = 100000

# Cost reduction/minimization problem
prob = LpProblem("Minimize_Max_Delay",LpMinimize)

# All the possible combinations between DCs and PTTs
x_variables = LpVariable.dicts("X",(dc_list, ptt_list), 0, None, LpInteger)

# If PTT is going to be activated
y_variables = LpVariable.dicts("Y", ptt_list, 0, None, LpInteger)

# Tuples (DC_i,PTT_j)
dc_ptt_pairs = [(dc,ptt) for dc in dc_list for ptt in ptt_list]

# Objective function
prob += lpSum([costs[dc][ptt]*x_variables[dc][ptt] for (dc,ptt) in dc_ptt_pairs]), "Cost"

# Delay restriction
for dc, ptt in dc_ptt_pairs:
    current_delay = delays[dc][ptt]
    current_x_variable = x_variables[dc][ptt]
    prob += current_delay*current_x_variable <= current_delay, "Delay_Restriction_%s_%s"%(dc, ptt)

# Yj restriction
for ptt in ptt_list:
    prob += [x_variables[dc][ptt] for dc in dc_list] <= y_variables[ptt], "Activation_PTT_%s"%ptt

# PTTs' restrictions
for ptt in ptt_list:
    prob += lpSum([x_variables[dc][ptt]*traffic_dcs[dc] for dc in dc_list]) <= cap_ptts[ptt], "Capacity_%s"%ptt

# DCs restrictions (each DC has to use only one PTT)
for dc in dc_list:
    prob += lpSum([x_variables[dc][ptt] for ptt in ptt_list]) == 1, "DC_Restriction_%s"%dc

# Fixed costs depend on the PTTs
cost_restriction = ""
for dc, ptt in dc_ptt_pairs:
    cost_restriction += lpSum(costs[dc][ptt]*x_variables[dc][ptt] + y_variables[ptt]*fixed_costs[ptt])
prob += cost_restriction <= budget, "Budget_Restriction"

prob.writeLP("activity2_DC4_PTT3.lp")
prob.solve()

# Logging
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Result
print("Smallest delay sum = ", value(prob.objective))
