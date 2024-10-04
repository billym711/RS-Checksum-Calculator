l = [i for i in range(339) if i < 226 or i > 288]
l.append(254)
l.append(255)
l.append(256)
l.append(257)
l.append(258)
for i in range(12):
    l.remove(i+121)
print(l)