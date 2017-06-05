def multiplicationTable():
    print("\n".join(("{:>4}"*13).format(*(i*j if i*j else i+j if i+j else "" for j in range(13))) for i in range(13)))

multiplicationTable()