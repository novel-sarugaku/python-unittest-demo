# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
# 【処理流れ】
# def → 関数を作る
# return → 結果を返す
# class → グループを作る
# self.assertEqual(実際の結果, 期待する結果) → 同じかどうかチェック！
# unittest.main() → テストを始める合図
# ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
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
