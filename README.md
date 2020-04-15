# Overview

libctfso-disparate-penguin is a bundle of Linux CTF challenges not requiring
memory corruption to solve.

Works out of the box on my machine, YMMV - PR's welcome.

# Prerequisites

To use this bundle you should have [Vagrant](https://www.vagrantup.com)
installed along with one of the following hypervisors:

* Virtualbox
* Hyper-V
* Parallels
* libvirt+QEMU
* VMWare Desktop (should work but not tested)

If you know what you're doing and prefer to manage deployment yourself, you can
simply run the [Ansible](https://www.ansible.com/)
[playbook](./ansible/site.yml) on a [Ubuntu Xenial
amd64](http://releases.ubuntu.com/xenial/) target.

## Notes

If you are using Parallels or libvirt+QEMU, please ensure you have `rsync`
installed locally.

If this is your first time using Vagrant with libvirt, please run `vagrant
plugin install vagrant-libvirt`.

If this is your first time using Vagrant with Parallels, please run `vagrant
plugin install vagrant-parallels`.

If this is your first time using Vagrant with Hyper-V, please run all commands
from an Administrator console. In addition, you will be asked to enter your
Windows username/password to enable shared folder support for provisioning.

# Usage

The following command will download a Ubuntu 16.04 VM template from VagrantHub,
create a new virtual machine for 'libctfso-disparate-penguin', and build/install
challenges under the `/challenges` directory of the VM:

**Note:** This can take a while the first time you run it depending on your host
specs and internet connection.

```sh
vagrant up
```

You can re-provision anytime with:

```sh
vagrant provision
```

You can connect to the virtual machine with:

```sh
vagrant ssh
```

This will login to the virtual machine using the 'vagrant' user account,
which has `sudo` privileges so that you can install any additional packages that
you want.

You can stop the virtual machine with:

```sh
vagrant halt
```

And delete the virtual machine with:

```sh
vagrant destroy
```

# Challenges

You should switch to the 'hahn' user account (password = 'hahn') when you are
ready to play:

```sh
su - hahn
```

All challenges can be found under the `/challenges/` directory.

Difficulty estimates are relative to other challenges in this bundle.

---

**Title:** hideandseek  
**Category:** Linux Misc  
**Flag:** `libctf{2c8cb434-2d3b-426a-b5a4-97ebd038a7ef}`  
**Relative Difficulty:** Trivial  

---

**Title:** alpha  
**Category:** Linux Misc  
**Flag:** `libctf{6c793a89-9022-479a-9d47-609d49107d11}`  
**Relative Difficulty:** Trivial  

---

**Title:** opensesame  
**Category:** Linux Misc  
**Flag:** `libctf{5fc205d0-207b-42df-8958-b9ab1b50b56e}`  
**Relative Difficulty:** Easy  

---

**Title:** less0nlearned  
**Category:** Linux Misc  
**Flag:** `libctf{a9552cda-f0df-4264-a878-75a838e976dd}`  
**Relative Difficulty:** Trivial  

---

**Title:** whatTHEarch  
**Category:** Linux Misc  
**Flag:** `libctf{b34bc9c7-4910-4ed4-8bca-d5e32d0ea0f1}`  
**Relative Difficulty:** Moderate  

---

**Title:** catwalk  
**Category:** Linux Misc  
**Flag:** `libctf{a9094223-f27a-4607-acfd-9594633cbed8}`  
**Relative Difficulty:** Moderate  

---

**Title:** einstein  
**Category:** Linux Misc  
**Flag:** `libctf{87b5c0f8-e33c-40b6-9e9a-0994dea16858}`  
**Relative Difficulty:** Moderate  

---

**Title:** randex  
**Category:** Linux Misc  
**Flag:** `libctf{ea979622-62cb-43f6-b086-bd75b45172e4}`  
**Relative Difficulty:** Moderate  

---

**Title:** speedway  
**Category:** Linux Misc  
**Flag:** `libctf{2d2df12a-21f7-441a-b03a-30367082872c}`  
**Relative Difficulty:** Easy  

---

# Hints

Each challenge directory should have everything you need to figure out a plan of
attack. If you really want, you can treat this source repository as an oracle by
asking it questions like:

```
hahn@apocalypse:~/libctfso-disparate-penguin/ansible/roles$ grep -iR 'randomize_va_space' . >/dev/null && true || false
hahn@apocalypse:~/libctfso-disparate-penguin/ansible/roles$ echo $?
0
hahn@apocalypse:~/libctfso-disparate-penguin/ansible/roles$ grep -iR 'idontexist' . >/dev/null && true || false
hahn@apocalypse:~/libctfso-disparate-penguin/ansible/roles$ echo $?
1
hahn@apocalypse:~/libctfso-disparate-penguin/ansible/roles$ 
```
