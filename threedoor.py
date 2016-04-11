# -*- coding: utf-8 -*-

# three door problem

import random

class Door(object):
    """Randomly generate three door with one prize
    """
    def __init__(self):
        pool = [0, 0, 1]
        self.one = random.choice(pool)
        pool.remove(self.one)
        self.two = random.choice(pool)
        pool.remove(self.two)
        self.three = random.choice(pool)


def choice(choice_num, door):        
    """verify choice
    """
    try:
        if choice_num == 1:
            assert door.one == 1
        elif choice_num == 2:
            assert door.two == 1
        elif choice_num == 3:
            assert door.three == 1
        else:
            raise Exception("invalid choice")
        return True
    except AssertionError:
        return False


def predict(choice_num, door):
    """show another door without prize
    """
    if choice_num == 1:
        if door.one == 1:
            return random.choice([2, 3])
        else:
            if door.two == 1:
                return 3
            else:
                return 2
    elif choice_num == 2:
        if door.two == 1:
            return random.choice([1, 3])
        else:
            if door.three == 1:
                return 1
            else:
                return 3
    elif choice_num == 3:
        if door.three == 1:
            return random.choice([1, 2])
        else:
            if door.one == 1:
                return 2
            else:
                return 1
    else:
        raise Exception("invalid input")


if __name__ == "__main__":
    # strategy 1, do not change the choice after one door opened by hostess
    count_1 = 0
    hit_1 = 0
    for i in xrange(100000):
        count_1 += 1
        door = Door()
        choice_num = random.choice([1, 2, 3])
        c = choice(choice_num, door)
        if c:
            hit_1 += 1
    print float(hit_1) / count_1

    # stategy 2, change
    count_2 = 0
    hit_2 = 0
    for i in xrange(100000):
        choice_pool = [1, 2, 3]
        count_2 += 1
        d = Door()
        choice_num = random.choice(choice_pool)
        p = predict(choice_num, d)
        # choose another door
        choice_num = (set(choice_pool)^set([p, choice_num])).pop()
        c = choice(choice_num, d)
        if c:
            hit_2 += 1
    print float(hit_2) / count_2

