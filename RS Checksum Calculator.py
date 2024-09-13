import csv
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
#print(otids_list[0])
'''
for i in range(100):
    for j in range(100):
        print(int(otids_list[i+1][1]) ^ int(otids_list[j+1][1]))
'''

print("Player OTID: " + hex(int(otids_list[1][2])) + hex(int(otids_list[1][1]))[2::])
print("Enemy OTID: " + hex(int(otids_list[1][1])) + hex(int(otids_list[1][2]))[2::])