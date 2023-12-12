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
    'Django==4.1.5',
    'TensorFlow==2.3.1' 
  ],

  entry_points={
    'console_scripts': [
      'creodamo=run:main'
    ]
  }
)
