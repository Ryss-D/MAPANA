

def valleysCount(path):
    traslation = {"U": 1, "D": -1}
    position = 0
    valley = 0

    try:
        for movement in path:
            position += traslation[movement] 
            if position == 0 and traslation[movement] > 0:
                valley += 1
    except:
        print("Undefied instruction, check your path")

    return valley




