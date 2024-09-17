import csv
import math
from ast import literal_eval 
with open('OTIDs.csv', newline='') as otids:
    reader = csv.reader(otids)
    otids_list = list(reader)
file = open('ACE combos.txt', 'a')

#TODO: just copy and paste the whole string of hex data (maybe can do int?) and substring it to get the data instead of doing individual copy pastes
enemy_list = ["Rick Wurmple 1-2", "Allen Poochyena", "Allen Taillow", "Tiana Zigzagoon 1-2", 
              "Billy Seedot", "Billy Taillow", "Winston Zigzagoon", "Lyle Wurmple 1-6", "James Nincada", "Cindy Zigzagoon", "Rick Wurmple 1-2 Test"]

enemy_dict = {
            "Rick Wurmple 1-2": 
              [562056,
               2078585799 ^ 2078585573,
                2078585509 ^ 2078585573,
                  2078602469 ^ 2078585573,
                    2075505348 ^ 2078585573,
                      2078585573 ^ 2078585573,
                        2078579398 ^ 2078585573,
                          2078585573 ^ 2078585573,
                            2078585573 ^ 2078585573,
                              2078585573 ^ 2078585573,
                                1533060069 ^ 2078585573,
                                  2078585573 ^ 2078585573,
                                    2078585573 ^ 2078585573],
              #"Rick Wurmple 1-2 Test": 
              #[(int('889308004C7EF9C92E7FF9C96E39F9C94F7FA8C96E7FF9C94D57F9C96E7FF9C96E7FF9C96E7FF9C96E6E7DE96E7FF9C96E7FF9C9'[i*8:(i+1)*8], 16) ^ int('6E7FF9C9', 16)) for i in range(13) ],
        "Allen Poochyena": 
              [704136,
               2714105353 ^ 2714105623,
                2714105706 ^ 2714105623,
                  2714087703 ^ 2714105623,
                    2694182710 ^ 2714105623,
                      2714105623 ^ 2714105623,
                        2714099508 ^ 2714105623,
                          2714105623 ^ 2714105623,
                            2714105623 ^ 2714105623,
                              2714105623 ^ 2714105623,
                                2168514071 ^ 2714105623,
                                  2714105623 ^ 2714105623,
                                    2714105623 ^ 2714105623],
        "Allen Taillow": 
              [1310344,
               3685542808 ^ 3685542808,
                3685542808 ^ 3685542808,
                  3685542808 ^ 3685542808,
                    4214225560 ^ 3685542808,
                      3685542808 ^ 3685542808,
                        3685542808 ^ 3685542808,
                          3685542568 ^ 3685542808,
                            3685542817 ^ 3685542808,
                              3685526936 ^ 3685542808,
                                3682724824 ^ 3685542808,
                                  3685542808 ^ 3685542808,
                                    3685532603 ^ 3685542808],
        "Tiana Zigzagoon 1-2": 
              [708984,
               2111133315 ^ 2111133603,
                2111133667 ^ 2111133603,
                  2111115683 ^ 2111133603,
                    2113427330 ^ 2111133603,
                      2111133603 ^ 2111133603,
                        2111143808 ^ 2111133603,
                          2111133603 ^ 2111133603,
                            2111133603 ^ 2111133603,
                              2111133603 ^ 2111133603,
                                1565607587 ^ 2111133603,
                                  2111133603 ^ 2111133603,
                                    2111133603 ^ 2111133603],
        "Billy Seedot": 
              [556680,
               1210673977 ^ 1210673683,
                1210673824 ^ 1210673683,
                  1210657811 ^ 1210673683,
                    1212377702 ^ 1210673683,
                      1210673683 ^ 1210673683,
                        1210676249 ^ 1210673683,
                          1210673683 ^ 1210673683,
                            1210673683 ^ 1210673683,
                              1210673683 ^ 1210673683,
                                1756330259 ^ 1210673683,
                                  1210673683 ^ 1210673683,
                                    1210673683 ^ 1210673683],
            "Billy Taillow": 
              [1166984,
               93776316 ^ 96201212,
                98167176 ^ 96201212,
                  463847903 ^ 96201212,
                    96201212 ^ 96201212,
                      96201212 ^ 96201212,
                        96201212 ^ 96201212,
                          96200908 ^ 96201212,
                            96200902 ^ 96201212,
                              96186364 ^ 96201212,
                                2771647228 ^ 96201212,
                                  96201212 ^ 96201212,
                                    96201212 ^ 96201212], 
            "Winston Zigzagoon": 
              [821896,
               1442059782 ^ 1442059782,
                1442059782 ^ 1442059782,
                  1442059782 ^ 1442059782,
                    1970472198 ^ 1442059782,
                      1442059782 ^ 1442059782,
                        1442059782 ^ 1442059782,
                          1436161830 ^ 1442059782,
                            1442060113 ^ 1442059782,
                              1442074630 ^ 1442059782,
                                1440290343 ^ 1442059782,
                                  1442059809 ^ 1442059782,
                                    1441414693 ^ 1442059782],
              "Lyle Wurmple 1-6":
              [int('88A00800', 16),
               int('30557DF6', 16) ^ 810909174,
                int('30557DF6', 16) ^ 810909174,
                  int('30557DF6', 16) ^ 810909174,
                    int('306EFE56', 16) ^ 810909174,
                      int('30557DF6', 16) ^ 810909174,
                        int('30557DF6', 16) ^ 810909174,
                          int('12547DF6', 16) ^ 810909174,
                            int('2B557DF6', 16) ^ 810909174,
                              int('30137DF6', 16) ^ 810909174,
                                int('11552CF6', 16) ^ 810909174,
                                  int('30557DF6', 16) ^ 810909174,
                                    int('137D7DF6', 16) ^ 810909174]  ,
              "James Nincada":
              [int('88160900', 16),
               int('68282FFA', 16) ^ 1646806522,
                int('EF2845FA', 16) ^ 1646806522,
                  int('41364AFA', 16) ^ 1646806522,
                    int('622845FA', 16) ^ 1646806522,
                      int('622845FA', 16) ^ 1646806522,
                        int('622845FA', 16) ^ 1646806522,
                          int('4F2945FA', 16) ^ 1646806522,
                            int('CC2B45FA', 16) ^ 1646806522,
                              int('626E45FA', 16) ^ 1646806522,
                                int('6213CD5A', 16) ^ 1646806522,
                                  int('622845FA', 16) ^ 1646806522,
                                    int('622845FA', 16) ^ 1646806522]     ,
              "Cindy Zigzagoon":
              [int('78DB0A00', 16),
               int('FE4D41E4', 16) ^ int('22250000', 16),
                int('FE4D41E4', 16) ^ int('22250000', 16),
                  int('FE4D41E4', 16) ^ int('22250000', 16),
                    int('FE5EC644', 16) ^ int('22250000', 16),
                      int('FE4D41E4', 16) ^ int('22250000', 16),
                        int('FE4D41E4', 16) ^ int('22250000', 16),
                          int('DE4C2FE4', 16) ^ int('22250000', 16),
                            int('A94C41E4', 16) ^ int('22250000', 16),
                              int('FE0B41E4', 16) ^ int('22250000', 16),
                                int('DF4D6CE4', 16) ^ int('22250000', 16),
                                  int('D94D41E4', 16) ^ int('22250000', 16),
                                    int('DD655FE4', 16) ^ int('22250000', 16)]                                                             
            }
