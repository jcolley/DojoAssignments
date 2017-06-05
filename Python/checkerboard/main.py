def checkerBoard():
    even = " * * * *"
    odd = "* * * * "

    for i in range(0,7):
        if(i%2 == 0):
            print odd
        else:
            print even
checkerBoard()