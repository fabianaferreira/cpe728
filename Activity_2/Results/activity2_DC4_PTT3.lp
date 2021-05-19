\* Minimize_Max_Delay *\
Minimize
Cost: 100 X_DC_1_PTT_1 + 150 X_DC_1_PTT_2 + 225 X_DC_1_PTT_3
 + 125 X_DC_2_PTT_1 + 100 X_DC_2_PTT_2 + 225 X_DC_2_PTT_3 + 400 X_DC_3_PTT_1
 + 200 X_DC_3_PTT_2 + 100 X_DC_3_PTT_3 + 50 X_DC_4_PTT_1 + 80 X_DC_4_PTT_2
 + 20 X_DC_4_PTT_3
Subject To
Activation_PTT_PTT_1: - X_DC_1_PTT_1 - X_DC_2_PTT_1 - X_DC_3_PTT_1
 - X_DC_4_PTT_1 + Y_PTT_1 >= 0
Activation_PTT_PTT_2: - X_DC_1_PTT_2 - X_DC_2_PTT_2 - X_DC_3_PTT_2
 - X_DC_4_PTT_2 + Y_PTT_2 >= 0
Activation_PTT_PTT_3: - X_DC_1_PTT_3 - X_DC_2_PTT_3 - X_DC_3_PTT_3
 - X_DC_4_PTT_3 + Y_PTT_3 >= 0
Budget_Restriction: 100 X_DC_1_PTT_1 + 150 X_DC_1_PTT_2 + 225 X_DC_1_PTT_3
 + 125 X_DC_2_PTT_1 + 100 X_DC_2_PTT_2 + 225 X_DC_2_PTT_3 + 400 X_DC_3_PTT_1
 + 200 X_DC_3_PTT_2 + 100 X_DC_3_PTT_3 + 50 X_DC_4_PTT_1 + 80 X_DC_4_PTT_2
 + 20 X_DC_4_PTT_3 + 6000 Y_PTT_1 + 8000 Y_PTT_2 + 8000 Y_PTT_3 <= 100000
Capacity_PTT_1: 16000 X_DC_1_PTT_1 + 12000 X_DC_2_PTT_1 + 30000 X_DC_3_PTT_1
 + 20000 X_DC_4_PTT_1 <= 20000
Capacity_PTT_2: 16000 X_DC_1_PTT_2 + 12000 X_DC_2_PTT_2 + 30000 X_DC_3_PTT_2
 + 20000 X_DC_4_PTT_2 <= 15000
Capacity_PTT_3: 16000 X_DC_1_PTT_3 + 12000 X_DC_2_PTT_3 + 30000 X_DC_3_PTT_3
 + 20000 X_DC_4_PTT_3 <= 21000
DC_Restriction_DC_1: X_DC_1_PTT_1 + X_DC_1_PTT_2 + X_DC_1_PTT_3 = 1
DC_Restriction_DC_2: X_DC_2_PTT_1 + X_DC_2_PTT_2 + X_DC_2_PTT_3 = 1
DC_Restriction_DC_3: X_DC_3_PTT_1 + X_DC_3_PTT_2 + X_DC_3_PTT_3 = 1
DC_Restriction_DC_4: X_DC_4_PTT_1 + X_DC_4_PTT_2 + X_DC_4_PTT_3 = 1
Delay_Restriction_DC_1_PTT_1: 2 X_DC_1_PTT_1 <= 2
Delay_Restriction_DC_1_PTT_2: 15 X_DC_1_PTT_2 <= 15
Delay_Restriction_DC_1_PTT_3: 20 X_DC_1_PTT_3 <= 20
Delay_Restriction_DC_2_PTT_1: 2 X_DC_2_PTT_1 <= 2
Delay_Restriction_DC_2_PTT_2: 8 X_DC_2_PTT_2 <= 8
Delay_Restriction_DC_2_PTT_3: 16 X_DC_2_PTT_3 <= 16
Delay_Restriction_DC_3_PTT_1: 5 X_DC_3_PTT_1 <= 5
Delay_Restriction_DC_3_PTT_2: 10 X_DC_3_PTT_2 <= 10
Delay_Restriction_DC_3_PTT_3: 100 X_DC_3_PTT_3 <= 100
Delay_Restriction_DC_4_PTT_1: 8 X_DC_4_PTT_1 <= 8
Delay_Restriction_DC_4_PTT_2: 15 X_DC_4_PTT_2 <= 15
Delay_Restriction_DC_4_PTT_3: 20 X_DC_4_PTT_3 <= 20
Bounds
0 <= X_DC_1_PTT_1
0 <= X_DC_1_PTT_2
0 <= X_DC_1_PTT_3
0 <= X_DC_2_PTT_1
0 <= X_DC_2_PTT_2
0 <= X_DC_2_PTT_3
0 <= X_DC_3_PTT_1
0 <= X_DC_3_PTT_2
0 <= X_DC_3_PTT_3
0 <= X_DC_4_PTT_1
0 <= X_DC_4_PTT_2
0 <= X_DC_4_PTT_3
0 <= Y_PTT_1
0 <= Y_PTT_2
0 <= Y_PTT_3
Generals
X_DC_1_PTT_1
X_DC_1_PTT_2
X_DC_1_PTT_3
X_DC_2_PTT_1
X_DC_2_PTT_2
X_DC_2_PTT_3
X_DC_3_PTT_1
X_DC_3_PTT_2
X_DC_3_PTT_3
X_DC_4_PTT_1
X_DC_4_PTT_2
X_DC_4_PTT_3
Y_PTT_1
Y_PTT_2
Y_PTT_3
End
