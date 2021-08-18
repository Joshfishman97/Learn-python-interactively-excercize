def sing():
    for i in (1,13):
        if(i < 5):
            print("let it be,")
        elif (i%5==0):
            print("whisper words of wisdom,")
        elif (i%11==0):
            print("there will be an answer,")
        else:
            print("let it be")

sing()
