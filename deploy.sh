#!/bin/bash
pelican content -o output -s publishconf.py
ghp-import output -b master
git push origin master
