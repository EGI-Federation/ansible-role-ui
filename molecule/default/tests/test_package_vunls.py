import os
import testinfra.utils.ansible_runner
import pytest
from distutils.version import LooseVersion  # , StrictVersion
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
# The vulnerability scanner on Quay gives us intelligence on which
# vulnerabilities are exposed by packages included in these images.
# We therefore keep track of those and test to see whether the installed
# version is greater than the one reported as fixing the vulnerability

# Watch the CVEs raised at https://quay.io/repository/egi/ui?tab=tags


@pytest.mark.parametrize_centos7('name,version', [
  ("gnupg2", "2.0.22-5.el7_5"),
  ("python", "2.7.5-69.el7_5"),
  ("python-libs", "2.7.5-69.el7_5"),
  ("bind-license", "61.el7_5.1"),
  ("yum-utils", "1.1.31-46.el7_5"),
  ("yum-plugin-ovl", "1.1.31-46.el7_5"),
  ("yum-plugin-priorities", "1.1.31-46.el7_5"),
  ("yum-plugin-fastestmirror", "1.31-45.el7")])
def test_vulnerable_packages(host, name, version):
    if (LooseVersion(host.system_info.release) >= '7.0.0'):
        p = host.package(name)
        assert p.release >= version


# @pytest.mark.parametrize('name,version', [
#   ("gnupg2", "2.0.22-5.el7_5"),
#   ("python", "2.7.5-69.el7_5"),
#   ("python-libs", "2.7.5-69.el7_5"),
#   ("bind-license", "61.el7_5.1"),
#   ("yum-utils", "1.1.31-46.el7_5"),
#   ("yum-plugin-ovl", "1.1.31-46.el7_5"),
#   ("yum-plugin-priorities", "1.1.31-46.el7_5"),
#   ("yum-plugin-fastestmirror", "1.31-45.el7")])
# def test_vulnerable_packages_centos6(host, name, version):
#     if (LooseVersion(host.system_info.release) < '7.0.0'):
#         p = host.package(name)
#         assert p.release >= version
