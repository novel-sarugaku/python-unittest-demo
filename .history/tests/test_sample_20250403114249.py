import unittest

def add(a, b):
    return a + b

# unittest.TestCase：テスト専用のクラスになる
# テスト名は「test_」で始めるのがルール
# self.assertEqual(左, 右) ：「左と右が同じかを確かめる。
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# 「このファイルを直接実行したときだけ、テストを実行する」という意味
if __name__ == "__main__":
    unittest.main()
