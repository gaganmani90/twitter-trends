from setuptools import setup, find_packages

setup(
    name='twitter',
    #packages=['twitter'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    author='Gagan Mani',
    author_email="gaganmani90@gmail.com",
    version="1.0.0",
    zip_safe=False
)