def typeList(thing):
    a = 0
    b = ""
    c = "mixed"
    output = ""
    for i in thing:
        if(isinstance(i,int)):
            a += i
        elif(isinstance(i,str)):
            b += i

    if(a == 0):
        if(b == ""):
            c = "No values"
        else:
            c = "string"
    else:
        if(b == ""):
            c = "integer"
    A = "Sum: "+str(a)
    B = "String: "+b
    C = "The array you entered is of "+c+" type."
    
    output += C + "\n"

    if(b):
        output += B + "\n"
    if(a):
        output += A + "\n"

    return output

l = ['magical','unicorns']

print typeList(l)