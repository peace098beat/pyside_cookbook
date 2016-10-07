#! coding:utf-8
"""
ディレクトリ名とパッケージ名が同じ場合．
http://www.glamenv-septzen.net/view/373

nameは識別しなだけ．実際にimportして利用する場合はpackagesの名前を使う
"""
from setuptools import setup, find_packages

# 動く
# setup(
#     name='fifilib5',
#     version='1.0',
#     packages=['fifilib5',
#               'fifilib5.model',
#               'fifilib5.view'],
#     package_dir={'fifilib5': 'fifilib5',
#                  'fifilib5.model': 'fifilib5/model',
#                  'fifilib5.view': 'fifilib5/view'
#                  },
#     test_suite='tests'
# )

# パッケージを手打ちする
# setup(
#     name='fifilib-develop',
#     version='1.0',
#     packages=['fifilib', 'fifilib.model', 'fifilib.view','tests'],
#     test_suite='tests'
# )


# find_packagesを利用
# setup.pyと同階層のディレクトリで__init__.pyがある場合パッケージとして取り込む．
setup(
    # 名前はあくまでも管理名. pipの時とかディレクトリ名に使われる．空白の場合UNKNOWNとなる．
    name='fifilib-develop',
    version='1.0',
    # 自動でパッケージを読み込む. お勧めしない.
    packages=find_packages(),
    # パッケージング後, unittestを実行する(ただし，この階層にパスが通っているので，相対参照なのかには注意)
    test_suite='tests',
    # zip_safe=Trueにすると.eggに圧縮される(デフォルト), Falseでディレクトリに解凍される．
    zip_safe=False,
)

# 所感
# 理想はsrc,testsとしておくほうがいい．
# 相対参照も起きない
setup(
    name="fifilib-dev",
    version='0.0',
    packages=['fifilib', 'fifilib.model', 'fifilib.view'],
    package_dir={'fifilib': 'src',
                 'fifilib.model': 'src/model',
                 'fifilib.view': 'src/view'},
    test_suite='tests',
    zip_safe=False
)
