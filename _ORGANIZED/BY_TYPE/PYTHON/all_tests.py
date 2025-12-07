# import unittest

class SomeClass():
    def __init__(self, num):
        num
        self.val = num
    def __repr__(self):
        self #?
        return str(self.val)
    def add(self, other):
        return SomeClass(self.val + other)

t = SomeClass(1) #?
t2 = t.add(2)
t2 #?

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         x=1 #?
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

# if __name__ == '__main__':
#     # unittest.main(exit=False)
#     unittest.main()

# import os

# path=os.environ['PATH'] #?
# print(path)

# i = 0 #?
# i=0 #?

# # Nested data
# inputs = [
#     [6.4, 2.8, 5.6, 2.2, 2],  # ?
#     [5.0, 2.3, 3.3, 1.0, 1],
#     [4.9, 2.5, 4.5, 1.7, 2],
# ]

# # Comprehensions
# features = [x[0:-1] for x in inputs]  # ?
# labels = [x[-1] for x in inputs]  # ?

# # macros
# hat = labels  # ?

# # print
# print(features)
# print(labels)

# # side effects
# b = [*range(1, 4)]  # ?  <-- Comment Macro ~ Result ->

# print('before', b)
# b.pop()  # ?
# print('after', b)

# b  # ?
# b


# # functions
# def add2(a):
#     rv = a + 2
#     rv
#     return rv

# # function nesting and macros

# def linked_list_from(*items):
#     head = None  # ?
#     for new_head in items[::-1]:
#         head = (new_head, head)  # ?
#     return head


# l = linked_list_from(1, 2, 3)
# l

# a = 1
# # Loop stuff
# while a < 5:
#     a
#     print('Tick', a)
#     a += 1


# for t in range(5):
#     t
#     t
#     t


# add2(14)  # ?
# a = add2(1)  # ?
# a


# # data types
# tup = (1, 2, 3)  # ?
# tup

# # assorted

# 1 < 0  # ?

# 1 + 334  # ?  Calculator (py-version < 3.6 only)  ->

# text = 'happy'  # ?

# text

# unicode_text = 'é'  # ?

# unicode_text

# print("🍆") #?

# # newline characters in strings
# x = "foo\nfaa"  # ?

# # errors

# 0/0
