def SayHello(name):
    print "I want to say hello with your, {}".format(name)
    print "hello {}".format(name)
    print "Done..................."

if __name__ == "__main__":
    print "*" * 30
    name = raw_input("Please input your name:")
    SayHello(name)
    print "@" * 30