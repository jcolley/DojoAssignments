def typeList(thing):
    integer_sum = 0
    output_string = ""
    output_type = "mixed"
    output = ""
    for i in thing:
        if isinstance(i, int) or isinstance(i, float):
            integer_sum += i
        elif isinstance(i, str):
            output_string += i

    if integer_sum == 0:
        if output_string == "":
            output_type = "No values"
        else:
            output_type = "string"
    else:
        if output_string == "":
            output_type = "integer"
    A = "Sum: "+str(integer_sum)
    B = "String: "+output_string
    C = "The array you entered is of "+output_type+" type."

    output += C + "\n"

    if output_string:
        output += B + "\n"
    if integer_sum:
        output += A + "\n"

    return output

l = ['magical unicorns',19,'hello',98.98,'world']

print typeList(l)