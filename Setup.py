from setuptools import setup

APP = ['Crypto_Viewer.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5', 'binance'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)