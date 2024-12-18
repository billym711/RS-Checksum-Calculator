import csv
import math
import time
t = time.time()
from ast import literal_eval 
with open('OTIDs.csv', newline='') as otids:
    reader = csv.reader(otids)
    otids_list = list(reader)
li = [i for i in range(339) if i < 226 or i > 288]
li.append(254)
li.append(255)
li.append(256)
li.append(257)
li.append(258)
for i in range(12):
    li.remove(i+121)
item_list = li
#SELECT VERSION
sapphire = True
otid_frame = 3001  
enemy_otid_frame = 8634  
#TODO: Add rematches, combine matching entries

enemy_data_list = [                [ "Colton Skitty 1", "886F09005B01342ECDC5C3CECED3FF0002000202BBFFFFFFFFFFFF00387D0000D36E3D2ED36E3D2ED36E3D2ED339AB8ED36E3D2ED36E3D2EE86FB62E954F3D2ED3283D2EC16FF12E6A6EEA2EC77A292B"],
                ]
enemy_dict = {              
            }

#int(bytes(reversed(bytearray.fromhex("DC02586C"))).hex(), 16) ^ int(bytes(reversed(bytearray.fromhex("FE03586C"))).hex(),16)
#must convert everything to little endian including PID
for i in enemy_data_list:
    enemy_dict[i[0]] = []
    #add PID here
    enemy_dict[i[0]].append(int(bytes(reversed(bytearray.fromhex(i[1][0:8]))).hex(), 16))
    for j in range(12):
      enemy_dict[i[0]].append(int(bytes(reversed(bytearray.fromhex(i[1][(j+8)*8:(j+9)*8]))).hex(), 16) ^ int(bytes(reversed(bytearray.fromhex(i[1][0:8]))).hex(), 16) ^ int(bytes(reversed(bytearray.fromhex(i[1][8:16]))).hex(), 16))

data_order = {0: 'GAEM',	6: 'AGEM', 	12: 'EGAM', 18: 'MGAE',
1: 'GAME', 	7: 'AGME', 	13: 'EGMA',  	19: 'MGEA',
2: 'GEAM', 	8: 'AEGM', 	14: 'EAGM', 	20: 'MAGE',
3: 'GEMA', 	9: 'AEMG',	15: 'EAMG', 	21: 'MAEG',
4: 'GMAE', 	10: 'AMGE', 16: 'EMGA', 	22: 'MEGA',
5: 'GMEA', 	11: 'AMEG',	17: 'EMAG', 	23: 'MEAG' }

data1 = 0
data2 = 0
data3 = 0
data4 = 0
data5 = 0
data6 = 0
data7 = 0
data8 = 0
data9 = 0
data10 = 0
data11 = 0
data12 = 0
#Note: PID actually doesn’t matter, as it gets used for the original and new decryption keys, cancelling each other out
pid = 1321080
valid_combinations = []
#print(otids_list[0])

