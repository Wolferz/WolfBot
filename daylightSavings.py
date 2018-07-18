def daySave():
    import time
    dysave = True
    local = time.localtime()
    print('CH: ' + str(local.tm_hour))
    if 11 <= local.tm_mon <= 12 or 1 <= local.tm_mon < 3 and local.tm_wday == 6 and local.tm_mday < 7:
        print('Not Daylight Savings')
        dysave = False
    if 3 <= local.tm_mon <= 10 and local.tm_wday == 6 and 7 > local.tm_mday > 14:
        print('Daylight Savings')
        dysave = True
    print(dysave)
    return dysave