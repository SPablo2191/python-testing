from Queue import Queue
import unittest
class unitTest(unittest.TestCase):
    def test1(self):
        q = Queue(3)
        res = q.empty()
        self.assertEqual(not res,False,"deberia estar vacia")
    def test2(self):
        q = Queue(1)
        q.enqueue(5) # Ingresamos el elemento 5
        x = q.dequeue()
        self.assertEqual(x == 5,True,"deberia ser 5")

    def test4(self):
        q = Queue(1)
        self.assertEqual((q.empty() and  q.full()), False, "Tiene que ser falso")


if __name__ == '__main__':
    unittest.main()