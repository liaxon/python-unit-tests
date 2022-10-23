# What is this?

This is a simple package to test automated unit tests.

# What does the source code do?

It joins strings together. It's not the important bit.

# What are all the configuration files?

### README.md

This is not a configuration file. This is the first file that any user should read to learn about what your repository is and how to use it.

### LICENSE

This is also not a configuration file. This gives the legal license for people to use your code. Common licenses include BSD, MIT, and GPL.

### gitignore

This file tells git which local files to include or ignore in the local repository. For example, since we could generate `__pycache__`
directories when running these files, but there is no reason to include those in the git repository, we add these directories to `.gitignore`.
In most cases, only source files (e.g. source code, tests, configuration, assets) should be included in a git repository, while generated
files do not need to be, and only serve to clutter a git repository.

### requirements.txt

This file contains all Python packages that are used when building and running the project.

### requirements_dev.txt

This file contains all (additional) Python packages that are used when developing the project. In particular, it includes packages for
testing and linting. This is kept separate so that people who use your project don't need to worry about downloading these packages, or any
version conflicts with them.

### setup.py

This file is used by `pip` and other packag managers when installing your module.

### setup.cfg

This file contains some metadata (such as author, license, and name) and some project configuration (such as `flake8` settings, `mypy` settings,
and a list of packages). Apparently, the Python community is moving towards including less project configuration here., and more in `pyproject.toml`.

### pyproject.toml

This contains various configurations for your project. This includes building your project (with `[build-system]`), mypy linting (with `[tool.mypy]`),
and pytest options (with `[tool.pytest.ini_options]`). More configurations are moving to this file. It is written in the well-known TOML format.
