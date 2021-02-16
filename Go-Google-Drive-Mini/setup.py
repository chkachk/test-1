from setuptools import setup
from setuptools import find_packages

setup(name='goCHK',
      version='0.1',
      description='Go Choi HongKi',
      install_requires=[
            'numpy', 
            'tensorflow', 
            'keras'
			],
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
