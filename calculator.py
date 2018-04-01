#  hrs = mAh / mA


def nimh(capacity, current, loss):
    return ((capacity / current) * loss) / 10
