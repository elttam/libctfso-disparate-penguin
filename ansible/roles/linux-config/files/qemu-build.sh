#!/bin/sh

# enable source repos
sudo cp /etc/apt/sources.list /etc/apt/sources.list.save
sudo sed -i 's/# deb-src/deb-src/' /etc/apt/sources.list
sudo apt-get update

# get build dependencies of qemu package
sudo apt-get -y build-dep qemu

# make sure we're at home
cd ~/

# clean any stale builds
sudo rm -rf qemu-5.0.0-rc2*

# remove any existing qemu installations
sudo apt-get -y purge "qemu*"
sudo apt-get -y autoremove

# build qemu from source
wget https://download.qemu.org/qemu-5.0.0-rc2.tar.xz 2>/dev/null
tar xvJf qemu-5.0.0-rc2.tar.xz >/dev/null
cd qemu-5.0.0-rc2
./configure --target-list=arm-linux-user,mips-linux-user --interp-prefix=/etc/qemu-binfmt/%M
make
sudo make install

# clean up after ourselves
cd ~/
sudo rm -rf qemu-5.0.0-rc2*
sudo cp /etc/apt/sources.list.save /etc/apt/sources.list
sudo apt-get update
