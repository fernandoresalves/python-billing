from distutils.core import setup

setup(
    name='SoneBilling',
    version='0.1.0',
    author='Fernando Resende Alves',
    author_email='fernandoresalves@gmail.com',
    package_dir={'': 'src'},
    packages=['sonebilling', 'sonebilling.test'], 
    url='http://pypi.python.org/pypi/SoneBilling/',
    license='LICENSE.txt',
    description='Client api billing in python',
    long_description=open('README.txt').read(),
    install_requires=[
        "Requests >= 2.18"
    ]
)

