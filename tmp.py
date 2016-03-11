def outside():
    msg = "Outside!"

    def inside():
        print(msg)
        msg = 1

    inside()
    print(msg)

outside()
