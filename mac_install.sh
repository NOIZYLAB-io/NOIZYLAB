#!/bin/bash
pip3 install -r ../backend/requirements.txt
cd ../remote/relay && npm install
cd ../../frontend && npm install
echo "NoizyOS installed"
