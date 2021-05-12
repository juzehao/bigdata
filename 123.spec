# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['123.py'],
             pathex=['C:\\users\\zc\\appdata\\local\\programs\\python\\python38-32\\lib\\site-packages', 'C:\\users\\zc\\roaming\\python\\python38\\site-packages', 'C:\\Users\\zc\\PycharmProjects\\untitled18'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='123',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
