import os

import pytest
import testinfra.utils.ansible_runner

# See http://egi-qc.github.io/#INSTALLATION
# Packages must install without issues in a machine configured without any
# external repositories (valid repositories are the standard OS repo, UMD repo
# and EPEL repo for RH based distros)
# Packages must follow the OS policies (name of packages, use of filesystem
# hierarchy, init scripts, ...). For any detected issue, open a ticket.
# Packages must be signed (or the repository where they are fetched from is
# signed for Debian-based distros)

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def packages():
    listfile = open("list.txt", "r")
    packages = listfile.read().splitlines()
    return packages


@pytest.mark.parametrize("pkg", packages())
def test_packages(host, pkg):
    assert host.package(pkg).is_installed
    assert host.package(pkg)
    assert host.package(pkg).version
