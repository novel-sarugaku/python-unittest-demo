# ユニットテストの追加（＝テストコードの作成）

import unittest
from hello import get_hello

class TestHello(unittest.TestCase):
    def test_get_hello(self):
        self.assertEqual(get_hello(), "200 OK Hello, World!")

if __name__ == '__main__':
    unittest.main()
