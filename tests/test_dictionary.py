"""Basic tests for chained dictionary"""

import unittest
from structures.dictionary import Dictionary


class test_add_two(unittest.TestCase):
    """Dictionary test class"""

    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")


class test_add_twice(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[1] = "one"
        self.assertEqual(len(s), 1)
        self.assertEqual(s[1], "one")


class test_store_false(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertFalse(s[1])


class test_store_none(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)


class test_none_key(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)


class test_False_key(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)


class test_collide(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[0] = "zero"
        s[10] = "ten"
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)


class test_double(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        for i in range(11):
            s[i] = str(i)
        self.assertEqual(len(s), 11)
        self.assertEqual(
            str(s),
            "[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], "
            "[6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']]")


class test_double_second(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        for i in range(41):
            s[i] = str(i)
        self.assertEqual(len(s), 41)
        self.assertEqual(
            str(s), "[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], "
            "[5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10'], "
            "[11, '11'], [12, '12'], [13, '13'], [14, '14'], [15, '15'], "
            "[16, '16'], [17, '17'], [18, '18'], [19, '19'], [20, '20'], "
            "[21, '21'], [22, '22'], [23, '23'], [24, '24'], [25, '25'], "
            "[26, '26'], [27, '27'], [28, '28'], [29, '29'], [30, '30'], "
            "[31, '31'], [32, '32'], [33, '33'], [34, '34'], [35, '35'], "
            "[36, '36'], [37, '37'], [38, '38'], [39, '39'], [40, '40']]")


class test_delitem(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        self.assertEqual(len(s), 5)
        s.__delitem__(1)
        s.__delitem__(5)
        s.__delitem__(2)
        s.__delitem__(3)
        s.__delitem__(4)
        self.assertEqual(len(s), 0)
        s[False] = 1
        s[1] = None
        s.__delitem__(False)
        s.__delitem__(1)
        self.assertEqual(len(s), 0)


class test_delitem_no_key(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        self.assertRaises(RuntimeError, lambda: s.__delitem__(6))


class test_half(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        for i in range(11):
            s[i] = str(i)
        self.assertEqual(len(s), 11)
        self.assertEqual(
            str(s),
            "[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], "
            "[6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10']]")
        s.__delitem__(1)
        s.__delitem__(5)
        s.__delitem__(2)
        s.__delitem__(3)
        s.__delitem__(4)
        s.__delitem__(0)
        s.__delitem__(6)
        s.__delitem__(7)
        s.__delitem__(8)
        self.assertEqual(len(s), 2)
        self.assertEqual(str(s), "[[10, '10'], [9, '9']]")


class test_half_second(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        for i in range(41):
            s[i] = str(i)
        self.assertEqual(len(s), 41)
        self.assertEqual(
            str(s),
            "[[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], "
            "[6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10'], [11, '11'], "
            "[12, '12'], [13, '13'], [14, '14'], [15, '15'], [16, '16'], "
            "[17, '17'], [18, '18'], [19, '19'], [20, '20'], [21, '21'], "
            "[22, '22'], [23, '23'], [24, '24'], [25, '25'], [26, '26'], "
            "[27, '27'], [28, '28'], [29, '29'], [30, '30'], [31, '31'], "
            "[32, '32'], [33, '33'], [34, '34'], [35, '35'], [36, '36'], "
            "[37, '37'], [38, '38'], [39, '39'], [40, '40']]")
        for i in range(20):
            s.__delitem__(i)
        self.assertEqual(
            str(s),
            "[[20, '20'], [21, '21'], [22, '22'], [23, '23'], [24, '24'], "
            "[25, '25'], [26, '26'], [27, '27'], [28, '28'], [29, '29'], "
            "[30, '30'], [31, '31'], [32, '32'], [33, '33'], [34, '34'], "
            "[35, '35'], [36, '36'], [37, '37'], [38, '38'], [39, '39'], "
            "[40, '40']]")
        for i in range(20, 34):
            s.__delitem__(i)
        self.assertEqual(
            str(s),
            "[[40, '40'], [34, '34'], [35, '35'], [36, '36'], [37, '37'], "
            "[38, '38'], [39, '39']]")


class test_keys_empty(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        self.assertEqual(s.__keys__(), [])


class test_keys(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        self.assertEqual(s.__keys__(), [1, 2, 3, 4, 5])


class test_keys_long(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        for i in range(41):
            s[i] = str(i)
        self.assertEqual(s.__keys__(),
                         [0,
                          1,
                          2,
                          3,
                          4,
                          5,
                          6,
                          7,
                          8,
                          9,
                          10,
                          11,
                          12,
                          13,
                          14,
                          15,
                          16,
                          17,
                          18,
                          19,
                          20,
                          21,
                          22,
                          23,
                          24,
                          25,
                          26,
                          27,
                          28,
                          29,
                          30,
                          31,
                          32,
                          33,
                          34,
                          35,
                          36,
                          37,
                          38,
                          39,
                          40])


class test_values(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        self.assertEqual(s.__values__(), [
            'one', 'two', 'three', 'four', 'five'])


class test_values_long(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        for i in range(21):
            s[i] = str(i)
        self.assertEqual(s.__values__(),
                         ['0',
                          '1',
                          '2',
                          '3',
                          '4',
                          '5',
                          '6',
                          '7',
                          '8',
                          '9',
                          '10',
                          '11',
                          '12',
                          '13',
                          '14',
                          '15',
                          '16',
                          '17',
                          '18',
                          '19',
                          '20'])


class test_values_empty(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        self.assertEqual(s.__values__(), [])


class test_eq(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        r = Dictionary()
        r[1] = "one"
        r[2] = "two"
        r[3] = "three"
        r[4] = "four"
        r[5] = "five"
        self.assertTrue(s.__eq__(r))


class test_not_eq(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        r = Dictionary()
        r[1] = "one"
        r[2] = "two"
        r[3] = "three"
        r[4] = "four"
        r[5] = "five"
        self.assertFalse(s.__eq__(r))


class test_eq_empty(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        r = Dictionary()
        self.assertTrue(s.__eq__(r))


class test_eq_one_empty(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        r = Dictionary()
        self.assertFalse(s.__eq__(r))


class test_eq_one_empty_other(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        r = Dictionary()
        r[1] = "one"
        self.assertFalse(s.__eq__(r))


class test_items(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        s[1] = "one"
        s[2] = "two"
        s[3] = "three"
        s[4] = "four"
        s[5] = "five"
        self.assertEqual(
            s.__items__(), [
                (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),
                (5, 'five')])


class test_items_empty(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        self.assertEqual(s.__items__(), [])


class test_items_large(unittest.TestCase):
    def test(self):
        """Dictionary test method"""
        s = Dictionary()
        for i in range(41):
            s[i] = str(i)
        self.assertEqual(
            s.__items__(), [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'),
                            (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
                            (10, '10'), (11, '11'), (12, '12'), (13, '13'),
                            (14, '14'), (15, '15'), (16, '16'), (17, '17'),
                            (18, '18'), (19, '19'), (20, '20'), (21, '21'),
                            (22, '22'), (23, '23'), (24, '24'), (25, '25'),
                            (26, '26'), (27, '27'), (28, '28'), (29, '29'),
                            (30, '30'), (31, '31'), (32, '32'), (33, '33'),
                            (34, '34'), (35, '35'), (36, '36'), (37, '37'),
                            (38, '38'), (39, '39'), (40, '40')])
