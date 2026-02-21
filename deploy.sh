#!/bin/bash

echo "Uploading to Test PyPI..."

twine upload --repository testpypi dist/*

echo "Does everything look correct? (y/N)"
read answer

if [[ $answer != "y" && $answer != "Y" ]]; then
echo "Please fix what's wrong and try again."
exit 1
fi

echo "Uploading to PyPI..."

twine upload dist/*

echo "Deploy complete!"
