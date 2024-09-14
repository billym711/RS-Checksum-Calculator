import csv
import math
from ast import literal_eval 
with open('OTIDs.csv', newline='') as otids:
    reader = csv.reader(otids)
    otids_list = list(reader)

#Shroomish Decrypted Data
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

valid_combinations = []
#print(otids_list[0])
original_checksum = ((data1 % 65536) + math.trunc(data1/65536) + (data2 % 65536) + math.trunc(data2/65536) + (data3 % 65536)
        + math.trunc(data3/65536) + (data4 % 65536) + math.trunc(data4/65536) + (data5 % 65536) + math.trunc(data5/65536)
        + (data6 % 65536) + math.trunc(data6/65536) + (data7 % 65536) + math.trunc(data7/65536) + (data8 % 65536)
        + math.trunc(data8/65536) + (data9 % 65536) + math.trunc(data9/65536) + (data10 % 65536) + math.trunc(data10/65536)
        + (data11 % 65536) + math.trunc(data11/65536) + (data12 % 65536) + math.trunc(data12/65536))%65536
for i in range(3000, 3500):
    player_key = pid ^ (literal_eval(f"{int(otids_list[i][2]):#0{6}x}" + f"{int(otids_list[i][1]):#0{6}x}"[2::]))
    print("Player frame " + str(i-1) + " Player Key: " + str(player_key))
    for j in range(700, 1200):

        enemy_key = pid ^ (literal_eval(f"{int(otids_list[j][1]):#0{6}x}" + f"{int(otids_list[j][2]):#0{6}x}"[2::]))


        new_checksum = ((player_key ^ enemy_key ^ data1 % 65536) + math.trunc((player_key ^ enemy_key ^ data1)/65536) + (player_key ^ enemy_key ^ data2 % 65536) + math.trunc((player_key ^ enemy_key ^ data2)/65536) + (player_key ^ enemy_key ^ data3 % 65536)
        + math.trunc((player_key ^ enemy_key ^ data3)/65536) + (player_key ^ enemy_key ^ data4 % 65536) + math.trunc((player_key ^ enemy_key ^ data4)/65536) + (player_key ^ enemy_key ^ data5 % 65536) + math.trunc((player_key ^ enemy_key ^ data5)/65536)
        + (player_key ^ enemy_key ^ data6 % 65536) + math.trunc((player_key ^ enemy_key ^ data6)/65536) + (player_key ^ enemy_key ^ data7 % 65536) + math.trunc((player_key ^ enemy_key ^ data7)/65536) + (player_key ^ enemy_key ^ data8 % 65536)
        + math.trunc((player_key ^ enemy_key ^ data8)/65536) + (player_key ^ enemy_key ^ data9 % 65536) + math.trunc((player_key ^ enemy_key ^ data9)/65536) + (player_key ^ enemy_key ^ data10 % 65536) + math.trunc((player_key ^ enemy_key ^ data10)/65536)
        + (player_key ^ enemy_key ^ data11 % 65536) + math.trunc((player_key ^ enemy_key ^ data11)/65536) + (player_key ^ enemy_key ^ data12 % 65536) + math.trunc((player_key ^ enemy_key ^ data12)/65536))%65536
        print("Enemy frame " + str(j) + " Enemy Key: " + str(enemy_key) + " New Checksum: " + str(new_checksum))
        if new_checksum == original_checksum:
            valid_combinations.append([i-1, j-1])
'''
print("Player OTID: " + f"{int(otids_list[1][2]):#0{6}x}" + f"{int(otids_list[1][1]):#0{6}x}"[2::])
print("Enemy OTID: " + f"{int(otids_list[1][1]):#0{6}x}" + f"{int(otids_list[1][2]):#0{6}x}"[2::])
print(literal_eval(f"{int(otids_list[1][1]):#0{6}x}" + f"{int(otids_list[1][2]):#0{6}x}"[2::]))
print(literal_eval(f"{int(otids_list[1][2]):#0{6}x}" + f"{int(otids_list[1][1]):#0{6}x}"[2::]))
print(pid ^ (literal_eval(f"{int(otids_list[1][2]):#0{6}x}" + f"{int(otids_list[1][1]):#0{6}x}"[2::])))
print(pid ^ (literal_eval(f"{int(otids_list[1][1]):#0{6}x}" + f"{int(otids_list[1][2]):#0{6}x}"[2::])))


player_key = pid ^ (literal_eval(f"{int(otids_list[1][2]):#0{6}x}" + f"{int(otids_list[1][1]):#0{6}x}"[2::]))
enemy_key = pid ^ (literal_eval(f"{int(otids_list[1][1]):#0{6}x}" + f"{int(otids_list[1][2]):#0{6}x}"[2::]))

checksum = data1 ^ (pid ^ (literal_eval(f"{int(otids_list[1][2]):#0{6}x}" + f"{int(otids_list[1][1]):#0{6}x}"[2::]))) ^ 979719048

print(checksum)'''
'''
print(((979719048 ^ 4218262619 ^ data1 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data1)/65536) + (979719048 ^ 4218262619 ^ data2 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data2)/65536) + (979719048 ^ 4218262619 ^ data3 % 65536)
        + math.trunc((979719048 ^ 4218262619 ^ data3)/65536) + (979719048 ^ 4218262619 ^ data4 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data4)/65536) + (979719048 ^ 4218262619 ^ data5 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data5)/65536)
        + (979719048 ^ 4218262619 ^ data6 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data6)/65536) + (979719048 ^ 4218262619 ^ data7 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data7)/65536) + (979719048 ^ 4218262619 ^ data8 % 65536)
        + math.trunc((979719048 ^ 4218262619 ^ data8)/65536) + (979719048 ^ 4218262619 ^ data9 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data9)/65536) + (979719048 ^ 4218262619 ^ data10 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data10)/65536)
        + (979719048 ^ 4218262619 ^ data11 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data11)/65536) + (979719048 ^ 4218262619 ^ data12 % 65536) + math.trunc((979719048 ^ 4218262619 ^ data12)/65536))%65536)
        '''
print(valid_combinations)