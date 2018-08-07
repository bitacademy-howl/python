def summary(*args):
    data = []
    total = 0

    for arg in args:
        if isinstance(arg, (int, float)):
            data.append(arg)
            total += arg

    return total, max(data), min(data), total / len(data)

total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg)
