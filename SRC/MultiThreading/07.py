#_*_coding=utf-8_*_

import threading

sum = 0
loopSum = 10000

def myAdd():
    global  sum,loopSum
    for i in range(1,loopSum):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1

if __name__ == "__main__":

    print "Starting......{}".format(sum)

    t1 = threading.Thread(target=myAdd)
    t2 = threading.Thread(target=myMinu)

    t1.start()
    t2.start()

    print "Done.....{}".format(sum)