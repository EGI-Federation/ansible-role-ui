import os

import testinfra

# See http://egi-qc.github.io/#SECURITY
# World-writable files and directories are dangerous since they allows anyone
# to modify them, several vulnerabilities in recent years have been due to
# world-writable files and directories being present when they should not be.
# No product should include or create world writable files in order to prevent
# new vulnerabilities being introduced in the future.

# What to check
# Verifier must assure that the product does not include or
# creates world-writable files or directories. If any world-writable files are
# required for the normal operation of the service, these should be documented
# by the Techonology Provider, a ticket reporting the files must be opened.
#  Logs and config files must not be world-writable.

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


# repoquery --requires
# HT
def test_world_writable_files(host):
    cmd = (
        "find /tmp -type d ( -perm -g+w -or -perm -o+w ) "
        + "-exec ls -adl {} ; |grep -v tmp"
    )
    assert testinfra.check_output(cmd) == ""
