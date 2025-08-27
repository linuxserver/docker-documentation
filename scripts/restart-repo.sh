#!/bin/env bash

temp=$(mktemp -d)

cp -r docs/deprecated_images "${temp}"
cp -r docs/images "${temp}"

git remote remove origin
git-filter-repo --path docs/images --path docs/deprecated_images --invert-paths --force

mv "${temp}/deprecated_images" docs 
mv "${temp}/images" docs

git add docs/deprecated_images
git add docs/images
git commit -m "Added templated files"

