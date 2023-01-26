"""
Unit tests for script `pre_gen_project.py <../hooks/pre_gen_project.py>`_.

How to run the tests
--------------------
To run the tests, execute the following command in the project directory:

.. code-block:: bash

	pytest -v ./tests

Unit tests summary
------------------
- :func:`test_main_pregen`: Test `main_pregen` function.
"""

import sys
import pytest
from pathlib import Path

# Since 'hooks' is not a proper Python package, but rather a folder that
# contains scripts, it needs to be added to the import paths.
# To ensure this unit test works independently of where you call `pytest` from,
# these next lines of code will find the 'hooks' directory by searching for it
# in the current directory and on up to two parent directiories as well.
current_dir = Path.cwd()
hooks_dirs = list(current_dir.glob("**/hooks"))
max_tries = 2

while not hooks_dirs and max_tries > 0:
    current_dir = current_dir.parent
    hooks_dirs = list(current_dir.glob("**/hooks"))

if not hooks_dirs:
    raise ModuleNotFoundError("No hooks directory found")

hooks_dir = [str(filepath) for filepath in hooks_dirs if filepath.is_dir()][0]
sys.path.insert(-1, hooks_dir)

from hooks import pre_gen_project
from hooks.pre_gen_project import main_pregen


def test_main_pregen():
    """Test the main_pregen function."""
    setattr(pre_gen_project, "PROJECT_NAME", "test-cookiepy-pre-gen-project")
    setattr(pre_gen_project, "PACKAGE_NAME", "test_cookiepy_pre_gen_project")
    assert main_pregen() is None


if __name__ == "__main__":
    pytest.main([__file__])
