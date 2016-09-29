import time


def proctimer(context):
    start_time = time.clock()

    def proctime():
        print(context + " %.3f" % (time.clock() - start_time) + "sec")

    return proctime