# -*- coding: utf-8 -*-

# three door problem

import random

class Door(object):
    """随机生成一个带奖品的三扇门门
    """
    def __init__(self):
        pool = [0, 0, 1]
        self.one = random.choice(pool)
        pool.remove(self.one)
        self.two = random.choice(pool)
        pool.remove(self.two)
        self.three = random.choice(pool)


def choice(choice_num, door):        
    """判断选择是否正确
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
    """
    brief：主持人展示另一扇有山羊的门
    """
    if choice_num == 1:
        if door.one == 1:
            # 选中了汽车，就展示另一个有山羊的门
            return random.choice([2, 3])
        else:
            # 选的是山羊，给出另一只山羊
            # 检测第二只是否山羊
            if door.two == 1:
                # 如果是，打开第三扇门
                return 3
            else:
                # 否则打开第二扇门
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
    # 策略 1, 不换门
    count_1 = 0
    hit_1 = 0
    for i in xrange(100000):
        count_1 += 1
        door = Door()
        cho_num = random.choice([1, 2, 3])
        c = choice(cho_num, door)
        if c:
            hit_1 += 1
    print float(hit_1) / count_1

    # 策略 2，换门
    count_2 = 0
    hit_2 = 0
    for i in xrange(100000):
        choice_pool = [1, 2, 3]
        count_2 += 1
        d = Door()
        cho_num = random.choice(choice_pool)
        p = predict(cho_num, d)
        choice_pool.remove(p)
        choice_pool.remove(cho_num)
        cho_num = random.choice(choice_pool)
        c = choice(cho_num, d)
        if c:
            hit_2 += 1
    print float(hit_2) / count_2

