subset = (0, 1, 2, 3)
p = [2, 3, 4, 5]
competidor = {0: 0, 1: 0}
i = 0
for abc in subset:
    z = competidor[i]
    if i >= 2:
        i = 0
    else:
        i += 1
print(competidor)