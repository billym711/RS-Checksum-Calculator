l = [i for i in range(339) if i < 226 or i > 288]
l.append(254)
l.append(255)
l.append(256)
l.append(257)
l.append(258)
for i in range(12):
    l.remove(i+121)
print(l)
data1 = 505287720
print((format(data1, '#034b')[2:10], 2))
print((format(data1, '#034b')[10:18], 2))
print((format(data1, '#034b')[18:26], 2))
print((format(data1, '#034b')[26:34], 2))

print((format(30, '#010b')[2:10]))
print(int(format(30, '#010b')[2:10], 2))
print((format(data1, '#034b')[2:26] + format(30, '#010b')[2:], 2))

#Checking PP counts
'''
print("OG Move 1 PP: " + str(int(format(data6, '#034b')[26:34], 2)))
print("OG Move 2 PP: " + str(int(format(data6, '#034b')[18:26], 2)))
print("OG Move 3 PP: " + str(int(format(data6, '#034b')[10:18], 2)))
print("OG Move 4 PP: " + str(int(format(data6, '#034b')[2:10], 2)))
'''
for m in reversed(range(0, 32 + 1)):
    print(m)