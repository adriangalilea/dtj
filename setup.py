from setuptools import setup, find_packages

setup(
    name='dtj',
    version='0.1.5',
    packages=find_packages(),
    include_package_data=True,
    description='A tool to convert directory contents to JSON',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/adriangalilea/dtj',
    author='Adrian Galilea Delgado',
    author_email='adriangalilea@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'rich',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'dtj=dtj.main:main',
        ],
    },
)
