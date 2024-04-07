# Introduction
I use these files to build my Ansible Execution Evironment to run my playbooks on my home lab.

USE AT YOUR OWN RISK! There are no guarantees these would work for you.

# Prerequisites
- [Ansible Builder](https://ansible.readthedocs.io/projects/builder/en/latest/) is installed.
- [Ansible Navigator](https://ansible.readthedocs.io/projects/navigator/) is installed.
- OPTIONAL:
  - Bitwarden/Vaultwarden: [I use Vaultwarden to manage my secrets](https://mteixeira.wordpress.com/2024/04/04/ansible-vaultwarden/). If you don't want it, just remove all the `addtional_builder_` lines from the [execution-environment.yml](execution-environment.yml) file, as well as the `environment-variables` and `volume-mounts` options from the [ansible-navigator.yaml](ansible-navigator.yaml) file.

# How to use
- Clone this repository.
- [Read this blog post](https://mteixeira.wordpress.com/2024/04/07/reading-secrets-from-vaultwarden-inside-ansible-navigator/).
