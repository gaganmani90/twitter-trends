from setuptools import setup, find_packages

setup(
    name='twitter',
    packages=['twitter'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    python_requires='3.8.0',
    author='Gagan Mani',
    author_email="gaganmani90@gmail.com",
    version="1.0.0",
    zip_safe=False
)