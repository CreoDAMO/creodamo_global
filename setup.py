from setuptools import setup, find_packages

setup(
  name='creodamo',
  version='0.2',  
  packages=find_packages(),
  
  install_requires=[
    'celery', 
    'flask',
    'jwt',
    'redis',
    'requests',
    'websockets',

    # Add fixed versions
    'numpy==1.26.2',  
    'Django==5.0',
    'TensorFlow==2.11.1' 
  ],

  entry_points={
    'console_scripts': [
      'creodamo=run:main'
    ]
  }
)
