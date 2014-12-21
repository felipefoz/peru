#! /usr/bin/env python3

# This script is for running peru directly from the repo, mainly for
# development. This isn't what gets installed when you install peru. That would
# be a script generated by setup.py, which calls peru.main.main().

import os
import sys

repo_root = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, repo_root)

import peru.main

print("Running peru from:", os.path.dirname(peru.__file__))

peru.main.main()
