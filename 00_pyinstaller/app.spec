# -*- coding:utf-8 -*-
"""
PyInstaller Manual
https://pythonhosted.org/PyInstaller/spec-files.html
"""
# ===========
# exe Setting
# ===========
block_cipher = None
a = Analysis(['./src/fiapp.py'], # 相対パス()
             pathex=['C:\\Users\\FiFi\\Desktop\\PrefferenceDialog\\src'],
             # binaries=None,
             # datas=[('./src/logger/logging.conf','.'),],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

# Project Search
my_project_tree = Tree(os.path.abspath('./src'))
# Tree('img',prefix='img'), #<--add img dir

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          my_project_tree,
          name='yourapplicationname',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='./src/Icon.ico'
          )

# app = BUNDLE(exe,
#              info_plist={'NSHighResolutionCapable': 'True'},
#              )
