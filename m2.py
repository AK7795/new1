import unittest
import main

class c1(unittest.TestCase):
    def testc1(self):
        j=int(input("enter 1 :"))
        k = int(input("enter 2 :"))
        r1 = main.add(j,k)
        self.assertEqual(r1,j+k)


    def testc2(self):
        j=int(input("enter 1 :"))
        k = int(input("enter 2 :"))
        r2 = main.sub(j,k)
        self.assertEqual(r2,j-k)

    def testc3(self):
        j=int(input("enter 1 :"))
        k = int(input("enter 2 :"))
        r3 = main.mul(j,k)
        self.assertEqual(r3,j*k)

    def testc4(self):
        j=int(input("enter 1 :"))
        k = int(input("enter 2 :"))
        r4 = main.div(j,k)
        self.assertEqual(r4,j/k)

if __name__== "__main__":
    unittest.main()