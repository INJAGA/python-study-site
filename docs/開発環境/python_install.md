---
icon: material/language-python
---

# Pythonバージョン管理

`uv`は、任意のバージョンのPythonを簡単にインストールし管理することができます。

## 利用可能なバージョンの確認

`uv`コマンドを用い、インストール可能なバージョン一覧を確認することができます。

```bash
uv python list
```

以下は、Windows11で`uv`インストール直後、このコマンドを実行した結果です。

```console
$ uv python list
cpython-3.14.0a4+freethreaded-windows-x86_64-none    <download available>
cpython-3.14.0a4-windows-x86_64-none                 <download available>
cpython-3.13.2+freethreaded-windows-x86_64-none      <download available>
cpython-3.13.2-windows-x86_64-none                   <download available>
cpython-3.12.9-windows-x86_64-none                   <download available>
cpython-3.11.11-windows-x86_64-none                  <download available>
cpython-3.10.16-windows-x86_64-none                  <download available>
cpython-3.9.21-windows-x86_64-none                   <download available>
cpython-3.8.20-windows-x86_64-none                   <download available>
cpython-3.7.9-windows-x86_64-none                    <download available>
pypy-3.10.14-windows-x86_64-none                     <download available>
pypy-3.9.19-windows-x86_64-none                      <download available>
pypy-3.8.16-windows-x86_64-none                      <download available>
pypy-3.7.13-windows-x86_64-none                      <download available>
```

CPython(1)とPyPyそれぞれに対し、バージョン情報が記されています。
{ .annotate }

1.  CPythonはPython言語のC実装です。一般的にPython=CPythonと考えて良いでしょう。その他にもPyPy（Python実装）、Jython（Java実装）などが存在します。

2025/02/11現在Stableリリースされている最新版は

## 最新安定版のインストール

下記コマンドで、実行時点での最新安定版をインストールすることができます。

```console
$ uv python install
Installed Python 3.13.2 in 6.87s
 + cpython-3.13.2-windows-x86_64-none
```

実行後

```console hl_lines="5"
$ uv python list
cpython-3.14.0a4+freethreaded-windows-x86_64-none    <download available>
cpython-3.14.0a4-windows-x86_64-none                 <download available>
cpython-3.13.2+freethreaded-windows-x86_64-none      <download available>
cpython-3.13.2-windows-x86_64-none                   C:\Users\injaga\AppData\Roaming\uv\python\cpython-3.13.2-windows-x86_64-none\python.exe
cpython-3.12.9-windows-x86_64-none                   <download available>
cpython-3.11.11-windows-x86_64-none                  <download available>
cpython-3.10.16-windows-x86_64-none                  <download available>
cpython-3.9.21-windows-x86_64-none                   <download available>
cpython-3.8.20-windows-x86_64-none                   <download available>
cpython-3.7.9-windows-x86_64-none                    <download available>
pypy-3.10.14-windows-x86_64-none                     <download available>
pypy-3.9.19-windows-x86_64-none                      <download available>
pypy-3.8.16-windows-x86_64-none                      <download available>
pypy-3.7.13-windows-x86_64-none                      <download available>
```
