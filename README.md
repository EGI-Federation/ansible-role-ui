# User Interface Role

[![Docker Repository on Quay](https://quay.io/repository/egi/ui/status "Docker Repository on Quay")](https://quay.io/repository/egi/ui)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1442700.svg)](https://doi.org/10.5281/zenodo.1442700)

This role provisions a UMD User Interface. It contains the client libraries of
the middleware distribution, for interacting with the various infrastructure
services, and is based on the
[VOMS-client role](https://galaxy.ansible.com/egi-foundation/voms-client).

## Using

This repository is kept under continuous integration. The role has been
expressed into the [UI container](https://quay.io/repository/egi/ui) during the
CI phase and can be immediately re-used, or can be applied to base images of
your favourite platform - bare metal, cloud or local vms. A generic `griduser`
has been created for you :smiley:. See the example playbook below.

### Docker

Running the user interface in a Docker container can be done interactively, or
by starting the container and `exec`ing commands in it:

1. First pull the container image: `docker pull quay.io/egi/ui`
1. Don't forget to mount a volume with your user credentials :
   `-v $HOME/.globus:/home/griduser/.globus`
1. Run interactively:
   `docker run -u griduser -ti --rm --name ui -v $HOME/.globus:/home/griduser/.globus quay.io/egi/ui /bin/bash/`
   (enter the container and do gridcloud things)
1. Run detached:
   `docker run -d -t --rm --name ui quay.io/egi/ui /bin/bash -c 'while true ; do sleep 1000 ; done'`
   1. run things in it: `docker exec ui voms-proxy-init`

## Requirements

No particular requirements are needed, but a typical playbook will need the
[VOMS-client role](https://galaxy.ansible.com/egi-foundation/voms-client)

## Role Variables

See `defaults/main.yml`

## Dependencies

- [EGI-Foundation.umd](https://galaxy.ansible.com/EGI-Foundation/umd)
- [EGI-Fondation.VOMS-client](https://galaxy.ansible.com/EGI-Foundation/VOMS-client)

## Example Playbook

```yaml
- name: Converge
  hosts: all
  roles:
    - {
        role: EGI-Foundation.umd,
        release: 4,
        ca_verification: false,
        tags: "umd",
      }
    - { role: EGI-Foundation.voms-client, tags: "voms" }
    - { role: ansible-role-ui, tags: "ui" }
```

## License

Apache-2.0

## Author Information

- Pablo Orviz @orviz
- Bruce Becker @brucellino

## Citing

If you use this role at your site and publish your infrastructure, please cite
as :

```text
Bruce Becker, & Pablo Orviz. (2018, October 2).
EGI-Federation/ansible-role-ui
Ansible Role: UMD user interface (v0.1.0) (Version v0.1.0).
Zenodo: http://doi.org/10.5281/zenodo.1442700
```
