"""
Unit tests for script `post_gen_project.py <../hooks/post_gen_project.py>`_.

How to run the tests
--------------------
To run the tests, execute the following command in the project directory:

.. code-block:: bash

	pytest -v ./tests

Unit tests summary
------------------
- :func:`test_remove_file`: Test `remove_file` function.
- :func:`test_create_dotenv`: Test `create_dotenv` function.
"""

import sys
import pytest
from pathlib import Path


current_dir = Path.cwd()
hooks_dirs = list(current_dir.glob('**/hooks'))
max_tries = 2
while not hooks_dirs and max_tries > 0:
	current_dir = current_dir.parent
	hooks_dirs = list(current_dir.glob('**/hooks'))

if not hooks_dirs:
	raise ModuleNotFoundError('No hooks directory found')

hooks_dir = [str(filepath) for filepath in hooks_dirs if filepath.is_dir()][0]
sys.path.insert(-1, hooks_dir)
from hooks.post_gen_project import remove_file, create_dotenv


def test_remove_file():
	"""Test remove_file function."""
	test_path = 'test'
	test_path = Path(test_path + str(hash(test_path))).with_suffix('.txt')
	test_path.touch(exist_ok=True)
	assert test_path.is_file()
	remove_file(test_path)
	assert not test_path.is_file()


def test_create_dotenv():
	"""Test create_dotenv function."""
	create_dotenv()
	with open('.env', 'r') as file:
		assert file.readlines()[
			       0] == 'PROJECT_NAME="{{ cookiecutter.project_name }}"\n'
	remove_file('.env')


if __name__ == "__main__":
    pytest.main([__file__])
