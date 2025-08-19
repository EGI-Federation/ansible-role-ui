import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_griduser(host):
    u = host.user("griduser")

    assert u.name == "griduser"
    assert u.group == "gridusers"

    g = host.group("gridusers")

    assert g.exists


def test_ssh_config(host):
    if host.package("openssh-clients").is_installed:
        ssh_config_file = host.file("/etc/ssh/ssh_config")
        assert not ssh_config_file.contains("arcfour")
        assert ssh_config_file.contains("Protocol 2")


@pytest.mark.parametrize(
    "c", ["voms-proxy-init", "voms-proxy-info", "voms-proxy-destroy"]
)
def test_voms_proxy(host, c):
    assert host.exists(c)
