# Reader.py を参照するため
import sys, pathlib
sys.path.append(str(pathlib.Path(pathlib.Path(__file__).parent.parent, 'src')))

import unittest
import unittest.mock
import logging
from Target import Target
class ReaderTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__expected = 'target'
    def __del__(self): self.__expected = None

    def test_0(self):
        self.assertEqual(self.__expected, Target().method())
    def test_1(self):
        with self.assertRaises(Exception) as e:
            Target().raise_error()
        self.assertEqual('エラーです。', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
