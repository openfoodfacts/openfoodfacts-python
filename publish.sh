#!/bin/bash
rm -rf dist build *.egg-info
pip install twine
python setup.py sdist bdist_wheel
sudo python -m twine upload dist/*
