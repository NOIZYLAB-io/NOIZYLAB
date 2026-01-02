def is_anomalous(status_series, k=3):
    # status_series: list of ints
    if not status_series: return False
    mean = sum(status_series)/len(status_series)
    var = sum((x-mean)**2 for x in status_series)/len(status_series)
    std = (var ** 0.5) or 1
    return any(abs(x-mean)/std >= k for x in status_series[-5:])
