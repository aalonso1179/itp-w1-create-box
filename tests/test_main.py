import unittest

from create_box import create_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

boarder_box_expected = """
xxxx
x  x
x  x
xxxx
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_large_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)

    def test_boarder_box(self):
        self.assertEqual(create_box(4, 4, 'x', False), boarder_box_expected)
    # Add your own test using third_box_expected