print(enemy_dict)
#int(bytes(reversed(bytearray.fromhex("DC02586C"))).hex(), 16) ^ int(bytes(reversed(bytearray.fromhex("FE03586C"))).hex(),16)
#must convert everything to little endian including PID
test_data = "889308005491506CD1CFCCC7CAC6BFFF00000202BBFFFFFFFFFFFF007BA10000FE03586C9C02586CDC44586CFD02096CDC02586CFF2A586CDC02586CDC02586CDC02586CDC13DC4CDC02586CDC02586C"
for i in enemy_list:
    enemy_dict[i] = []
    #add PID here
    enemy_dict[i].append(int(bytes(reversed(bytearray.fromhex(test_data[0:8]))).hex(), 16))
    for j in range(12):
      enemy_dict[i].append(int(bytes(reversed(bytearray.fromhex(test_data[(j+8)*8:(j+9)*8]))).hex(), 16) ^ int(bytes(reversed(bytearray.fromhex("DC02586C"))).hex(),16))

data_order = {0: 'GAEM',	6: 'AGEM', 	12: 'EGAM', 18: 'MGAE',
1: 'GAME', 	7: 'AGME', 	13: 'EGMA',  	19: 'MGEA',
2: 'GEAM', 	8: 'AEGM', 	14: 'EAGM', 	20: 'MAGE',
3: 'GEMA', 	9: 'AEMG',	15: 'EAMG', 	21: 'MAEG',
4: 'GMAE', 	10: 'AMGE', 16: 'EMGA', 	22: 'MEGA',
5: 'GMEA', 	11: 'AMEG',	17: 'EMAG', 	23: 'MEAG' }

