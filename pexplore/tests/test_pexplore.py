import pytest
import shutil
import json
from pexplore import pexplore

@pytest.fixture(scope="session")
def custom_json(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("custom.json")
    shutil.copyfile("pexplore/test_data/custom.json", fn)
    return fn

def test_open_psort_json(custom_json):
    jf = pexplore.open_psort_json(custom_json)
    assert type(jf) == dict
