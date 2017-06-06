def odd_even():
    for i in range(1, 2001):
        if i%2 == 0:
            isEven = "even"
        else:
            isEven = "odd"

        print "Number is", str(i) + ". This is an ", isEven, "number."
    print "=" * 40 + "\n"
odd_even()

def multiply(list,multiplier):
    newList = []
    for i in list:
        newList.append(i * multiplier)
    return newList

multiply([2, 4, 10, 16], 5)

def layered_multiples(arr):
    new_array = []
    for i in arr:
        new_array.append([1] * i)

    return new_array

x = layered_multiples(multiply([2, 4, 5], 3))
print x