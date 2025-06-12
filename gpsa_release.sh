#!/bin/bash

# Exit immediately on error
set -e

# Bump version manually first in setup.py before running this!

# Clean previous build artifacts
rm -rf dist/ build/ *.egg-info

# Build new release
python -m build

# Verify the build
twine check dist/*

# Upload to TestPyPI
twine upload --repository testpypi dist/*

echo "✅ Successfully uploaded to TestPyPI!"
