import os

import pytest

from tox_ansible.ansible import Ansible


@pytest.mark.parametrize(
    "folder",
    [
        ("tests/fixtures/collection"),
        ("tests/fixtures/expand_collection"),
        ("tests/fixtures/expand_collection_newlines"),
        ("tests/fixtures/not_collection"),
        ("tests/fixtures/has_deps"),
        ("tests/fixtures/nothing"),
    ],
)
def test_with_scenarios(mocker, folder):
    ansible = Ansible(base=folder)
    ansible.options = mocker.Mock()
    ansible.options.ignore_paths = []
    assert ansible.directory == os.path.realpath(folder)


def test_with_full_path():
    ansible = Ansible("/dev")
    assert ansible.directory == "/dev"


def test_scenarios_correct(mocker):
    ansible = Ansible("tests/fixtures/collection")
    ansible.options = mocker.Mock()
    ansible.options.ignore_paths = []
    assert len(ansible.scenarios) == 6
