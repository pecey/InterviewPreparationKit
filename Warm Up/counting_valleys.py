def counting_valleys(n, path):
    valleys = 0
    previous_altitude = 0
    for step in path:
        if step == "D":
            current_altitude = previous_altitude - 1
        else:
            current_altitude = previous_altitude + 1
        if current_altitude == 0 and step == "U":
            valleys = valleys + 1
        previous_altitude = current_altitude
    return valleys



