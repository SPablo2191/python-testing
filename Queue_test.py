from Queue import Queue
import unittest
class unitTest(unittest.TestCase):
    def test1(self):
        q = Queue(3)
        res = q.empty()
        self.assertEqual(not res,False,"deberia estar vacia")


    def test4(self):
        q = Queue(1)
        self.assertEqual((q.empty() and  q.full()), False, "Tiene que ser falso")


if __name__ == '__main__':
    unittest.main()