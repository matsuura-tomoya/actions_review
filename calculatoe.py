"""
シンプルな計算を行うためのモジュール。

このモジュールは、四則演算と指定した回数だけ挨拶を返す機能を提供します。
ドキュメント自動生成のテストに適しています。
"""


class Calculator:
    """
    四則演算を行う計算機クラス。

    Attributes:
        result (int | float): 計算結果を保持します。
    """

    def __init__(self) -> None:
        """
        Calculatorのインスタンスを初期化します。
        """
        self.result = 0

    def add(self, a: int, b: int) -> int:
        """
        2つの整数を加算します。

        Args:
            a (int): 1つ目の数値。
            b (int): 2つ目の数値。

        Returns:
            int: 2つの数値の和。
        """
        self.result = a + b
        return self.result

    def subtract(self, a: int, b: int) -> int:
        """
        一方の整数からもう一方の整数を減算します。

        Args:
            a (int): 引かれる数。
            b (int): 引く数。

        Returns:
            int: 減算の結果。
        """
        self.result = a - b
        return self.result

    def multiply(self, a: int, b: int) -> int:
        """
        2つの整数を乗算します。

        Args:
            a (int): 1つ目の数値。
            b (int): 2つ目の数値。

        Returns:
            int: 2つの数値の積。
        """
        self.result = a * b
        return self.result

    def divide(self, a: int, b: int) -> float:
        """
        一方の整数をもう一方の整数で除算します。

        Args:
            a (int): 割られる数。
            b (int): 割る数。

        Returns:
            float: 除算の結果。

        Raises:
            ValueError: 0で除算しようとした場合に発生します。
        """
        if b == 0:
            raise ValueError("0で割ることはできません。")
        self.result = a / b
        return self.result


def greet(name: str, times: int = 1) -> str:
    """
    指定された回数だけ挨拶を生成します。

    Args:
        name (str): 挨拶する相手の名前。
        times (int, optional): 挨拶を繰り返す回数。デフォルトは1回。

    Returns:
        str: 生成された挨拶の文字列。

    Examples:
        >>> greet("Alice")
        'Hello, Alice!\\n'
        >>> greet("Bob", 3)
        'Hello, Bob!\\nHello, Bob!\\nHello, Bob!\\n'
    """
    return "".join([f"Hello, {name}!\n" for _ in range(times)])


if __name__ == "__main__":
    # このファイルが直接実行された場合の簡単な使用例
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")

    print(greet("World", 3))
