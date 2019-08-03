import time

m = 7910033
a = 84589
c = 5463313


previous_seed = int(time.time()) % m
current_seed = (a * previous_seed + c) % m


def next_number():
    global current_seed, previous_seed
    previous_seed, current_seed = current_seed, (a * current_seed + c) % m


def current_number():
    return current_seed


def previous_number():
    return previous_seed
