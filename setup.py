from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: MacOS :: MacOS X',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='firebotpy',
    version='1.0',
    description='Python library to connect to Firebots API',
    url='https://github.com/whatupcraig/Firebotpy',
    author='Craig Bailey',
    author_email='bailey_craig@me.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['firebot', 'twitch bot', 'twitch', 'fire bot'],
    packages=find_packages(),
    install_requires=['requests']
)
