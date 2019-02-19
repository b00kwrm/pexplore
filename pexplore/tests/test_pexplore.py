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


def test_get_tags(custom_json):
    jf = pexplore.open_psort_json(custom_json)
    tags = pexplore.get_tags(jf)
    assert type(tags) == dict
    assert tags == {
        "T1156_bash_profile_and_bashrc": 3,
        "T1136_create_account": 1,
        "__type__": "collections.Counter",
        "T1215_Kernel_Modules_and_Extensions": 3,
        "ssh_logs": 4,
        "total": 47,
        "T1078_valid_accounts": 1,
        "T1003_credential_dumping": 24,
        "S0002_mimikatz": 24,
        "T1168_local_job_scheduling": 2,
        "T1098_account_manipulation": 8,
        "T1057_Process_Discovery": 1,
    }
