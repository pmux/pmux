from setuptools import setup, find_packages

setup(
    name='pmux',
    version='0.2',
    packages=find_packages(),
    author='Travis Woodrow <travis.woodrow@latitudeengineering.com>, Chasen Johnson <chase.johnson@latitudeengineering.com>',
    description='An effort toward making distributed, cross-language programs easier to write.',
    url="https://github.com/pmux/pmux",
    install_requires=['nnpy', 'msgpack-python'],
    zip_safe=False,
)
