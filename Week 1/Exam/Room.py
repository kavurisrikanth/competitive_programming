import unittest

def can_enter_all_rooms(rooms):
    '''
    Checks whether all rooms can be entered
    :param rooms: A list of lists.
    :return: True or False
    '''
    keys = [False] * len(rooms)

    print(keys)
    enter = [0]

    while len(enter) > 0:
        one = enter.pop(0)
        if keys[one]:
            continue

        keys[one] = True

        for key in rooms[one]:
            if key < len(keys):
                enter.append(key)

    for key in keys:
        if not key:
            return False

    return True


class Test(unittest.TestCase):

    def test_one(self):
        rooms = [[1], [0,2], [3]]
        self.assertTrue(can_enter_all_rooms(rooms))

    def test_two(self):
        rooms = [[1,3], [3,0,1], [2], [0]]
        self.assertFalse(can_enter_all_rooms(rooms))
    #
    def test_three(self):
        rooms = [[1,2,3], [0], [0], [0]]
        self.assertTrue(can_enter_all_rooms(rooms))

    def test_four(self):
        rooms = [[1], [0,2,4], [1,3,4], [2], [1,2]]
        self.assertTrue(can_enter_all_rooms(rooms))

    def test_five(self):
        rooms = [[1], [2,3], [1,2], [4], [1], [5]]
        self.assertFalse(can_enter_all_rooms(rooms))

    def test_six(self):
        rooms = [[1], [2], [3], [4], [2]]
        self.assertTrue(can_enter_all_rooms(rooms))

    def test_seven(self):
        rooms = [[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]
        self.assertFalse(can_enter_all_rooms(rooms))


unittest.main(verbosity=2)