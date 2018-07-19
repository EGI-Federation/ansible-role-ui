import os
import testinfra.utils.ansible_runner
import pytest
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name,version', [
  ("gnupg2", "2.0.22-5.el7_5"),
  ("python", "2.7.5-69.el7_5"),
  ("python-libs", "2.7.5-69.el7_5")])
def test_vulnerable_packages(host, name, version):
    p = host.package(name)
    assert p.release >= version
