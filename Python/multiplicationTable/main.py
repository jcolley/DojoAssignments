def multiplicationTable():
    print("\n".join(("{:>4}"*13).format(*(l*k if l*k else l+k if l+k else "" for k in range(13))) for l in range(13)))

multiplicationTable()