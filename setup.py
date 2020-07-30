from setuptools import setup

setup(
    name='adbsploit',
    version='0.1',
    py_modules=['adbsploit'],
    install_requires=[
        'setuptools~=49.2.0',
        'Click',
        'adb-shell'
    ],
    entry_points={
        'console_scripts': ['adbsploit=adbsploit.adbsploit:cli'],
    },
)