n = int(input())
anton = 0
danik = 0

games = input().strip()

for game in games[:n]:
    if game == 'A':
        anton += 1
    else:
        danik += 1

if anton > danik:
    print("Anton")
elif anton == danik:
    print("Friendship")
else:
    print("Danik")