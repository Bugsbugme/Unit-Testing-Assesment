
import unittest

from Program2 import recur_fibo


class testCases(unittest.TestCase):

    # After 3 loops, the program should output 2
    def testThreeLoop(self):
        # arrange
        sut = recur_fibo(3)
        # act
        expected = 2
        # assert
        self.assertEqual(sut, expected)

    # This test will pass because the assertion
    # does not expect the output to be equal to 2
    def testThreeLoopAlt(self):
        # arrange
        sut = recur_fibo(3)
        # act
        expected = 10
        # assert
        self.assertNotEqual(sut, expected)

    # This test will fail because it is expecting
    # the wrong output
    def testFourLoopFail(self):
        # arrange
        sut = recur_fibo(4)
        # act
        expected = 3
        # assert
        self.assertEqual(sut, expected)


if __name__ == "__main__":
    # run the tests
    unittest.main()
