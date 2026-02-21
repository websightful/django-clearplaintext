#!/bin/bash

echo "Did you update the CHANGELOG.md and commit the changes? (y/N)"
read answer

if [[ $answer != "y" && $answer != "Y" ]]; then
echo "Please update and commit the changelog before building."
exit 1
fi

echo "Choose version bump type (major, minor, patch):"
read bump_type

if [[ ! ( $bump_type == "major" || $bump_type == "minor" || $bump_type == "patch" ) ]]; then
echo "Invalid bump type. Please choose major, minor, or patch."
exit 1
fi

echo "Removing the old build/ directory..."
rm -fr build

echo "Bumping version to $bump_type..."
bump-my-version bump $bump_type

echo "Building source distribution and wheel..."
python3 setup.py sdist bdist_wheel

echo "Build complete!"
