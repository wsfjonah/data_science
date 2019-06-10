def get_mean(data):
    s = 0.0
    mean = 0.0
    if len(data) == 0:
        raise Exception('normal data size is zero')
    if len(data) <= 4:
        for a in data:
            s = s + a
        mean = s / len(data)
    if len(data) > 4:
        data.sort(reverse=True)
        data = data[2::]
        data.sort()
        for a in data[2::]:
            s = s + a
        mean = s / (len(data) - 4)
    return mean
