import subprocess
import sys

packages = [
    'tensorflow',
    'torch',
    'transformers',
    'streamlit',
    'langchain',
    'paramiko',
    'opencv-python',
    'scikit-learn',
    'matplotlib',
    'pandas',
    'numpy',
    'scipy',
    'nltk',
    'spacy',
    'sentence-transformers',
    'openai',
    'tqdm',
    'requests',
    'beautifulsoup4',
    'flask',
    'fastapi',
    'uvicorn',
    'pymupdf',
]

for package in packages:
    print(f'Installing {package}...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    print(f'{package} installed successfully.')
