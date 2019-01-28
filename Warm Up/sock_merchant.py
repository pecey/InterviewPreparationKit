def sock_merchant(size, socks):
    pairs = {}
    count = 0
    for index, sock in enumerate(socks):
        if sock in pairs.keys():
            pairs[sock] = pairs[sock] + 1
            if pairs[sock] == 2:
                count = count + 1
                pairs[sock] = 0
        else:
            pairs[sock] = 1
    return count
