#! coding:utf-8
"""
ディレクトリ名とパッケージ名が同じ場合．
http://www.glamenv-septzen.net/view/373

"""
from setuptools import setup, find_packages


# 所感
# 理想はsrc,testsとしておくほうがいい．
# 相対参照も起きない
setup(
    # 名前はあくまでも管理名. pipの時とかディレクトリ名に使われる．空白の場合UNKNOWNとなる．
    name="fifilib-dev",
    version='0.0',
    # 面倒だけど初心者はパッケージ名を書く
    packages=['fifilib', 'fifilib.model', 'fifilib.view', 'fifilib.tests'],
    # 面倒だけど初心者はパッケージとディレクトリの関連付けを行う
    package_dir={'fifilib': 'src',
                 'fifilib.model': 'src/model',
                 'fifilib.view': 'src/view',
                 'fifilib.tests':'tests'},
    # 面倒だけど初心者はunittestを書くように心がける
    test_suite='tests',
   # zip_safe=Trueにすると.eggに圧縮される(デフォルト), Falseでディレクトリに解凍される．
    zip_safe=False
)
