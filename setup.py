from setuptools import setup, find_packages

setup(
    name='PyDeployCLI',
    version='0.0.2',
    packages=find_packages(),
    author='yukinotenshi',
    author_email='gabriel.bentara@gmail.com',
    license='MIT',
    url='https://github.com/yukinotenshi/pydeploy',
    install_requires=[
        'requests',
        'psutil',
        'click',
        'bottle',
        'boddle'
    ],
    description='Automatically deploy git repositories',
    keywords='automatic deploy deployment auto pull git',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': ['pydeploy=pydeploy.main:load_config']
    }
)