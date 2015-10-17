from setuptools import setup

import flake8_strings


def get_long_description():
    description = []
    for file_name in ('README.rst',):
        with open(file_name) as f:
            description.append(f.read())
    return '\n\n'.join(description)


setup(
    name='flake8-strings',
    version=flake8_strings.__version__,
    description='Checker for PEP-8 String Quote Consistency.',
    long_description=get_long_description(),
    keywords='flake8 pep8 string quotes',
    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/flake8-strings',
    license='MIT',
    py_modules=['flake8_strings'],
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'S80 = flake8_strings:StringChecker'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],

)
