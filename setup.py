from setuptools import setup,find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='autodnd',
   version='0.1',
   description='Add schedule to the gnome do not disturb',
   long_description=long_description,
   license="GPL-3",
   author='Riccardo Isola',
   author_email='riky.isola@gmail.com',
   url="https://github.com/RikyIsola/AutoDND",
   packages=find_packages(),
   scripts=['autodnd']
)
