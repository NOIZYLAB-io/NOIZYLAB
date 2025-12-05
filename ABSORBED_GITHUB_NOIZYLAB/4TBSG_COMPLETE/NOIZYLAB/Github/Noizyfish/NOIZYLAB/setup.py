from setuptools import setup, find_packages

setup(
    name='noizy-fish-orchestrator',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project for managing accounts, 2FA, and audio libraries.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/noizy-fish-orchestrator',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Click',
        'PyYAML',
        'requests',
        'rich',
        'cryptography',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)