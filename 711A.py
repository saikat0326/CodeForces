n = int(input())
row = []
result = "NO"
for i in range(n):
    r = list(input())
    row.append(r)

for r in row:
    if r[0] == "O" and r[1] == "O":
        r[0] = "+"
        r[1] = "+"
        result = "YES"
        break
    if r[3] == "O" and r[4] == "O":
        r[3] = "+"
        r[4] = "+"
        result = "YES"
        break
    else: continue

print(result)
if result == "YES":
    for r in row:
        print(*r,sep='')