#Shroomish Decrypted Data
'''
data1 = 306
data2 = 967
data3 = 17920
data4 = 2162759
data5 = 4784206
data6 = 169747220
data7 = 0
data8 = 0
data9 = 0
data10 = 2693537792
data11 = 0
data12 = 0
pid = 1321080
'''
print(enemy_dict["Rick Wurmple 1-2"])
print(enemy_dict["Rick Wurmple 1-2 Test"])
exit()
example_key = 2157728869
# Wurmple Decrypted Data
data1 = 2160940100 ^ example_key
data2 = 2157728869 ^ example_key
data3 = 2157739078 ^ example_key
data4 = 2157728869 ^ example_key
data5 = 2157728869 ^ example_key
data6 = 2157728869 ^ example_key
data7 = 2157729095 ^ example_key
data8 = 2157728805 ^ example_key
data9 = 2157711973 ^ example_key
data10 = 538461541 ^ example_key
data11 = 2157728869 ^ example_key
data12 = 2157728869 ^ example_key
#Note: PID actually doesn’t matter, as it gets used for the original and new decryption keys, cancelling each other out
pid = 1321080
valid_combinations = []
#print(otids_list[0])

 
for i in range(4000, 5000):
    player_key = pid ^ (literal_eval(f"{int(otids_list[i][2]):#0{6}x}" + f"{int(otids_list[i][1]):#0{6}x}"[2::]))
    #print("Player frame " + str(i-1) + " Player Key: " + str(player_key))
    for j in range(700, 3700):

        enemy_key = pid ^ (literal_eval(f"{int(otids_list[j][1]):#0{6}x}" + f"{int(otids_list[j][2]):#0{6}x}"[2::]))
        for enemy_mon in enemy_list:
            if (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'GAEM':
                #normalize around 0. GAEM
                #TODO: Replace this with looping through the string or something
                data1 = enemy_dict[enemy_mon][1]
                data2 = enemy_dict[enemy_mon][2]
                data3 = enemy_dict[enemy_mon][3]
                data4 = enemy_dict[enemy_mon][4]
                data5 = enemy_dict[enemy_mon][5]
                data6 = enemy_dict[enemy_mon][6]
                data7 = enemy_dict[enemy_mon][7]
                data8 = enemy_dict[enemy_mon][8]
                data9 = enemy_dict[enemy_mon][9]
                data10 = enemy_dict[enemy_mon][10]
                data11 = enemy_dict[enemy_mon][11]
                data12 = enemy_dict[enemy_mon][12]
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'GAME':
                data1 = enemy_dict[enemy_mon][1]
                data2 = enemy_dict[enemy_mon][2]
                data3 = enemy_dict[enemy_mon][3]
                data4 = enemy_dict[enemy_mon][4]
                data5 = enemy_dict[enemy_mon][5]
                data6 = enemy_dict[enemy_mon][6]
                data7 = enemy_dict[enemy_mon][10]
                data8 = enemy_dict[enemy_mon][11]
                data9 = enemy_dict[enemy_mon][12]
                data10 = enemy_dict[enemy_mon][7]
                data11 = enemy_dict[enemy_mon][8]
                data12 = enemy_dict[enemy_mon][9]   
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'GEAM':
                data1 = enemy_dict[enemy_mon][1]
                data2 = enemy_dict[enemy_mon][2]
                data3 = enemy_dict[enemy_mon][3]
                data4 = enemy_dict[enemy_mon][7]
                data5 = enemy_dict[enemy_mon][8]
                data6 = enemy_dict[enemy_mon][9]
                data7 = enemy_dict[enemy_mon][4]
                data8 = enemy_dict[enemy_mon][5]
                data9 = enemy_dict[enemy_mon][6]
                data10 = enemy_dict[enemy_mon][10]
                data11 = enemy_dict[enemy_mon][11]
                data12 = enemy_dict[enemy_mon][12]     
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'GEMA':
                data1 = enemy_dict[enemy_mon][1]
                data2 = enemy_dict[enemy_mon][2]
                data3 = enemy_dict[enemy_mon][3]
                data4 = enemy_dict[enemy_mon][10]
                data5 = enemy_dict[enemy_mon][11]
                data6 = enemy_dict[enemy_mon][12]
                data7 = enemy_dict[enemy_mon][4]
                data8 = enemy_dict[enemy_mon][5]
                data9 = enemy_dict[enemy_mon][6]
                data10 = enemy_dict[enemy_mon][7]
                data11 = enemy_dict[enemy_mon][8]
                data12 = enemy_dict[enemy_mon][9]    
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'GMAE':
                data1 = enemy_dict[enemy_mon][1]
                data2 = enemy_dict[enemy_mon][2]
                data3 = enemy_dict[enemy_mon][3]
                data4 = enemy_dict[enemy_mon][7]
                data5 = enemy_dict[enemy_mon][8]
                data6 = enemy_dict[enemy_mon][9]
                data7 = enemy_dict[enemy_mon][10]
                data8 = enemy_dict[enemy_mon][11]
                data9 = enemy_dict[enemy_mon][12]
                data10 = enemy_dict[enemy_mon][4]
                data11 = enemy_dict[enemy_mon][5]
                data12 = enemy_dict[enemy_mon][6]    
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'GMEA':
                data1 = enemy_dict[enemy_mon][1]
                data2 = enemy_dict[enemy_mon][2]
                data3 = enemy_dict[enemy_mon][3]
                data4 = enemy_dict[enemy_mon][10]
                data5 = enemy_dict[enemy_mon][11]
                data6 = enemy_dict[enemy_mon][12]
                data7 = enemy_dict[enemy_mon][7]
                data8 = enemy_dict[enemy_mon][8]
                data9 = enemy_dict[enemy_mon][9]
                data10 = enemy_dict[enemy_mon][4]
                data11 = enemy_dict[enemy_mon][5]
                data12 = enemy_dict[enemy_mon][6]    
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'AGEM':
                data1 = enemy_dict[enemy_mon][4]
                data2 = enemy_dict[enemy_mon][5]
                data3 = enemy_dict[enemy_mon][6]
                data4 = enemy_dict[enemy_mon][1]
                data5 = enemy_dict[enemy_mon][2]
                data6 = enemy_dict[enemy_mon][3]
                data7 = enemy_dict[enemy_mon][7]
                data8 = enemy_dict[enemy_mon][8]
                data9 = enemy_dict[enemy_mon][9]
                data10 = enemy_dict[enemy_mon][10]
                data11 = enemy_dict[enemy_mon][11]
                data12 = enemy_dict[enemy_mon][12]  
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'AGME':
                data1 = enemy_dict[enemy_mon][4]
                data2 = enemy_dict[enemy_mon][5]
                data3 = enemy_dict[enemy_mon][6]
                data4 = enemy_dict[enemy_mon][1]
                data5 = enemy_dict[enemy_mon][2]
                data6 = enemy_dict[enemy_mon][3]
                data7 = enemy_dict[enemy_mon][10]
                data8 = enemy_dict[enemy_mon][11]
                data9 = enemy_dict[enemy_mon][12]
                data10 = enemy_dict[enemy_mon][7]
                data11 = enemy_dict[enemy_mon][8]
                data12 = enemy_dict[enemy_mon][9]  
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'AEGM':
                data1 = enemy_dict[enemy_mon][7]
                data2 = enemy_dict[enemy_mon][8]
                data3 = enemy_dict[enemy_mon][9]
                data4 = enemy_dict[enemy_mon][1]
                data5 = enemy_dict[enemy_mon][2]
                data6 = enemy_dict[enemy_mon][3]
                data7 = enemy_dict[enemy_mon][4]
                data8 = enemy_dict[enemy_mon][5]
                data9 = enemy_dict[enemy_mon][6]
                data10 = enemy_dict[enemy_mon][10]
                data11 = enemy_dict[enemy_mon][11]
                data12 = enemy_dict[enemy_mon][12]  
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'AEMG':
                data1 = enemy_dict[enemy_mon][10]
                data2 = enemy_dict[enemy_mon][11]
                data3 = enemy_dict[enemy_mon][12]
                data4 = enemy_dict[enemy_mon][1]
                data5 = enemy_dict[enemy_mon][2]
                data6 = enemy_dict[enemy_mon][3]
                data7 = enemy_dict[enemy_mon][4]
                data8 = enemy_dict[enemy_mon][5]
                data9 = enemy_dict[enemy_mon][6]
                data10 = enemy_dict[enemy_mon][7]
                data11 = enemy_dict[enemy_mon][8]
                data12 = enemy_dict[enemy_mon][9]  
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'AMGE':
                data1 = enemy_dict[enemy_mon][7]
                data2 = enemy_dict[enemy_mon][8]
                data3 = enemy_dict[enemy_mon][9]
                data4 = enemy_dict[enemy_mon][1]
                data5 = enemy_dict[enemy_mon][2]
                data6 = enemy_dict[enemy_mon][3]
                data7 = enemy_dict[enemy_mon][10]
                data8 = enemy_dict[enemy_mon][11]
                data9 = enemy_dict[enemy_mon][12]
                data10 = enemy_dict[enemy_mon][4]
                data11 = enemy_dict[enemy_mon][5]
                data12 = enemy_dict[enemy_mon][6]
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'AMEG':
                data1 = enemy_dict[enemy_mon][10]
                data2 = enemy_dict[enemy_mon][11]
                data3 = enemy_dict[enemy_mon][12]
                data4 = enemy_dict[enemy_mon][1]
                data5 = enemy_dict[enemy_mon][2]
                data6 = enemy_dict[enemy_mon][3]
                data7 = enemy_dict[enemy_mon][7]
                data8 = enemy_dict[enemy_mon][8]
                data9 = enemy_dict[enemy_mon][9]
                data10 = enemy_dict[enemy_mon][4]
                data11 = enemy_dict[enemy_mon][5]
                data12 = enemy_dict[enemy_mon][6]   
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'EGAM':
                data1 = enemy_dict[enemy_mon][4]
                data2 = enemy_dict[enemy_mon][5]
                data3 = enemy_dict[enemy_mon][6]
                data4 = enemy_dict[enemy_mon][7]
                data5 = enemy_dict[enemy_mon][8]
                data6 = enemy_dict[enemy_mon][9]
                data7 = enemy_dict[enemy_mon][1]
                data8 = enemy_dict[enemy_mon][2]
                data9 = enemy_dict[enemy_mon][3]
                data10 = enemy_dict[enemy_mon][10]
                data11 = enemy_dict[enemy_mon][11]
                data12 = enemy_dict[enemy_mon][12]   
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'EGMA':
                data1 = enemy_dict[enemy_mon][4]
                data2 = enemy_dict[enemy_mon][5]
                data3 = enemy_dict[enemy_mon][6]
                data4 = enemy_dict[enemy_mon][10]
                data5 = enemy_dict[enemy_mon][11]
                data6 = enemy_dict[enemy_mon][12]
                data7 = enemy_dict[enemy_mon][1]
                data8 = enemy_dict[enemy_mon][2]
                data9 = enemy_dict[enemy_mon][3]
                data10 = enemy_dict[enemy_mon][7]
                data11 = enemy_dict[enemy_mon][8]
                data12 = enemy_dict[enemy_mon][9]  
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'EAGM':
                data1 = enemy_dict[enemy_mon][7]
                data2 = enemy_dict[enemy_mon][8]
                data3 = enemy_dict[enemy_mon][9]
                data4 = enemy_dict[enemy_mon][4]
                data5 = enemy_dict[enemy_mon][5]
                data6 = enemy_dict[enemy_mon][6]
                data7 = enemy_dict[enemy_mon][1]
                data8 = enemy_dict[enemy_mon][2]
                data9 = enemy_dict[enemy_mon][3]
                data10 = enemy_dict[enemy_mon][10]
                data11 = enemy_dict[enemy_mon][11]
                data12 = enemy_dict[enemy_mon][12]       
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'EAMG':
                data1 = enemy_dict[enemy_mon][10]
                data2 = enemy_dict[enemy_mon][11]
                data3 = enemy_dict[enemy_mon][12]
                data4 = enemy_dict[enemy_mon][4]
                data5 = enemy_dict[enemy_mon][5]
                data6 = enemy_dict[enemy_mon][6]
                data7 = enemy_dict[enemy_mon][1]
                data8 = enemy_dict[enemy_mon][2]
                data9 = enemy_dict[enemy_mon][3]
                data10 = enemy_dict[enemy_mon][7]
                data11 = enemy_dict[enemy_mon][8]
                data12 = enemy_dict[enemy_mon][9]   
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'EMGA':
                data1 = enemy_dict[enemy_mon][7]
                data2 = enemy_dict[enemy_mon][8]
                data3 = enemy_dict[enemy_mon][9]
                data4 = enemy_dict[enemy_mon][10]
                data5 = enemy_dict[enemy_mon][11]
                data6 = enemy_dict[enemy_mon][12]
                data7 = enemy_dict[enemy_mon][1]
                data8 = enemy_dict[enemy_mon][2]
                data9 = enemy_dict[enemy_mon][3]
                data10 = enemy_dict[enemy_mon][4]
                data11 = enemy_dict[enemy_mon][5]
                data12 = enemy_dict[enemy_mon][6]   
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'EMAG':
                data1 = enemy_dict[enemy_mon][10]
                data2 = enemy_dict[enemy_mon][11]
                data3 = enemy_dict[enemy_mon][12]
                data4 = enemy_dict[enemy_mon][7]
                data5 = enemy_dict[enemy_mon][8]
                data6 = enemy_dict[enemy_mon][9]
                data7 = enemy_dict[enemy_mon][1]
                data8 = enemy_dict[enemy_mon][2]
                data9 = enemy_dict[enemy_mon][3]
                data10 = enemy_dict[enemy_mon][4]
                data11 = enemy_dict[enemy_mon][5]
                data12 = enemy_dict[enemy_mon][6]  
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'MGAE':
                data1 = enemy_dict[enemy_mon][4]
                data2 = enemy_dict[enemy_mon][5]
                data3 = enemy_dict[enemy_mon][6]
                data4 = enemy_dict[enemy_mon][7]
                data5 = enemy_dict[enemy_mon][8]
                data6 = enemy_dict[enemy_mon][9]
                data7 = enemy_dict[enemy_mon][10]
                data8 = enemy_dict[enemy_mon][11]
                data9 = enemy_dict[enemy_mon][12]
                data10 = enemy_dict[enemy_mon][1]
                data11 = enemy_dict[enemy_mon][2]
                data12 = enemy_dict[enemy_mon][3]  
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'MGEA':
                data1 = enemy_dict[enemy_mon][4]
                data2 = enemy_dict[enemy_mon][5]
                data3 = enemy_dict[enemy_mon][6]
                data4 = enemy_dict[enemy_mon][10]
                data5 = enemy_dict[enemy_mon][11]
                data6 = enemy_dict[enemy_mon][12]
                data7 = enemy_dict[enemy_mon][7]
                data8 = enemy_dict[enemy_mon][8]
                data9 = enemy_dict[enemy_mon][9]
                data10 = enemy_dict[enemy_mon][1]
                data11 = enemy_dict[enemy_mon][2]
                data12 = enemy_dict[enemy_mon][3] 
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'MAGE':
                data1 = enemy_dict[enemy_mon][7]
                data2 = enemy_dict[enemy_mon][8]
                data3 = enemy_dict[enemy_mon][9]
                data4 = enemy_dict[enemy_mon][4]
                data5 = enemy_dict[enemy_mon][5]
                data6 = enemy_dict[enemy_mon][6]
                data7 = enemy_dict[enemy_mon][10]
                data8 = enemy_dict[enemy_mon][11]
                data9 = enemy_dict[enemy_mon][12]
                data10 = enemy_dict[enemy_mon][1]
                data11 = enemy_dict[enemy_mon][2]
                data12 = enemy_dict[enemy_mon][3]    
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'MAEG':
                data1 = enemy_dict[enemy_mon][10]
                data2 = enemy_dict[enemy_mon][11]
                data3 = enemy_dict[enemy_mon][12]
                data4 = enemy_dict[enemy_mon][4]
                data5 = enemy_dict[enemy_mon][5]
                data6 = enemy_dict[enemy_mon][6]
                data7 = enemy_dict[enemy_mon][7]
                data8 = enemy_dict[enemy_mon][8]
                data9 = enemy_dict[enemy_mon][9]
                data10 = enemy_dict[enemy_mon][1]
                data11 = enemy_dict[enemy_mon][2]
                data12 = enemy_dict[enemy_mon][3] 
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'MEGA':
                data1 = enemy_dict[enemy_mon][7]
                data2 = enemy_dict[enemy_mon][8]
                data3 = enemy_dict[enemy_mon][9]
                data4 = enemy_dict[enemy_mon][10]
                data5 = enemy_dict[enemy_mon][11]
                data6 = enemy_dict[enemy_mon][12]
                data7 = enemy_dict[enemy_mon][4]
                data8 = enemy_dict[enemy_mon][5]
                data9 = enemy_dict[enemy_mon][6]
                data10 = enemy_dict[enemy_mon][1]
                data11 = enemy_dict[enemy_mon][2]
                data12 = enemy_dict[enemy_mon][3]    
            elif (data_order[(enemy_dict[enemy_mon][0]) % 24]) == 'MEAG':
                data1 = enemy_dict[enemy_mon][10]
                data2 = enemy_dict[enemy_mon][11]
                data3 = enemy_dict[enemy_mon][12]
                data4 = enemy_dict[enemy_mon][7]
                data5 = enemy_dict[enemy_mon][8]
                data6 = enemy_dict[enemy_mon][9]
                data7 = enemy_dict[enemy_mon][4]
                data8 = enemy_dict[enemy_mon][5]
                data9 = enemy_dict[enemy_mon][6]
                data10 = enemy_dict[enemy_mon][1]
                data11 = enemy_dict[enemy_mon][2]
                data12 = enemy_dict[enemy_mon][3]                                                                                       
            for k in range(1, 13):
                #checking each pokeball
                data10 = int(format(data10, '#034b')[2:3] + format(k, '#06b')[2:] + format(data10, '#034b')[7:], 2)

                original_checksum = ((data1 % 65536) + math.trunc(data1/65536) + (data2 % 65536) + math.trunc(data2/65536) + (data3 % 65536)
                        + math.trunc(data3/65536) + (data4 % 65536) + math.trunc(data4/65536) + (data5 % 65536) + math.trunc(data5/65536)
                        + (data6 % 65536) + math.trunc(data6/65536) + (data7 % 65536) + math.trunc(data7/65536) + (data8 % 65536)
                        + math.trunc(data8/65536) + (data9 % 65536) + math.trunc(data9/65536) + (data10 % 65536) + math.trunc(data10/65536)
                        + (data11 % 65536) + math.trunc(data11/65536) + (data12 % 65536) + math.trunc(data12/65536))%65536


                new_checksum = ((player_key ^ enemy_key ^ data1 % 65536) + math.trunc((player_key ^ enemy_key ^ data1)/65536) + (player_key ^ enemy_key ^ data2 % 65536) + math.trunc((player_key ^ enemy_key ^ data2)/65536) + (player_key ^ enemy_key ^ data3 % 65536)
                + math.trunc((player_key ^ enemy_key ^ data3)/65536) + (player_key ^ enemy_key ^ data4 % 65536) + math.trunc((player_key ^ enemy_key ^ data4)/65536) + (player_key ^ enemy_key ^ data5 % 65536) + math.trunc((player_key ^ enemy_key ^ data5)/65536)
                + (player_key ^ enemy_key ^ data6 % 65536) + math.trunc((player_key ^ enemy_key ^ data6)/65536) + (player_key ^ enemy_key ^ data7 % 65536) + math.trunc((player_key ^ enemy_key ^ data7)/65536) + (player_key ^ enemy_key ^ data8 % 65536)
                + math.trunc((player_key ^ enemy_key ^ data8)/65536) + (player_key ^ enemy_key ^ data9 % 65536) + math.trunc((player_key ^ enemy_key ^ data9)/65536) + (player_key ^ enemy_key ^ data10 % 65536) + math.trunc((player_key ^ enemy_key ^ data10)/65536)
                + (player_key ^ enemy_key ^ data11 % 65536) + math.trunc((player_key ^ enemy_key ^ data11)/65536) + (player_key ^ enemy_key ^ data12 % 65536) + math.trunc((player_key ^ enemy_key ^ data12)/65536))%65536
                #print("Enemy frame " + str(j) + " Enemy Key: " + str(enemy_key) + " New Checksum: " + str(new_checksum))
                if new_checksum == original_checksum:
                    #valid_combinations.append([i-1, j-1])
                    #if ("0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83' or "0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83'):
                     #   print("ACE move found: " + str(i-1) + " " + str(j-1))
                      #  file.write("ACE move found: " + str(i-1) + " " + str(j-1))
                    #if (f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x0113'):
                    #    print("Eon Ticket found: " + str(i-1) + " " + str(j-1))
                    
                    print("Match Found! Player frame: " + str(i-1) + " Enemy Frame: " + str(j-1) + " Player TID/SID: " + otids_list[i][1] + " " + otids_list[i][2] + 
                        " Enemy TID/SID: " + otids_list[j][2] + " " + otids_list[j][1] 
                        + " Species: " + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] 
                    + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] 
                    + " Held Item: " + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] 
                    + " Moves: " + "0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6]
                        + " 0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] + " Pokeball: " + str(k)
                        + (" Egg: " + format(player_key ^ enemy_key ^ data11, '#034b')[3:4]) + " Enemy Mon: " + enemy_mon) 
                    break
                #if ((literal_eval(hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] )) < 440):
                    #print("VALID MON")
print("Done")
file.close()