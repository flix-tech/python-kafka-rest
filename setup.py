from setuptools import setup, find_packages

about = {}


with open('./kafka_rest/__version__.py') as fh:
    exec(fh.read(), about)

setup(
    name='python-kafka-rest',
    version=about['__version__'],
    description='Python Client for Kafka REST Proxy.',
    long_description='',
    url='https://github.com/flix-tech/python-kafka-rest',

    author='Bastian Venthur',
    author_email='bastian.venthur@flixbus.com',

    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='kafka rest proxy',
    packages=find_packages(),
    #install_requires=[],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'kafka-rest = kafka_rest.__main__:main']
    },

)
