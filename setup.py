from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='twitter',
    packages=['twitter'],
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.8.0',
    author='Gagan Mani',
    author_email="gaganmani90@gmail.com",
    version="1.0.0",
    zip_safe=False
)