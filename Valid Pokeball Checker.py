import csv
import math
from ast import literal_eval 
with open('OTIDs.csv', newline='') as otids:
    reader = csv.reader(otids)
    otids_list = list(reader)
file = open('ACE combos.txt', 'a')
file.write('test')




enemy_list = ["Rick Wurmple 1", "Rick Wurmple 2", "Allen Poochyena", "Allen Taillow", "Tiana Zigzagoon 1", "Tiana Zigzagoon 2", "Billy Seedot", "Billy Taillow", "Winston Zigzagoon"]
enemy_dict = {
            "Rick Wurmple 1": 
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
        "Rick Wurmple 2": 
              [1123976,
               2160940100 ^ 2157728869,
                2157728869 ^ 2157728869,
                  2157739078 ^ 2157728869,
                    2157728869 ^ 2157728869,
                      2157728869 ^ 2157728869,
                        2157728869 ^ 2157728869,
                          2157729095 ^ 2157728869,
                            2157728805 ^ 2157728869,
                              2157711973 ^ 2157728869,
                                538461541 ^ 2157728869,
                                  2157728869 ^ 2157728869,
                                    2157728869 ^ 2157728869],
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
        "Tiana Zigzagoon 1": 
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
        "Tiana Zigzagoon 2": 
              [1417848,
               3692285076 ^ 3692285364,
                3692285428 ^ 3692285364,
                  3692268468 ^ 3692285364,
                    3695103381 ^ 3692285364,
                      3692285364 ^ 3692285364,
                        3692291479 ^ 3692285364,
                          3692285364 ^ 3692285364,
                            3692285364 ^ 3692285364,
                              3692285364 ^ 3692285364,
                                4237810868 ^ 3692285364,
                                  3692285364 ^ 3692285364,
                                    3692285364 ^ 3692285364],
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
               2827846186 ^ 2829091434,
                2831319582 ^ 2829091434,
                  3065948745 ^ 2829091434,
                    2829091434 ^ 2829091434,
                      2829091434 ^ 2829091434,
                        2829091434 ^ 2829091434,
                          2829091674 ^ 2829091434,
                            2829091664 ^ 2829091434,
                              2829108330 ^ 2829091434,
                                2284360042 ^ 2829091434,
                                  2829091434 ^ 2829091434,
                                    2829091434 ^ 2829091434], 
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
                                    1441414693 ^ 1442059782]                                                      
            }


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

 
print(data10)
for i in range(6750, 6850):
    player_key = pid ^ (literal_eval(f"{int(otids_list[i][2]):#0{6}x}" + f"{int(otids_list[i][1]):#0{6}x}"[2::]))
    #print("Player frame " + str(i-1) + " Player Key: " + str(player_key))
    for j in range(33000, 33800):

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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'GAME':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'GEAM':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'GEMA':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'GMAE':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'GMEA':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'AGEM':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'AGME':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'AEGM':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'AEMG':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'AMGE':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'AMEG':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'EGAM':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'EGMA':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'EAGM':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'EAMG':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'EMGA':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'EMAG':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'MGAE':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'MGEA':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'MAGE':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'MAEG':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'MEGA':
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
            elif ((enemy_dict[enemy_mon][0]) % 24) == 'MEAG':
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
                    if ("0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83' or "0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83'):
                        print("ACE move found: " + str(i-1) + " " + str(j-1))
                        file.write("ACE move found: " + str(i-1) + " " + str(j-1))
                    #if (f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x0113'):
                    #    print("Eon Ticket found: " + str(i-1) + " " + str(j-1))
                    
                    print("Match Found! Player frame: " + str(i-1) + " Enemy Frame: " + str(j-1) + " Player TID/SID: " + otids_list[i][1] + " " + otids_list[i][2] + 
                        " Enemy TID/SID: " + otids_list[j][2] + " " + otids_list[j][1] 
                        + " Species: " + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] 
                    + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] 
                    + " Held Item: " + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] 
                    + " Moves: " + "0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6]
                        + " 0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] + " Pokeball: " + str(k)
                        + (" Egg: " + format(player_key ^ enemy_key ^ data11, '#034b')[3:4]))
                    break
                #if ((literal_eval(hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] )) < 440):
                    #print("VALID MON")
print("Done")
file.close()