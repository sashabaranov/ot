from setuptools import setup, find_packages

setup(
    name='ot-assignment',
    version='0.1.0',
    url='https://github.com/sashabaranov/ot',
    author='Alexander Baranov',
    packages=['tvapi'],
    install_requires=[
        "click",
        "requests",
        "jwt",
    ],
    tests_require=["pytest"],
    scripts=['scripts/tv-calculate-assoc-score']
)
