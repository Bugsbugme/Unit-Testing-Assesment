import unittest

from Program1 import count_characters


class testCases(unittest.TestCase):
    # test with upper case characters
    def testUpperCase(self):
        # arrange
        sut = count_characters('Hello')
        # act
        expected = [1, 4, 0]
        # assert
        self.assertEqual(sut, expected)

    # test with other characters
    def testOtherChars(self):
        # arrange
        sut = count_characters('email@email.com')
        # act
        expected = [0, 13, 2]
        # assert
        self.assertEqual(sut, expected)

    # this test should fail because it uses the wrong assertion
    def testFail(self):
        # arrange
        sut = count_characters('email@email.com')
        # act
        expected = [0, 10, 2]
        # assert
        self.assertNotEqual(sut, expected)


if __name__ == "__main__":
    # run the tests
    unittest.main()
