# What is this?

This is a simple package to test automated unit tests.

# What does the source code do?

It joins strings together. It's not the important bit.

# What are all the configuration files?

### gitignore

This file tells git which local files to include or ignore in the local repository. For example, since we could generate `__pycache__` directories when running these files, but there is no reason to include those in the git repository, we add these directories to `.gitignore`. In most cases, only source files (e.g. source code, tests, configuration, assets) should be included in a git repository, while generated files do not need to be, and only serve to clutter a git repository.

### pyproject.toml

I don't have a handle on this yet, but this file tells us how to build the python project.
