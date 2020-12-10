from pexplore import pexplore
from click.testing import CliRunner


#tags = '{"T1156_bash_profile_and_bashrc": 3, "T1136_create_account": 1, "__type__": "collections.Counter", "T1215_Kernel_Modules_and_Extensions": 3, "ssh_logs": 4, "total": 47, "T1078_valid_accounts": 1, "T1003_credential_dumping": 24, "S0002_mimikatz": 24, "T1168_local_job_scheduling": 2, "T1098_account_manipulation": 8, "T1057_Process_Discovery": 1}'

tags = '{"total": 48, "T1003_credential_dumping": 24, "S0002_mimikatz": 24, "T1098_account_manipulation": 8, "T1136_create_account": 1, "T1156_bash_profile_and_bashrc": 3, "T1215_Kernel_Modules_and_Extensions": 3, "ssh_logs": 4, "T1057_Process_Discovery": 2, "T1105_remote_file_copy": 3}'

with open("pexplore/test_data/new_custom.json") as f:
    custom_json = f.read()
    pinfo_file = custom_json.encode("utf-8")


def test_pexplore_cli():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("pinfo_file.json", "wb") as f:
            f.write(pinfo_file)
        result = runner.invoke(pexplore.cli, ["pinfo_file.json"])
        assert result.exit_code == 0
        assert result.output == tags
