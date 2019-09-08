from random import choices
ntrials=10000
player1wins=0
for i in range(ntrials):
    ndice1=2
    dice1=choices(range(1,7), k=ndice1)
    if dice1[0]==dice1[1]:
        player1wins+=1
    ndice2=3
    dice2=choices(range(1,7), k=ndice2)
    dice2.sort(reverse=True)
    if (dice1[0]+dice1[1])>=(dice2[0]+dice2[1]):
        player1wins+=1
print(player1wins/ntrials)