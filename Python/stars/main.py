def stars(arr):
    for i in arr:
        if isinstance(i, str):
            print i[0].lower() * len(i) + "\n"
        else:
            print "*" * i + "\n"

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars(x)