data = 2693009664
print(format(data, '#034b'))
print(int(format(data, '#034b')[3:7], 2))
print(format(data, '#034b')[2:3] + format(data, '#034b')[3:7] + format(data, '#034b')[7:])
print(format(3, '#06b')[2:])

print("Egg: " + format(data, '#034b')[3:4])
for k in range(1, 13):
            #checking each pokeball
            data_new = int(format(data, '#034b')[2:3] + format(k, '#06b')[2:] + format(data, '#034b')[7:], 2)
            print(data_new)

#0b01101101110100101000001010110111
#0b01101101110100100010111110110111

print(eval("data"))