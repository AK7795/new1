import unittest
import main

class c1(unittest.TestCase):

    def setUp(self):
        self.j = 10
        self.k = 5

    def tearDown(self):
        self.j =0
        self.k =0

    def testc1(self):
        r1 = main.add(self.j,self.k)
        self.assertEqual(r1,self.j+self.k)


    def testc2(self):
        r2 = main.sub(self.j, self.k)
        self.assertEqual(r2, self.j - self.k)

    def testc3(self):
        r1 = main.mul(self.j, self.k)
        self.assertEqual(r1, self.j * self.k)

    def testc4(self):
        r1 = main.div(self.j, self.k)
        self.assertEqual(r1, self.j /self.k)

if __name__== "__main__":
    unittest.main()