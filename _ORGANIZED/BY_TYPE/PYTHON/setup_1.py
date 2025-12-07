#!/usr/bin/env python3
"""
setup.py for NOIZY.AI - Consolidated AI Engine
Audio & Music-Centered AI Platform
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), 'r', 
          encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = [line.strip() for line in f 
                   if line.strip() and not line.startswith('#')]

setup(
    name="noizy-ai",
    version="1.0.0",
    author="Noizy Fishes Empire",
    author_email="contact@fishmusicwebsite.com",
    description="Consolidated AI Engine for Audio & Music Processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noizyfish/noizy-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-asyncio>=0.21.0',
            'pytest-cov>=4.1.0',
            'black>=23.11.0',
            'flake8>=6.1.0',
            'mypy>=1.7.0',
            'bandit>=1.7.5',
            'pre-commit>=3.6.0',
            'isort>=5.12.0',
        ],
        'audio': [
            'essentia>=2.1b6.dev1091',
            'madmom>=0.16.1',
            'pyrubberband>=0.3.0',
            'pedalboard>=0.7.7',
        ],
        'ml': [
            'torch>=2.1.0',
            'torchaudio>=2.1.0',
            'transformers>=4.35.0',
            'datasets>=2.14.0',
        ],
        'cloud': [
            'boto3>=1.34.0',
            'azure-storage-blob>=12.19.0',
            'google-cloud-storage>=2.10.0',
        ],
        'monitoring': [
            'prometheus-client>=0.19.0',
            'sentry-sdk>=1.38.0',
            'newrelic>=9.2.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'noizy-ai=noizy_ai.cli:main',
            'noizy-setup=noizy_ai.setup:setup_environment',
            'noizy-test=noizy_ai.test:run_tests',
        ],
    },
    include_package_data=True,
    package_data={
        'noizy_ai': [
            'config/*.json',
            'templates/*.html',
            'static/*.css',
            'static/*.js',
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/noizyfish/noizy-ai/issues",
        "Source": "https://github.com/noizyfish/noizy-ai",
        "Documentation": "https://noizy-ai.readthedocs.io/",
        "Fish Music Website": "https://fishmusicwebsite.com",
    },
    keywords=[
        "ai", "audio", "music", "artificial intelligence", 
        "voice synthesis", "audio processing", "music production",
        "elevenlabs", "openai", "audio mastering", "sound design"
    ],
)