words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
new = words.replace("day","month")
print new

print "\n=============================================\n"

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

print "\n=============================================\n"

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
newlist = [x[0],x[len(x)-1]]
print newlist

print "\n=============================================\n"

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[:len(x)/2]
x = x[len(x)/2:]
print x
print y
x.insert(0,y)
print x