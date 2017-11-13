import datetime

def test():
    # ticks = time.time()
    # print(ticks)
    #
    # localtime = time.localtime(time.time())
    # print(localtime)
    #
    # asctime = time.asctime( time.localtime(time.time()) )
    # print(asctime)
    #
    # strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(strftime)

#import datetime

    now = datetime.datetime.now()
    print(now)

    delta = datetime.timedelta(days=1)
    print(delta)

    n_days = now + delta

    print(n_days.strftime('%Y-%m-%d %H:%M:%S'))
    print(n_days.strftime('%d'))

test()
