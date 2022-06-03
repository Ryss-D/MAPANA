
matrix = [[6, 2, 6, 6, 2], [6, 1, 2, 7, 3]]
def paintin_a_city(matrix) :
    n = len(matrix)
    m = len(matrix[0])

    floor_rooft = (n * m)*2
    side = []
    otherside = []
    front = []
    back = []

    for i in range(m) :
        x = []
        for line in matrix:
            x.append(line[i])
        side.append(x[0])
        for indexe in range(len(x)-1):
            if x[indexe] < x[indexe + 1]:
                side.append(x[indexe+1]-x[indexe])
            else: 
                pass

    for i in range(m) :
        x = []
        for line in matrix:
            x.append(line[i])
        x.reverse()
        otherside.append(x[0])
        for indexe in range(len(x)-1):
            if x[indexe] < x[indexe + 1]:
                otherside.append(x[indexe+1]-x[indexe])
            else: 
                pass

    for line in matrix:
        front.append(line[0])
        for indexe in range(len(line)-1):
            if line[indexe] < line[indexe + 1]:
                front.append(line[indexe+1]-line[indexe])
            else: 
                pass

    for line in matrix:
        line.reverse()
        back.append(line[0])
        for indexe in range(len(line)-1):
            if line[indexe] < line[indexe + 1]:
                back.append(line[indexe+1]-line[indexe])
            else: 
                pass

                

    liters = sum(side) + sum(otherside) + sum(front) + sum(back) + floor_rooft

    return liters