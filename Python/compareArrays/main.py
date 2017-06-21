def compareArrays(thing1,thing2):
    if(thing1 == thing2):
        output = "The lists are the same."
    else:
        output = "The lists are not the same."
    
    print output

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

compareArrays(list_one,list_two)