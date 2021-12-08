with open("input.txt") as f:
    data = [""]*12
    for i in f:
        i = i.strip()
        for j in range(0, 12):
            data[j] += i[j]

gamma = ""
epsilon = ""
for i in data:
    if i.count("1") > i.count("0"):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


print(gamma)
print(epsilon)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)



print(gamma * epsilon)
