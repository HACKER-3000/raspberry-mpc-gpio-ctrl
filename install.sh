#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

mkdir /opt/mpc-btns

cp * /opt/mpc-btns

cd /opt/mpc-btns

chmod +x mpc-btns.py

cp mpc-btns.service /etc/systemd/system

systemctl enable mpc-btns.service

systemctl start mpc-btns.service
