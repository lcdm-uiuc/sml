from setuptools import setup

setup(name='sml',
    version='0.1',
    description='SQL like language for machine learning applications',
    url='https://github.com/UI-DataScience/ML-SQL',
    author='Neeraj Asthana, Michael Hao',
    author_email='neeasthana@gmail.com, mike.hao@yahoo.com',
    license='UIUC',
    install_requires=['markdown','pandas', 'pyparsing', 'requests', \
    'scikit-learn'],
    packages=["sml",],
    zip_safe=False)
