import unittest
from src import this

class TestThis(unittest.TestCase):
    def setUp(self):
        self. x = 8
        self.y = 10

    def testDoIt(self):
        result = this.doit()
        self.x = 22
        self.assertEqual(result, 10)

    def testNowAgain(self):
        result = this.nowagain()
        self.assertIsInstance(result, type(""))

    def testProduct(self):
        result = this.product(self.x, self.y)
        self.assertEqual(result, 80)

    @unittest.expectedFailure
    def testRetTrue(self):
        result = this.retTrue()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()