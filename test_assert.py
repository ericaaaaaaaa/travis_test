import unittest


class MyTestCase(unittest.TestCase):
    def test_false(self):
        self.assertTrue(True, "should be True")

    def test_greater(self):
        self.assertGreater(1, 2, "should be greater")

    def test_equal(self):
        self.assertEqual(False, False, "should be equal")


if __name__ == '__main__':
    unittest.main()
