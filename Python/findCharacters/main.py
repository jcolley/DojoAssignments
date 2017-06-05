def findCharacters(list,char):
    newList = [];
    for i in list:
        if(char in i):
            newList.append(i)
    output = "new_list = "+str(newList)
    
    print output

lst = ['hello','world','my','name','is','Anna']
char = "o"

findCharacters(lst,char)