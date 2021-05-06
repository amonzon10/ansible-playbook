#!/usr/bin/python
# -*- coding: utf-8 -*-


hostname = 'doubi'
add_ip = '192.168.3.41'
netmask_ip = '255.255.255.0'
gateway_ip = '192.168.3.1'

import os

def maj_hostname(hostname):
    hostname = ''
    try:
      os.system("sudo hostnamectl set-hostname hostname")
    except: 
      print("erreur dans le changement de nom")

def rename_file_interfaces():
    try:
      old_file = os.path.join("/etc/network/","interfaces")
      new_file = os.path.join("/etc/network/","interfaces.old")
      os.rename(old_file,new_file)
    except: 
      print("erreur lors du changement du nom du fichier interface")

def maj_address_ip(add_ip, netmask_ip, gateway_ip):
    add_ip = ''
    netmask_ip = ''
    gateway_ip = ''
    file = None
    try:
      file = open("/etc/network/interfaces", "x")
      file.write("source /etc/network/interfaces.d/*\n\nauto lo\niface lo inet loopback\n\nauto enp0s3\niface enp0s3 inet static\n  address add_ip\n  netmask netmask_ip\n  gateway gatway_ip")
    except:
      print("erreur dans la configuration de l'adresse ip")
    finally:
      file.close()


maj_hostname(hostname)
rename_file_interfaces()
maj_address_ip(add_ip, netmask_ip, gateway_ip)



