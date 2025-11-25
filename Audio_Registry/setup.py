#!/usr/bin/env python3
# ==============================================================================
# METABEAST_CC - Setup & Installation
# ==============================================================================
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text() if readme_path.exists() else ""

setup(
    name="metabeast-cc",
    version="1.0.0",
    author="Rob",
    author_email="rob@fishmusicinc.com",
    description="METABEAST_CC - Audio Canon Command Center",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Noizyfish/NOIZYLAB",
    project_urls={
        "Documentation": "https://github.com/Noizyfish/NOIZYLAB/tree/main/Audio_Registry",
        "Source": "https://github.com/Noizyfish/NOIZYLAB",
        "Tracker": "https://github.com/Noizyfish/NOIZYLAB/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: System :: Archiving",
        "Topic :: Utilities",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pyyaml>=6.0.1",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
        "api": [
            "fastapi>=0.100.0",
            "uvicorn>=0.23.0",
        ],
        "rich": [
            "rich>=13.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "audiocat=tools.audiocat:main",
            "ai-host=tools.ai_host_guide:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": [
            "data/*.yaml",
            "data/*.json",
            "manifests/**/*.yaml",
            "templates/**/*",
            "integrations/*.yaml",
            "integrations/*.json",
        ],
    },
)
