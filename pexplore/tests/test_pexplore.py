import pytest
import shutil
from pexplore import pexplore


@pytest.fixture(scope="session")
def custom_json(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("custom.json")
    shutil.copyfile("pexplore/test_data/custom.json", fn)
    return fn


def test_open_psort_json(custom_json):
    jf = pexplore.open_psort_json(custom_json)
    assert type(jf) == dict


def test_add_command_line_arguments(custom_json):
    args = pexplore.parse_args(custom_json)
    assert args == "test fail"
