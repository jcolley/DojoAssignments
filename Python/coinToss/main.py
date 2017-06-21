import random
def coinToss():
    heads = 0
    tails = 0
    for i in range(5000):
        toss = random.randint(1,100)
        head_tail = ""
        if toss >= 50:
            head_tail = "head"
            heads += 1
        if toss < 50:
            head_tail = "tail"
            tails += 1
        print "Attempt #"+str(i)+": Throwing a coin... It's a "+head_tail+"! ... Got "+str(heads)+" head(s) so far and "+str(tails)+" tail(s) so far"

coinToss()