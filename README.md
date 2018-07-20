# Role Name

[![Build Status](https://travis-ci.org/EGI-Foundation/ansible-role-ui.svg?branch=master)](https://travis-ci.org/EGI-Foundation/ansible-role-ui) [![Docker Repository on Quay](https://quay.io/repository/egi/ui/status "Docker Repository on Quay")](https://quay.io/repository/egi/ui)

<!-- A brief description of the role goes here. -->

## Requirements

<!--
Any pre-requisites that may not be covered by Ansible itself or the role should be
mentioned here.
For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
-->
No particular requirements are needed.

## Role Variables

<!--
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
-->

## Dependencies

<!--
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.
Use https://galaxy.ansible.com/EGI-Foundation/ roles first if possible.
-->
  - [EGI-Foundation.umd](https://galaxy.ansible.com/EGI-Foundation/umd)
  - [EGI-Fondation.VOMS-client](https://galaxy.ansible.com/EGI-Foundation/VOMS-client)

## Example Playbook

<!--
Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:
-->

```yaml
  - name: Converge
    hosts: all
    roles:
      - { role: EGI-Foundation.umd, release: 4, ca_verification: false, tags: "umd" }
      - { role: EGI-Foundation.voms-client, tags: "voms"}
      - { role: ansible-role-ui, tags: "ui"}
```

## License

Apache-2.0

## Author Information

<!--
Add the relevant contributors
-->