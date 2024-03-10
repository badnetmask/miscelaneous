# Introduction
This is a very basic Ansible playbook that helps install Pi-Hole with DNS over HTTPS (DoH) support.
I'm using this to quickly configure a Raspberry Pi or a small VM with direct install (NOT containers).

# Prerequisites
- You accept using (OpenDNS)[https://support.opendns.com/hc/en-us] as your DoH provider.
  - I may add othe providers later, just need time to test.
- A host running with Debian, or a variant.
  - I may be able to support other distros later, just need time to test.
- You can SSH without password.
- You can SUDO without password.

# How to use
- Clone this repository.
- Modify [inventory.yaml](inventory.yaml).
```
all:
  hosts:
    debian: <-- this is whatever you want to call your host
      ansible_host: 192.168.122.197 <-- this is the IP address of your host
      network_gateway: 192.168.122.1 <-- this is your network router/default gateway
      network_interface: enp1s0 <-- this is the host's network interface name
  vars:
    network_dns: 208.67.222.222 208.67.220.220
    doh_server: doh.opendns.com
```
- Execute.
```
ansible-playbook -i inventory.yaml pihole-doh.yaml
```

# How to test if everything is working
- To confirm that DoH is working, you need to SSH into the host itself.
```
dig @127.0.0.1 -p 5053 www.google.com
```
- To confirm that Pi-Hole is working, you can run this from another host.
```
dig @<host-ip> www.google.com
```

# If you need help
Feel free to post an issue here, or [reach out to me on Mastodon](https://hachyderm.io/@badnetmask).
