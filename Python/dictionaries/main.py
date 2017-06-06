def aboutMe():
    me = {}
    me["name"] = raw_input("What is your name? ")
    me["favorite language"] = raw_input("What is your language of choice? ")
    me["country of birth"] = raw_input("In what country were you born? ")
    me["age"] = raw_input("How old are you? ")
    s1 = "My"
    s2 = "is"
    for key,val in me.iteritems():
        print "My",key,"is",val

aboutMe()