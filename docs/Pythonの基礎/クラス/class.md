---
icon: material/robot
---

# クラス

## クラスの基本

下記のクラスを例に説明します。

```py
--8<-- "docs_src/class.py:basic"
```

### コンストラクタ

コンストラクタは`__init__` (1) で定義します。
{ .annotate }

1.  Dunder（ダンダー）メソッドの一つです。

```py hl_lines="2"
--8<-- "docs_src/class.py:basic"
```

第一引数の`self`(1)は必須です。自身のインスタンスオブジェクトが入ります。
{ .annotate }

1.  変数名は`self`でなくとも動作しますが、慣習として`self`を使います。

第二引数以降は任意で、関数同様に任意の引数を定義できます。任意引数も定義できます。

### インスタンス変数

クラスの変数（プロパティ）は、`self`に対して任意の箇所で代入して行います。

```py hl_lines="3-4"
--8<-- "docs_src/class.py:basic"
```

インスタンス化は、コンストラクタに指定する引数を与えます。

```python
taro = User("Taro", 21)
```

インスタンスのプロパティには`.`でアクセスできます。

```py
print(taro.name)  # => 'Taro'
print(taro.age)  # => 21
```

### インスタンス変数のスコープ

### メソッド（インスタンスメソッド）

メソッドは第一引数に`self`を指定します。

```py hl_lines="6-7"
--8<-- "docs_src/class.py:basic"
```

メソッドも`.`で呼び出します。

```py
taro.hello()  # => 'こんにちは、私はTaroです！'
```

## クラス変数、クラスメソッド

以下のクラスを例に解説します。

```py
class User:
    instance_count: int = 0

    def __init__(self) -> None:
        self.instance_count += 1

    @classmethod
    def print_instance_count(cls) -> str:
        print(f"インスタンスの生成数は{cls.instance_count}個です")
```

### クラス変数の定義

クラス変数は、クラスの直下に`{変数名} = {初期値}`の形で定義します。

```py hl_lines="2"
class User:
    instance_count: int = 0

    def __init__(self) -> None:
        self.instance_count += 1

    @classmethod
    def print_instance_count(cls) -> str:
        print(f"インスタンスの生成数は{cls.instance_count}個です")
```

### クラス変数へのアクセス

クラス変数は、インスタンスからアクセスすることができます。値はクラス全体で共有されます。

```py hl_lines="5"
class User:
    instance_count: int = 0

    def __init__(self) -> None:
        self.instance_count += 1

    @classmethod
    def print_instance_count(cls) -> str:
        print(f"インスタンスの生成数は{cls.instance_count}個です")
```

クラスから直接アクセスすることもできます。

```py
User.instance_count # => 0
```

### クラスメソッドの定義

クラスメソッドは`@classmethod`のアノテーションをつけたメソッドとして定義します。

```py hl_lines="7-9"
class User:
    instance_count: int = 0

    def __init__(self) -> None:
        self.instance_count += 1

    @classmethod
    def print_instance_count(cls) -> str:
        print(f"インスタンスの生成数は{cls.instance_count}個です")
```

第一引数の`cls`(1)は必須です。自身のクラスオブジェクトが入ります。
{ .annotate }

1.  変数名は`cls`でなくとも動作しますが、慣習として`cls`を使います。

`cls.{クラス変数名}`でクラス変数にアクセスできます。

## スタティックメソッド

## インスタンスメソッド、クラスメソッド、スタティックメソッドの使い分け

## 継承
