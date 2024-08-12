from setuptools import setup, find_packages

setup(
    name='your_project_name',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'kafka-python',
        'influxdb',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'your_project_name=your_project_name.main:main',
        ],
    },
    include_package_data=True,
    description='Your project description',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/yourprojectname',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
