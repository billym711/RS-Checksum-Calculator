import csv
import math
from ast import literal_eval 
with open('OTIDs.csv', newline='') as otids:
    reader = csv.reader(otids)
    otids_list = list(reader)
file = open('ACE combos.txt', 'a')
file.write('test')

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
for i in range(80000, 100000):
    player_key = pid ^ (literal_eval(f"{int(otids_list[i][2]):#0{6}x}" + f"{int(otids_list[i][1]):#0{6}x}"[2::]))
    #print("Player frame " + str(i-1) + " Player Key: " + str(player_key))
    for j in range(700, 50000):

        enemy_key = pid ^ (literal_eval(f"{int(otids_list[j][1]):#0{6}x}" + f"{int(otids_list[j][2]):#0{6}x}"[2::]))

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
                if ("0x" + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83' or "0x" + f"{(int(format((player_key ^ enemy_key ^ data2), '#034b')[2:], 2)):#0{10}x}"[-4:] == '0x6d83' or f"{(int(format((player_key ^ enemy_key ^ data2), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x6d83'):
                    print("ACE move found: " + str(i-1) + " " + str(j-1))
                    file.write("ACE move found: " + str(i-1) + " " + str(j-1))
                #if (f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6] == '0x0113'):
                #    print("Eon Ticket found: " + str(i-1) + " " + str(j-1))
                
                print("Match Found! Player frame: " + str(i-1) + " Enemy Frame: " + str(j-1) + " Player TID/SID: " + otids_list[i][1] + " " + otids_list[i][2] + 
                    " Enemy TID/SID: " + otids_list[j][2] + " " + otids_list[j][1] + " Moves: " + "0x" + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2)):#0{10}x}"[0:6]
                    + " 0x" + f"{(int(format((player_key ^ enemy_key ^ data2), '#034b')[2:], 2)):#0{10}x}"[-4:] + " " + f"{(int(format((player_key ^ enemy_key ^ data2), '#034b')[2:], 2)):#0{10}x}"[0:6] + " Pokeball: " + str(k))
                break
            #if ((literal_eval(hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] )) < 440):
                #print("VALID MON")
print("Done")
file.close()