from distutils.core import setup
import setuptools

with open('./version.txt', encoding='utf8') as f:
    version = f.read().strip()

with open('./README.md', 'r', encoding='utf8') as f:
    long_description = f.read()

with open('./requirements.txt', 'r', encoding='utf8') as f:
    install_requires = list(map(lambda x: x.strip(), f.readlines()))

setup(
    name='ltp_server',
    version=version,
    description="a simple LTP service implemented in Python based on FastAPI",
    author='lightsmile',
    author_email='iamlightsmile@gmail.com',
    url='https://github.com/smilelight/ltp_server',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'ltp_server=ltp_server.server:run'
        ]
    },
    package_data={
        'ltp_server': ['*.yml']
    },
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
)
