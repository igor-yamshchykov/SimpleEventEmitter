from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SimpleEventEmitter',
    version='0.0.1',

    description='Simple EventEmitter with basic emit, on, remove_listener',
    long_description=long_description,

    url='https://github.com/pypa/sampleproject',

    author='Ihor Yamshchykov',
    author_email='yamshikov3@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Helper Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='events event emitter',

    py_modules=["EventEmitter"],
)
