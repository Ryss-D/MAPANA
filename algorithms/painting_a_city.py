def paintin_a_city(building) :
    n = len(building)
    m = len(building[0])

    floor_rooft = (n * m)*2
    side = []
    otherside = []
    front = []
    back = []

    for i in range(m) :
        view = []
        for line in building:
            view.append(line[i])
        side.append(view[0])
        for wall in range(len(view)-1):
            if view[wall] < view[wall + 1]:
                side.append(view[wall+1]-view[wall])
            else: 
                pass

    for i in range(m) :
        view = []
        for line in building:
            view.append(line[i])
        view.reverse()
        otherside.append(view[0])
        for wall in range(len(view)-1):
            if view[wall] < view[wall + 1]:
                otherside.append(view[wall+1]-view[wall])
            else: 
                pass

    for line in building:
        front.append(line[0])
        for wall in range(len(line)-1):
            if line[wall] < line[wall + 1]:
                front.append(line[wall+1]-line[wall])
            else: 
                pass

    for line in building:
        line.reverse()
        back.append(line[0])
        for wall in range(len(line)-1):
            if line[wall] < line[wall + 1]:
                back.append(line[wall+1]-line[wall])
            else: 
                pass

    liters = sum(side) + sum(otherside) + sum(front) + sum(back) + floor_rooft

    return liters