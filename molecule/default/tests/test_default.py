import os
import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_griduser(host):
    u = host.user('griduser')

    assert u.name == 'griduser'
    assert u.group == 'gridusers'

    g = host.group('gridusers')

    assert g.exists