def main():
    ############################################
    # Put your own TID/SID frame here (can find with PokeFinder)
    ############################################
    for i in range(otid_frame + 1, otid_frame + 2):
        player_key = pid ^ (literal_eval(f"{int(otids_list[i][2]):#0{6}x}" + f"{int(otids_list[i][1]):#0{6}x}"[2::]))
        #print("Player frame " + str(i-1) + " Player Key: " + str(player_key))
        #################################################
        # Put the range of frames you want to search for here
        #################################################
        for j in range(enemy_otid_frame + 1, enemy_otid_frame + 2):

            enemy_key = pid ^ (literal_eval(f"{int(otids_list[j][1]):#0{6}x}" + f"{int(otids_list[j][2]):#0{6}x}"[2::]))
            for enemy_mon in enemy_data_list:
                if (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'GAEM':
                    #normalize around 0. GAEM
                    #TODO: Replace this with looping through the string or something
                    data1 = enemy_dict[enemy_mon[0]][1]
                    data2 = enemy_dict[enemy_mon[0]][2]
                    data3 = enemy_dict[enemy_mon[0]][3]
                    data4 = enemy_dict[enemy_mon[0]][4]
                    data5 = enemy_dict[enemy_mon[0]][5]
                    data6 = enemy_dict[enemy_mon[0]][6]
                    data7 = enemy_dict[enemy_mon[0]][7]
                    data8 = enemy_dict[enemy_mon[0]][8]
                    data9 = enemy_dict[enemy_mon[0]][9]
                    data10 = enemy_dict[enemy_mon[0]][10]
                    data11 = enemy_dict[enemy_mon[0]][11]
                    data12 = enemy_dict[enemy_mon[0]][12]
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'GAME':
                    data1 = enemy_dict[enemy_mon[0]][1]
                    data2 = enemy_dict[enemy_mon[0]][2]
                    data3 = enemy_dict[enemy_mon[0]][3]
                    data4 = enemy_dict[enemy_mon[0]][4]
                    data5 = enemy_dict[enemy_mon[0]][5]
                    data6 = enemy_dict[enemy_mon[0]][6]
                    data7 = enemy_dict[enemy_mon[0]][10]
                    data8 = enemy_dict[enemy_mon[0]][11]
                    data9 = enemy_dict[enemy_mon[0]][12]
                    data10 = enemy_dict[enemy_mon[0]][7]
                    data11 = enemy_dict[enemy_mon[0]][8]
                    data12 = enemy_dict[enemy_mon[0]][9]   
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'GEAM':
                    data1 = enemy_dict[enemy_mon[0]][1]
                    data2 = enemy_dict[enemy_mon[0]][2]
                    data3 = enemy_dict[enemy_mon[0]][3]
                    data4 = enemy_dict[enemy_mon[0]][7]
                    data5 = enemy_dict[enemy_mon[0]][8]
                    data6 = enemy_dict[enemy_mon[0]][9]
                    data7 = enemy_dict[enemy_mon[0]][4]
                    data8 = enemy_dict[enemy_mon[0]][5]
                    data9 = enemy_dict[enemy_mon[0]][6]
                    data10 = enemy_dict[enemy_mon[0]][10]
                    data11 = enemy_dict[enemy_mon[0]][11]
                    data12 = enemy_dict[enemy_mon[0]][12]     
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'GEMA':
                    data1 = enemy_dict[enemy_mon[0]][1]
                    data2 = enemy_dict[enemy_mon[0]][2]
                    data3 = enemy_dict[enemy_mon[0]][3]
                    data4 = enemy_dict[enemy_mon[0]][10]
                    data5 = enemy_dict[enemy_mon[0]][11]
                    data6 = enemy_dict[enemy_mon[0]][12]
                    data7 = enemy_dict[enemy_mon[0]][4]
                    data8 = enemy_dict[enemy_mon[0]][5]
                    data9 = enemy_dict[enemy_mon[0]][6]
                    data10 = enemy_dict[enemy_mon[0]][7]
                    data11 = enemy_dict[enemy_mon[0]][8]
                    data12 = enemy_dict[enemy_mon[0]][9]    
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'GMAE':
                    data1 = enemy_dict[enemy_mon[0]][1]
                    data2 = enemy_dict[enemy_mon[0]][2]
                    data3 = enemy_dict[enemy_mon[0]][3]
                    data4 = enemy_dict[enemy_mon[0]][7]
                    data5 = enemy_dict[enemy_mon[0]][8]
                    data6 = enemy_dict[enemy_mon[0]][9]
                    data7 = enemy_dict[enemy_mon[0]][10]
                    data8 = enemy_dict[enemy_mon[0]][11]
                    data9 = enemy_dict[enemy_mon[0]][12]
                    data10 = enemy_dict[enemy_mon[0]][4]
                    data11 = enemy_dict[enemy_mon[0]][5]
                    data12 = enemy_dict[enemy_mon[0]][6]    
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'GMEA':
                    data1 = enemy_dict[enemy_mon[0]][1]
                    data2 = enemy_dict[enemy_mon[0]][2]
                    data3 = enemy_dict[enemy_mon[0]][3]
                    data4 = enemy_dict[enemy_mon[0]][10]
                    data5 = enemy_dict[enemy_mon[0]][11]
                    data6 = enemy_dict[enemy_mon[0]][12]
                    data7 = enemy_dict[enemy_mon[0]][7]
                    data8 = enemy_dict[enemy_mon[0]][8]
                    data9 = enemy_dict[enemy_mon[0]][9]
                    data10 = enemy_dict[enemy_mon[0]][4]
                    data11 = enemy_dict[enemy_mon[0]][5]
                    data12 = enemy_dict[enemy_mon[0]][6]    
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'AGEM':
                    data1 = enemy_dict[enemy_mon[0]][4]
                    data2 = enemy_dict[enemy_mon[0]][5]
                    data3 = enemy_dict[enemy_mon[0]][6]
                    data4 = enemy_dict[enemy_mon[0]][1]
                    data5 = enemy_dict[enemy_mon[0]][2]
                    data6 = enemy_dict[enemy_mon[0]][3]
                    data7 = enemy_dict[enemy_mon[0]][7]
                    data8 = enemy_dict[enemy_mon[0]][8]
                    data9 = enemy_dict[enemy_mon[0]][9]
                    data10 = enemy_dict[enemy_mon[0]][10]
                    data11 = enemy_dict[enemy_mon[0]][11]
                    data12 = enemy_dict[enemy_mon[0]][12]  
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'AGME':
                    data1 = enemy_dict[enemy_mon[0]][4]
                    data2 = enemy_dict[enemy_mon[0]][5]
                    data3 = enemy_dict[enemy_mon[0]][6]
                    data4 = enemy_dict[enemy_mon[0]][1]
                    data5 = enemy_dict[enemy_mon[0]][2]
                    data6 = enemy_dict[enemy_mon[0]][3]
                    data7 = enemy_dict[enemy_mon[0]][10]
                    data8 = enemy_dict[enemy_mon[0]][11]
                    data9 = enemy_dict[enemy_mon[0]][12]
                    data10 = enemy_dict[enemy_mon[0]][7]
                    data11 = enemy_dict[enemy_mon[0]][8]
                    data12 = enemy_dict[enemy_mon[0]][9]  
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'AEGM':
                    data1 = enemy_dict[enemy_mon[0]][7]
                    data2 = enemy_dict[enemy_mon[0]][8]
                    data3 = enemy_dict[enemy_mon[0]][9]
                    data4 = enemy_dict[enemy_mon[0]][1]
                    data5 = enemy_dict[enemy_mon[0]][2]
                    data6 = enemy_dict[enemy_mon[0]][3]
                    data7 = enemy_dict[enemy_mon[0]][4]
                    data8 = enemy_dict[enemy_mon[0]][5]
                    data9 = enemy_dict[enemy_mon[0]][6]
                    data10 = enemy_dict[enemy_mon[0]][10]
                    data11 = enemy_dict[enemy_mon[0]][11]
                    data12 = enemy_dict[enemy_mon[0]][12]  
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'AEMG':
                    data1 = enemy_dict[enemy_mon[0]][10]
                    data2 = enemy_dict[enemy_mon[0]][11]
                    data3 = enemy_dict[enemy_mon[0]][12]
                    data4 = enemy_dict[enemy_mon[0]][1]
                    data5 = enemy_dict[enemy_mon[0]][2]
                    data6 = enemy_dict[enemy_mon[0]][3]
                    data7 = enemy_dict[enemy_mon[0]][4]
                    data8 = enemy_dict[enemy_mon[0]][5]
                    data9 = enemy_dict[enemy_mon[0]][6]
                    data10 = enemy_dict[enemy_mon[0]][7]
                    data11 = enemy_dict[enemy_mon[0]][8]
                    data12 = enemy_dict[enemy_mon[0]][9]  
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'AMGE':
                    data1 = enemy_dict[enemy_mon[0]][7]
                    data2 = enemy_dict[enemy_mon[0]][8]
                    data3 = enemy_dict[enemy_mon[0]][9]
                    data4 = enemy_dict[enemy_mon[0]][1]
                    data5 = enemy_dict[enemy_mon[0]][2]
                    data6 = enemy_dict[enemy_mon[0]][3]
                    data7 = enemy_dict[enemy_mon[0]][10]
                    data8 = enemy_dict[enemy_mon[0]][11]
                    data9 = enemy_dict[enemy_mon[0]][12]
                    data10 = enemy_dict[enemy_mon[0]][4]
                    data11 = enemy_dict[enemy_mon[0]][5]
                    data12 = enemy_dict[enemy_mon[0]][6]
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'AMEG':
                    data1 = enemy_dict[enemy_mon[0]][10]
                    data2 = enemy_dict[enemy_mon[0]][11]
                    data3 = enemy_dict[enemy_mon[0]][12]
                    data4 = enemy_dict[enemy_mon[0]][1]
                    data5 = enemy_dict[enemy_mon[0]][2]
                    data6 = enemy_dict[enemy_mon[0]][3]
                    data7 = enemy_dict[enemy_mon[0]][7]
                    data8 = enemy_dict[enemy_mon[0]][8]
                    data9 = enemy_dict[enemy_mon[0]][9]
                    data10 = enemy_dict[enemy_mon[0]][4]
                    data11 = enemy_dict[enemy_mon[0]][5]
                    data12 = enemy_dict[enemy_mon[0]][6]   
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'EGAM':
                    data1 = enemy_dict[enemy_mon[0]][4]
                    data2 = enemy_dict[enemy_mon[0]][5]
                    data3 = enemy_dict[enemy_mon[0]][6]
                    data4 = enemy_dict[enemy_mon[0]][7]
                    data5 = enemy_dict[enemy_mon[0]][8]
                    data6 = enemy_dict[enemy_mon[0]][9]
                    data7 = enemy_dict[enemy_mon[0]][1]
                    data8 = enemy_dict[enemy_mon[0]][2]
                    data9 = enemy_dict[enemy_mon[0]][3]
                    data10 = enemy_dict[enemy_mon[0]][10]
                    data11 = enemy_dict[enemy_mon[0]][11]
                    data12 = enemy_dict[enemy_mon[0]][12]   
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'EGMA':
                    data1 = enemy_dict[enemy_mon[0]][4]
                    data2 = enemy_dict[enemy_mon[0]][5]
                    data3 = enemy_dict[enemy_mon[0]][6]
                    data4 = enemy_dict[enemy_mon[0]][10]
                    data5 = enemy_dict[enemy_mon[0]][11]
                    data6 = enemy_dict[enemy_mon[0]][12]
                    data7 = enemy_dict[enemy_mon[0]][1]
                    data8 = enemy_dict[enemy_mon[0]][2]
                    data9 = enemy_dict[enemy_mon[0]][3]
                    data10 = enemy_dict[enemy_mon[0]][7]
                    data11 = enemy_dict[enemy_mon[0]][8]
                    data12 = enemy_dict[enemy_mon[0]][9]  
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'EAGM':
                    data1 = enemy_dict[enemy_mon[0]][7]
                    data2 = enemy_dict[enemy_mon[0]][8]
                    data3 = enemy_dict[enemy_mon[0]][9]
                    data4 = enemy_dict[enemy_mon[0]][4]
                    data5 = enemy_dict[enemy_mon[0]][5]
                    data6 = enemy_dict[enemy_mon[0]][6]
                    data7 = enemy_dict[enemy_mon[0]][1]
                    data8 = enemy_dict[enemy_mon[0]][2]
                    data9 = enemy_dict[enemy_mon[0]][3]
                    data10 = enemy_dict[enemy_mon[0]][10]
                    data11 = enemy_dict[enemy_mon[0]][11]
                    data12 = enemy_dict[enemy_mon[0]][12]       
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'EAMG':
                    data1 = enemy_dict[enemy_mon[0]][10]
                    data2 = enemy_dict[enemy_mon[0]][11]
                    data3 = enemy_dict[enemy_mon[0]][12]
                    data4 = enemy_dict[enemy_mon[0]][4]
                    data5 = enemy_dict[enemy_mon[0]][5]
                    data6 = enemy_dict[enemy_mon[0]][6]
                    data7 = enemy_dict[enemy_mon[0]][1]
                    data8 = enemy_dict[enemy_mon[0]][2]
                    data9 = enemy_dict[enemy_mon[0]][3]
                    data10 = enemy_dict[enemy_mon[0]][7]
                    data11 = enemy_dict[enemy_mon[0]][8]
                    data12 = enemy_dict[enemy_mon[0]][9]   
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'EMGA':
                    data1 = enemy_dict[enemy_mon[0]][7]
                    data2 = enemy_dict[enemy_mon[0]][8]
                    data3 = enemy_dict[enemy_mon[0]][9]
                    data4 = enemy_dict[enemy_mon[0]][10]
                    data5 = enemy_dict[enemy_mon[0]][11]
                    data6 = enemy_dict[enemy_mon[0]][12]
                    data7 = enemy_dict[enemy_mon[0]][1]
                    data8 = enemy_dict[enemy_mon[0]][2]
                    data9 = enemy_dict[enemy_mon[0]][3]
                    data10 = enemy_dict[enemy_mon[0]][4]
                    data11 = enemy_dict[enemy_mon[0]][5]
                    data12 = enemy_dict[enemy_mon[0]][6]   
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'EMAG':
                    data1 = enemy_dict[enemy_mon[0]][10]
                    data2 = enemy_dict[enemy_mon[0]][11]
                    data3 = enemy_dict[enemy_mon[0]][12]
                    data4 = enemy_dict[enemy_mon[0]][7]
                    data5 = enemy_dict[enemy_mon[0]][8]
                    data6 = enemy_dict[enemy_mon[0]][9]
                    data7 = enemy_dict[enemy_mon[0]][1]
                    data8 = enemy_dict[enemy_mon[0]][2]
                    data9 = enemy_dict[enemy_mon[0]][3]
                    data10 = enemy_dict[enemy_mon[0]][4]
                    data11 = enemy_dict[enemy_mon[0]][5]
                    data12 = enemy_dict[enemy_mon[0]][6]  
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'MGAE':
                    data1 = enemy_dict[enemy_mon[0]][4]
                    data2 = enemy_dict[enemy_mon[0]][5]
                    data3 = enemy_dict[enemy_mon[0]][6]
                    data4 = enemy_dict[enemy_mon[0]][7]
                    data5 = enemy_dict[enemy_mon[0]][8]
                    data6 = enemy_dict[enemy_mon[0]][9]
                    data7 = enemy_dict[enemy_mon[0]][10]
                    data8 = enemy_dict[enemy_mon[0]][11]
                    data9 = enemy_dict[enemy_mon[0]][12]
                    data10 = enemy_dict[enemy_mon[0]][1]
                    data11 = enemy_dict[enemy_mon[0]][2]
                    data12 = enemy_dict[enemy_mon[0]][3]  
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'MGEA':
                    data1 = enemy_dict[enemy_mon[0]][4]
                    data2 = enemy_dict[enemy_mon[0]][5]
                    data3 = enemy_dict[enemy_mon[0]][6]
                    data4 = enemy_dict[enemy_mon[0]][10]
                    data5 = enemy_dict[enemy_mon[0]][11]
                    data6 = enemy_dict[enemy_mon[0]][12]
                    data7 = enemy_dict[enemy_mon[0]][7]
                    data8 = enemy_dict[enemy_mon[0]][8]
                    data9 = enemy_dict[enemy_mon[0]][9]
                    data10 = enemy_dict[enemy_mon[0]][1]
                    data11 = enemy_dict[enemy_mon[0]][2]
                    data12 = enemy_dict[enemy_mon[0]][3] 
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'MAGE':
                    data1 = enemy_dict[enemy_mon[0]][7]
                    data2 = enemy_dict[enemy_mon[0]][8]
                    data3 = enemy_dict[enemy_mon[0]][9]
                    data4 = enemy_dict[enemy_mon[0]][4]
                    data5 = enemy_dict[enemy_mon[0]][5]
                    data6 = enemy_dict[enemy_mon[0]][6]
                    data7 = enemy_dict[enemy_mon[0]][10]
                    data8 = enemy_dict[enemy_mon[0]][11]
                    data9 = enemy_dict[enemy_mon[0]][12]
                    data10 = enemy_dict[enemy_mon[0]][1]
                    data11 = enemy_dict[enemy_mon[0]][2]
                    data12 = enemy_dict[enemy_mon[0]][3]    
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'MAEG':
                    data1 = enemy_dict[enemy_mon[0]][10]
                    data2 = enemy_dict[enemy_mon[0]][11]
                    data3 = enemy_dict[enemy_mon[0]][12]
                    data4 = enemy_dict[enemy_mon[0]][4]
                    data5 = enemy_dict[enemy_mon[0]][5]
                    data6 = enemy_dict[enemy_mon[0]][6]
                    data7 = enemy_dict[enemy_mon[0]][7]
                    data8 = enemy_dict[enemy_mon[0]][8]
                    data9 = enemy_dict[enemy_mon[0]][9]
                    data10 = enemy_dict[enemy_mon[0]][1]
                    data11 = enemy_dict[enemy_mon[0]][2]
                    data12 = enemy_dict[enemy_mon[0]][3] 
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'MEGA':
                    data1 = enemy_dict[enemy_mon[0]][7]
                    data2 = enemy_dict[enemy_mon[0]][8]
                    data3 = enemy_dict[enemy_mon[0]][9]
                    data4 = enemy_dict[enemy_mon[0]][10]
                    data5 = enemy_dict[enemy_mon[0]][11]
                    data6 = enemy_dict[enemy_mon[0]][12]
                    data7 = enemy_dict[enemy_mon[0]][4]
                    data8 = enemy_dict[enemy_mon[0]][5]
                    data9 = enemy_dict[enemy_mon[0]][6]
                    data10 = enemy_dict[enemy_mon[0]][1]
                    data11 = enemy_dict[enemy_mon[0]][2]
                    data12 = enemy_dict[enemy_mon[0]][3]    
                elif (data_order[(enemy_dict[enemy_mon[0]][0]) % 24]) == 'MEAG':
                    data1 = enemy_dict[enemy_mon[0]][10]
                    data2 = enemy_dict[enemy_mon[0]][11]
                    data3 = enemy_dict[enemy_mon[0]][12]
                    data4 = enemy_dict[enemy_mon[0]][7]
                    data5 = enemy_dict[enemy_mon[0]][8]
                    data6 = enemy_dict[enemy_mon[0]][9]
                    data7 = enemy_dict[enemy_mon[0]][4]
                    data8 = enemy_dict[enemy_mon[0]][5]
                    data9 = enemy_dict[enemy_mon[0]][6]
                    data10 = enemy_dict[enemy_mon[0]][1]
                    data11 = enemy_dict[enemy_mon[0]][2]
                    data12 = enemy_dict[enemy_mon[0]][3]                   
                if (sapphire == False):
                    data10 += 128
                for k in range(1, 13):
                    #checking each pokeball
                    data10 = int(format(data10, '#034b')[2:3] + format(k, '#06b')[2:] + format(data10, '#034b')[7:], 2)
                    #for l in range(0, 512):
                        #data1 = int(format(l, '#018b')[2:18] + format(data1, '#034b')[18:], 2)
                        #for m in reversed(range(0, int(format(data6, '#034b')[18:26], 2) + 1)):
                        #for m in reversed(range(32, 1)):
                            #data6 = int(format(data6, '#034b')[2:26] + format(m, '#010b')[2:], 2)                     
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
                        #print(original_checksum)
                        #valid_combinations.append([i-1, j-1])
                        #if ("0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83' or "0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83'):
                        #   print("ACE move found: " + str(i-1) + " " + str(j-1))
                        #  file.write("ACE move found: " + str(i-1) + " " + str(j-1))
                        #if (f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x0113'):
                        #    print("Eon Ticket found: " + str(i-1) + " " + str(j-1))
                        '''
                        if hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] == '0x9b1e':


                            print(" ACE species found: " + "Player frame: " + str(i-1) + " Enemy Frame: " + str(j-1) + " Player TID/SID: " + otids_list[i][1] + " " + otids_list[i][2] + 
                                " Enemy TID/SID: " + otids_list[j][2] + " " + otids_list[j][1] 
                                + " Species: " + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] 
                            + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] 
                            + " Held Item: " + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] 
                            + " Moves: " + "0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6]
                                + " 0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] + " Pokeball: " + str(k)
                                + (" Egg: " + format(player_key ^ enemy_key ^ data11, '#034b')[3:4]) + " Enemy Mon: " + enemy_mon[0])
                        '''

                        print("Match Found! Player frame: " + str(i-1) + " Enemy Frame: " + str(j-1) + " Player TID/SID: " + otids_list[i][1] + " " + otids_list[i][2] + 
                            " Enemy TID/SID: " + otids_list[j][2] + " " + otids_list[j][1] 
                            + " Species: " + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] 
                        + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] 
                        + " Held Item: " + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] 
                        + " Moves: " + "0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6]
                            + " 0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] + " Pokeball: " + str(k)
                            + (" Egg: " + format(player_key ^ enemy_key ^ data11, '#034b')[3:4]) + " Enemy Mon: " + enemy_mon[0] +  " Checksums: " + str(new_checksum) + " " + str(original_checksum)) 
                        break
                    
                    else: 
                        print("Match Not Found. Player frame: " + str(i-1) + " Enemy Frame: " + str(j-1) + " Player TID/SID: " + otids_list[i][1] + " " + otids_list[i][2] + 
                            " Enemy TID/SID: " + otids_list[j][2] + " " + otids_list[j][1] 
                            + " Species: " + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] 
                        + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] 
                        + " Held Item: " + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] 
                        + " Moves: " + "0x" + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data4), '#034b')[2:], 2)):#0{10}x}"[0:6]
                            + " 0x" + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data5), '#034b')[2:], 2)):#0{10}x}"[0:6] + " Pokeball: " + str(k)
                            + (" Egg: " + format(player_key ^ enemy_key ^ data11, '#034b')[3:4]) + " Enemy Mon: " + enemy_mon[0] + " Checksums: " + str(new_checksum) + " " + str(original_checksum) + " " + 
                            str((int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))) + " " + str((int(format((data1), '#034b')[2:], 2))) + " " + str(data1 % 65536) + " " + str(math.trunc(data1/65536)) + " " + str(player_key ^ enemy_key ^ data1 % 65536) + " " + str(math.trunc((player_key ^ enemy_key ^ data1)/65536))
                            + " Diff: " + str((new_checksum) - (original_checksum))) 
                            
                    #if ((literal_eval(hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] )) < 440):
                        #print("VALID MON")

    #TODO Implement Held Item and PP Checks
    #different versions technically have different checksums (does it matter?)
        #There are version differences for some setups, but other setups work the same on both versions (why?)
    #same with met location?
main()
print("\n",time.time()-t)