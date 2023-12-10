from setuptools import setup, find_packages

setup(
    name='creodamo',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'celery', 'flask', 'jwt', 'redis', 'requests', 'websockets'
    ],
    entry_points={
        'console_scripts': [
            'creodamo=run:main'
        ]
    }
)
