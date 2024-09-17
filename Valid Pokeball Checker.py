import csv
import math
from ast import literal_eval 
with open('OTIDs.csv', newline='') as otids:
    reader = csv.reader(otids)
    otids_list = list(reader)
file = open('ACE combos.txt', 'a')

#TODO: just copy and paste the whole string of hex data (maybe can do int?) and substring it to get the data instead of doing individual copy pastes
#Do we need to check the PIDs for otherwise equal mons? different nature = different PID but i haven't noticed any differences yet
#No because the original PID is preserved on the glitch mon. This means that the structure doesn't matter as long as all the decrypted data is identical
#Enemy 1 starts at 45C0, Enemy 2 starts at 4624, Enemy 3 starts at 4688
enemy_data_list = [["Rick Wurmple 1-2", "889308005491506CD1CFCCC7CAC6BFFF00000202BBFFFFFFFFFFFF007BA10000FE03586C9C02586CDC44586CFD02096CDC02586CFF2A586CDC02586CDC02586CDC02586CDC13DC4CDC02586CDC02586C"], 
                   ["Allen Poochyena", "88BE0A00DEDDA50DCAC9C9BDC2D3BFC8BBFF0202BBFFFFFFFFFFFF00B42200004862AF0D2B63AF0D5625AF0D7763FF0C5663AF0D754BAF0D5663AF0D5663AF0D5663AF0D56722AAD5663AF0D5663AF0D"],
                   ["Allen Taillow", "88FE1300462BAED1CEBBC3C6C6C9D1FF00000202BBFFFFFFFFFFFF007C210000CED5BDD1CED5BDD1CED5BDD1CEC43E71CED5BDD1CED5BDD1FED4BDD1F7D5BDD1CE93BDD18ED590D1CED5BDD1EDFDBDD1"],
                   ["Tiana Zigzagoon 1-2", "78D10A00B2F4C231D4C3C1D4BBC1C9C9C8FF0202BBFFFFFFFFFFFF0055210000EA24C8318A25C831CA63C831EB25E531CA25C831E90DC831CA25C831CA25C831CA25C831CA344C91CA25C831CA25C831"],
              ["Billy Seedot", "887E08001650DCF9CDBFBFBEC9CEFF0000000202BBFFFFFFFFFFFF004C1A0000B42FD4F92D2ED4F99E68D4F9EB2EBEF99E2ED4F99430D4F99E2ED4F99E2ED4F99E2ED4F99E3D52599E2ED4F99E2ED4F9"],
              ["Billy Taillow", "88CE110091ED6464CEBBC3C6C6C9D1FF00000202BBFFFFFFFFFFFF0076430000592358646D2317643A0B6B7A1923756419237564192375642922756423227564196575641930FDC41923756419237564"],
              ["Winston Zigzagoon", "888A0C00167F827DD4C3C1D4BBC1C9C9C8FF0202BBFFFFFFFFFFFF00222500009EF58E7D9EF58E7D9EF58E7D9EE609DD9EF58E7D9EF58E7DBEF4E07DC9F48E7D9EB38E7DBFF5A37DB9F58E7DBDDD907D"],
                ["Lyle Wurmple 1-6", "88A00800BE6BC52ED1CFCCC7CAC6BFFFFF000202BBFFFFFFFFFFFF00554B000036CBCD2E36CBCD2E36CBCD2E36F04E8E36CBCD2E36CBCD2E14CACD2E2DCBCD2E368DCD2E17CB9C2E36CBCD2E15E3CD2E"],
                ["James Nincada", "8816090056DFBD49C8C3C8BDBBBEBBFF00000202BBFFFFFFFFFFFF0096450000D4C9DE4953C9B449FDD7BB49DEC9B449DEC9B449DEC9B449F3C8B44970CAB449DE8FB449DEF23CE9DEC9B449DEC9B449"],
                ["Cindy Zigzagoon", "78DB0A008AD11A25D4C3C1D4BBC1C9C9C8FF0202BBFFFFFFFFFFFF0022250000F20A1025F20A1025F20A1025F2199785F20A1025F20A1025D20B7E25A50B1025F24C1025D30A3D25D50A1025D1220E25"],
                [ "Haley Lotad", "78AB0700EAF90810C6C9CEBBBEFF000000000202BBFFFFFFFFFFFF006725000092520F1092520F1092520F10924188B092520F1092520F10B5530F107E520F1092140F10A4532210D5520F109D7A1B10"],
                [ "Haley Shroomish", "78861200B723C68BCDC2CCC9C9C7C3CDC2FF0202BBFFFFFFFFFFFF00531F000088A5F58B81A5D48BDB86CA8BCFA5D48BCFA5D48BCFA5D48BFDA4D48B7DA5D48BCFE3D48BCFB6532BCFA5D48BCFA5D48B"],
                [ "Ivan Magikarp 1-3", "88320900B55F3EECC7BBC1C3C5BBCCCAFF000202BBFFFFFFFFFFFF00D3FB0000BC6D37EC336C37EC3D2B37ECAB6D37EC3D6D37EC156D37EC3D6D37EC3D6D37EC3D6D37EC3D7EB14C3D6D37EC3D6D37EC"],
                [ "Joey Zigzagoon", "88210A006D58F3CAD4C3C1D4BBC1C9C9C8FF0202BBFFFFFFFFFFFF005E310000C479D4CAC279F9CAC651E7CAE579F9CAE579F9CAE579F9CAC578F9CAE57BF9CAE53FF9CAE566716AE579F9CAE579F9CA"],
                [ "Joey Machop", "88D411003B129AD2C7BBBDC2C9CAFF0000000202BBFFFFFFFFFFFF0010270000F0C6A0D2C7C68BD2A7D895D2B3C68BD2B3C68BD2B3C68BD2F1C68BD283C48BD2B3808BD2B3D90172B3C68BD2B3C68BD2"],
                [ "Jose Wurmple", "889B08009766FDB5D1CFCCC7CAC6BFFFFF000202BBFFFFFFFFFFFF00B35600003EFDA4B537FDF5B53CD5D6B51FFDF5B51FFDF5B51FFDF5B53DFCF5B51FFFF5B51FBBF5B51FE27D15D9E596B91FFDF5B5"],
                [ "Jose Silcoon", "88211100CCDC9842CDC3C6BDC9C9C8FF06000202BBFFFFFFFFFFFF005C2E000067FC894244FF894244BB89422EFD894244FD89425AFD894244FD894244FD894244FD894244E201E282E5EA4E44FD8942"],
                [ "Jose Nincada", "887E1900CB7CEB7BC8C3C8BDBBBEBBFF06000202BBFFFFFFFFFFFF00BF4E00004902987BCE02F27B601CFD7B4302F27B4302F27B4302F27B6E03F27BED01F27B4344F27B431D7ADB851A91774302F27B"],
                [ "Janice Marill", "7823090041A30F8FC7BBCCC3C6C6FF0000000202BBFFFFFFFFFFFF00904B00001880698F1E80318F1AA818963980068F3980068F3980068F8E80068F1983068F39C6068F399F8C2F3980068F3980068F"],
                [ "Clark Geodude 1-3", "882209005F8B17CFC1BFC9BECFBEBFFF33000202BBFFFFFFFFFFFF00FA300000F6A971CFFBA81ECFF48111CFD7A91ECFD7A91ECFD7A91ECF9DA91ECFEDA81ECFD7EF1ECFD7B6966FD7A91ECFD7A91ECF"],
                [ "Jerry Ralts", "88D60700909DFB15CCBBC6CECDFF000001000202BBFFFFFFFFFFFF00D7880000904AFC15FA4FFC151868FC15354BA115184BFC153052FC15184BFC15184BFC15184BFC15185476B539CFEC17184BFC15"],
                [ "Karen Shroomish", "78D90A0065984FC2CDC2CCC9C9C7C3CDC2FF0202BBFFFFFFFFFFFF005DB200005A4164C2534145C209625BC21D4145C21D4145C21D4145C22F4045C2944045C21D0745C21D5ECC623CC555C01D4145C2"],
                [ "Karen Whismur", "7831140011E0159FD1C2C3CDC7CFCCFF01000202BBFFFFFFFFFFFF00F09900001BD0019FCAD0019F6997019F68D1FC9F69D1019F4ADB019F69D1019F69D1019F69D1019F69CE883F4855119D69D1019F"],
                [ "Ned Tentacool", "88380900D5B68E29CEBFC8CEBBBDC9C9C6FF0202BBFFFFFFFFFFFF0066190000158E87292D8687295DC88729758EB729D98E87297E9AA4295D8E87295D8E87295D8E87295D9B0B895D8E87295D8E8729"],
                [ "Elliot Magikarp 1-2", "88C10A002F1C46E6C7BBC1C3C5BBCCCAFF000202BBFFFFFFFFFFFF004903000026DD4CE6D8DB4CE6A79B4CE631DD4CE6A7DD4CE68FDD4CE6A7DD4CE6A7DD4CE6A7DD4CE6A7C8C746A7DD4CE6A7DD4CE6"],
                [ "Elliot Tentacool", "8859160003DA209BCEBFC8CEBBBDC9C9C6FF0202BBFFFFFFFFFFFF00CB1200008B83369B8B83369B8B83369B8B96BE3B8B83369B8B83369BC383369B0B81369B8BC5369BA383069B8B83369BA897369B"],
                [ "Huey Machop", "88B7070034F7B4F8C7BBBDC2C9CAFF001C000202BBFFFFFFFFFFFF00323D0000FF4098F8C840B1F8A85EADE1BC40B3F8BC40B3F8BC40B3F8FE40B3F8F046B3F8BC06B3F8BC583D58BC40B3F8BC40B3F8"],
                [ "Edmond Wingull 1-2", "880B0A001C2CDDECD1C3C8C1CFC6C6FF11000202BBFFFFFFFFFFFF00512000009427D7EC9427D7EC9427D7EC943F5B4C9427D7EC9427D7ECA126D7EC5421D7EC9461D7ECB927E0ECA427D7ECBC3EC3EC"],
                [ "Edmond Machop", "88321300439EE458C7BBBDC2C9CAFF0000000202BBFFFFFFFFFFFF00AF210000CBACF758CBACF758CBACF758CBB47BF8CBACF758CBACF75889ACF75806AFF758CBEAF75888ACDC58BFACF758DFB2E958"],
                [ "Ricky Zigzagoon", "88E60A00B7612C53D4C3C1D4BBC1C9C9C8FF0202BBFFFFFFFFFFFF002C2900003F8726533F8726533F8726533F9FA8F33F8726533F8726531F862653878D26533FC1265323873B5318871F533088385C"],
                [ "Lola Azurill 1-2", "78890800F0C6EEB1BBD4CFCCC3C6C6FF11000202BBFFFFFFFFFFFF00283B0000884FE6B1884FE6B1884FE6B188576B11884FE6B1884FE6B1D64EE6B15549E6B18809E6B11E4F2AB1AF4F77B1A05BF8AF"],
                [ "Simon Azurill", "88610900B3A45B5EBBD4CFCCC3C6C6FF00000202BBFFFFFFFFFFFF00B0390000ADC59E5E1CC5C35E13D14C403BC5525E3BC5525E3BC5525E65C4525E5DC0525E3B83525E3BDDDEFE3BC5525E3BC5525E"],
                [ "Simon Marill", "88E611002B5EE0A9C7BBCCC3C6C6FF0000000202BBFFFFFFFFFFFF00D846000082B89EA984B8C6A98090EFB0A3B8F1A9A3B8F1A9A3B8F1A914B8F1A9C5BDF1A9A3FEF1A9A3A07D09A3B8F1A9A3B8F1A9"],
                [ "Johanna Goldeen", "78A90A005B5EE78AC1C9C6BEBFBFC8FF02000202BBFFFFFFFFFFFF00BB3B000063F7CA8A79F6DD8A00E9E29E23F7ED8A23F7ED8A23F7ED8A55F7ED8AB6FFED8A23B1ED8A23EF602A23F7ED8A23F7ED8A"],
                [ "Dwayne Wingull", "881C0A003618CB56D1C3C8C1CFC6C6FF02000202BBFFFFFFFFFFFF00C31E00008B05C1568D01C156BE42C1569304F6568E04C156961DD556BE04C156BE04C156BE04C156BE1C4AF6BE04C156BE04C156"],
                [ "Dwayne Machop", "88541300F295D590C7BBBDC2C9CAFF0000000202BBFFFFFFFFFFFF00C720000039C1ED900EC1C6906EDFD8907AC1C6907AC1C6907AC1C69038C1C6909CC3C6907A87C6907AD94D307AC1C6907AC1C690"],
                [ "Dwayne Tentacool", "88EB1E0076734B66CEBFC8CEBBBDC9C9C6FF0202BBFFFFFFFFFFFF00CD190000D6986566FE985566DD8C5566FE985566FE985566FE985566B6985566819E5566FEDE5566FE80DEC6FE985566FE985566"],
                [ "Isabel Plusle", "783D0900CBF723E5CAC6CFCDC6BFFF0008000202BBFFFFFFFFFFFF00E3380000B3CA2AE5B3CA2AE5B3CA2AE5B3D3A545B3CA2AE5B3CA2AE5D2CBA1E59CC72AE5B38C2AE59ECA7CE5D1CA24E49BDE34F1"],
                [ "Isabel Minun", "78B21100370F8B51C7C3C8CFC8FF0003E0450202BBFFFFFFFFFFFF00E43800002DBC115160B09A514FFB9A5162BDCC512DBD945067A984454FBD9A514FBD9A514FBD9A514FA415F14FBD9A514FBD9A51"],
                [ "Daisy Roselia", "784109002FAA20C1CCC9CDBFC6C3BBFF00000202BBFFFFFFFFFFFF00204B000010EB63C17FEB67C143C30ADF57EB29C157EB29C157EB29C13CEA29C1B0E229C157AD29C157F9B96157EB29C157EB29C1"],
                [ "Amy & Liv Plusle", "808C0900AB1BE273CAC6CFCDC6BFFF0002000202BBFFFFFFFFFFFF002A3400002B97EB732B97EB732B97EB732B857BD32B97EB732B97EB734A96EB732B87EB732BD1EB730697BD734997E5720383F567"],
                [ "Amy & Liv Minun", "80501200DAFC3D00C7C3C8CFC8FF000000000202BBFFFFFFFFFFFF002B3400005AAC2F005AAC2F005AAC2F005ABEBFA05AAC2F005AAC2F0038AD2F005ABC2F005AEA2F0077AC790038AC210172B83114"],
                [ "Miguel Skitty", "886309007BB0CF0CCDC5C3CECED3FF0001000202BBFFFFFFFFFFFF007D210000F3D3C60CF3D3C60CF3D3C60CF3C156ACF3D3C60CF3D3C60CC8D24D0C3FDFC60CF395C60CD4D3130CDCD3C50CEDDCC906"],
                [ "Andrew Magikarp 1", "88B90A00F9FEAAA7C7BBC1C3C5BBCCCAFF000202BBFFFFFFFFFFFF0060FA00007147A0A77147A0A77147A0A7715525077147A0A77147A0A7F047A0A7ED47A0A77101A0A7E747A0A77147A0A75947A0A7"],
                [ "Andrew Tentacool", "884916007E6C0315CEBFC8CEBBBDC9C9C6FF0202BBFFFFFFFFFFFF002F120000BE25151514211515F6631515DE252515F6251515D5311515F6251515F6251515F6251515F6379FB5F6251515F6251515"],
                [ "Andrew Magikarp 2", "880221009A42192FC7BBC1C3C5BBCCCAFF000202BBFFFFFFFFFFFF00692D00009340382F6850382F1206382F8440192F1240382F3A63382F1240382F1240382F1240382F1252B78F1240382F1240382F"],
                [ "Timmy Poochyena", "88E20A00D0F03E6ECAC9C9BDC2D3BFC8BBFF0202BBFFFFFFFFFFFF00293100004613346E9814346E5854346E7912646F4412346E7B3A3B6E5812346E5812346E5812346E580BB8CE5812346E5812346E"],
                [ "Timmy Aron", "88EC11007FB3DDDFBBCCC9C8FF00000000000202BBFFFFFFFFFFFF00672100009D5F71DFEA5F24DFE955C3FCF75FCCDFF75FCCDFF75FCCDF895ECCDFF74BCCDFF77CCCDFF7465C7FF75FCCDFF75FCCDF"],
                [ "Timmy Electrike", "88C01C006FD8FECEBFC6BFBDCECCC3C5BFFF0202BBFFFFFFFFFFFF00784C0000C618B4CECC18B2CFC40CFCE6E718E2CEE718E2CEE718E2CEB619E2CE8115E2CEE75EE2CEE7016C6EE718E2CEE718E2CE"],
                [ "Edwin Lombre", "8876080005305EDFC6C9C7BCCCBFFF0001000202BBFFFFFFFFFFFF00DA4500008D4656DF8D4656DF8D4656DF8D5FD87F8D4656DF8D4656DFA54756DFC14056DF8D0056DFBB477BDFCA465DDE826E42CB"],
                [ "Edwin Nuzleaf", "88BA1100ECC30B2BC8CFD4C6BFBBC0FF00000202BBFFFFFFFFFFFF00103B00004F781A2B287F1A2B643F1A2B6579702B2E79112A4767323F64791A2B64791A2B64791A2B6460948B64791A2B64791A2B"],
                [ "Edward Abra", "8891070010C4C8D1BBBCCCBBFF11000000110202BBFFFFFFFFFFFF00B20A0000A755CFD17F5CCFD19813CFD17555CFD19855CFD19755CFD19855CFD19855CFD19855CFD1984C5F719855CFD19855CFD1"],
                [ "Dale Tentacool 1+3", "88F10900392C00F3CEBFC8CEBBBDC9C9C6FF0202BBFFFFFFFFFFFF00661D000099DD39F335DD09F392C92AF3B1DD09F3B1DD09F3B1DD09F3F9DD09F3C1D509F3B19B09F3B1C48553B1DD09F3B1DD09F3"],
                [ "Dale Wailmer", "8856120072854093D1BBC3C6C7BFCCFF00000202BBFFFFFFFFFFFF0075460000C3D252935FD45293FA9552936CD37F93CDD39F93D2FB4B87FAD35293FAD35293FAD35293FACADD33FAD35293FAD35293"],
                [ "Dale Tentacool 2", "88471C007706C714CEBFC8CEBBBDC9C9C6FF0202BBFFFFFFFFFFFF00DB170000FF41DB14FF41DB14FF41DB14FF5852B4FF41DB14FF41DB14B741DB147042DB14FF07DB14D741EB14FF41DB14DC55DB14"],

              ]

enemy_dict = {
                                                            
            }
print(enemy_dict)
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
print(enemy_dict)

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
                        + (" Egg: " + format(player_key ^ enemy_key ^ data11, '#034b')[3:4]) + " Enemy Mon: " + enemy_mon[0]) 
                    break
                #if ((literal_eval(hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[0:2] + hex(int(format((player_key ^ enemy_key ^ data1), '#034b')[2:], 2))[-4:] )) < 440):
                    #print("VALID MON")
print("Done")
file.close()