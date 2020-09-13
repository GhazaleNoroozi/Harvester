#!/bin/sh
sudo apt-get update
packages="python3.6 python3-venv"
for package in $packages;
do
dpkg -l "$package" >/dev/null 2>&1
if [ $? -eq 1 ]
then
sudo apt-get install "python3-pip"
fi
done
v_path=testvenv
mkdir $v_path
python3 -m venv $v_path
cd $v_path || { echo "cd $PATH failed"; exit 155; }
# shellcheck disable=SC1090
. "${v_path}/bin/activate"
bin/pip3 install telethon
bin/python Harvestor/src/Main.py
