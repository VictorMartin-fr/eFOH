# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['VI-Stream-App.py'],
             pathex=['D:\\z_Developpement\\eConsole - HTTPS\\Script Console\\Main program'],
             binaries=[],
             datas=[('./logo-noir.ico', '.'), ('./logo-blanc.png', '.')],
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
          [],
          exclude_binaries=True,
          name='VI-Stream-App',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='logo-noir.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='VI-Stream-App')
