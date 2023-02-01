from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Web App',
    ext_modules=cythonize("Task Manager.py"),
    zip_safe=False,
)