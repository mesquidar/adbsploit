from setuptools import setup, find_packages

setup(
    name='adbsploit',
    version='0.1',
    author='Ruben Mesquida',
    author_email='16049893+mesquidar@users.noreply.github.com',
    description="A python based tool for exploiting and managing Android devices via ADB",
    url='https://github.com/mesquidar/adbsploit',
    packages=find_packages(),
    py_modules=['adbsploit'],
    install_requires=[
        'setuptools~=49.2.0',
        'colorama',
        'adbutils',
        'pyfiglet',
        'rich'
    ],
    entry_points={
        'console_scripts': ['adbsploit=adbsploit.adbsploit:main'],
    },
)