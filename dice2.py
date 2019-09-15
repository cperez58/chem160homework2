from random import choices
ntrials=10000
player1wins=0
for i in range(ntrials):
    ndice1=3
    dice1=choices(range(1,7), k=ndice1)
    dice1.sort(reverse=True)
    if (dice1[0]*dice1[1])^2==8:
        player1wins+=1
    if (dice1[0]*dice1[2])^2==8:
        player1wins+=1
    if (dice1[1]*dice1[2])^2==8:
        player1wins+=1
print(player1wins/ntrials)