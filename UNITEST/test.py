import unittest
import main


class TestMain(unittest.TestCase):

    def test_do_stuff(self):
        test_param = 10
        result = m.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        tes_param = "10"
        result = m.do_stuff(tes_param)
        self.assertEqual(result, 15)

    def test_do_stuff3(self):
        test_param = None
        result = m.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)


if __name__ == "__main__":
    unittest.main()
