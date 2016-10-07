#! coding:utf-8
"""
logging-sample

Python 標準ロギングモジュール logging の使い方メモ
http://www.sakito.com/2012/10/python-logging.html

import traceback
try:
   ...
except:
   log.error(traceback.format_exc())
   raise


レベル 関数  数値  概要
CRITICAL    logging.critical()  50  停止してしまうような致命的な問題用
ERROR   logging.error() 40  重大な問題用
WARNING logging.warning()   30  実行機能で問題が発生した場合用
INFO    logging.info()  20  動作情報表示用
DEBUG   logging.debug() 10  詳細な情報表示用
NOTSET      0   全てを出力。基本的に設定用の値

フォーマット  概要
%(asctime)s 実行時刻
%(filename)s    ファイル名
%(funcName)s    関数名
%(levelname)s   DEBUG、INFO等のレベル名
%(lineno)d  行番号
%(name)s    呼びだしたログの定義名
%(module)s  モジュール名
%(message)s ログメッセージ
%(process)d プロセスID
%(thread)d  スレッドID

Created by 0160929 on 2016/02/04 14:37
"""
__version__ = '0.0'

import os
import sys
import logging
import logging.config
import traceback

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )
filename = resource_path("logging.conf")

# logging.config.fileConfig(fname='logging.conf')
logging.config.fileConfig(fname=filename)
logger = logging.getLogger('app')

__all__ = ["logger"]