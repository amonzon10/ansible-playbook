#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

hostname = 'doubi'
add_ip = '192.168.3.41'
netmask_ip = '255.255.255.0'
gateway_ip = '192.168.3.1'

import os

def maj_hostname(hostname):
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
    file = None
    try:
      file = open("/etc/network/interfaces", "w")
      file.write("source /etc/network/interfaces.d/*\n\nauto lo\niface lo inet loopback\n\nauto enp0s3\niface enp0s3 inet static\n  address " + add_ip + "\n  netmask " + netmask_ip + "\n  gateway " + gatway_ip)
    except:
      print("erreur dans la configuration de l'adresse ip")
    finally:
      file.close()

def return_new_hostname():
    return_hostname = ''
    try:
     return_hostname = os.system("hostname")
    except:
      print("erreur dans le hostname")
    return return_hostname

def return_new_ip():
    data = ''
    file = None
    try:
      file = open("/etc/network/interfaces", "r")
      data = file.read()
      file.close()
    except:
      return ''
    return data

def main():
    changed = False
    fiels = {
            "hostname": {"required": True, "type": "str"},
            "add_ip": {"required": True, "type": "str"},
            "netmask_ip": {"required": True, "type": "str"},
            "gateway": {"required": True, "type": "str"}
            }

    module = AnsibleModule(argument_spec=fiels)

    hostname = module.params['hostname']
    add_ip= module.params['add_ip']
    netmask_ip = module.params['netmask_ip']
    gateway_ip = module.params['gateway_ip']

    if return_new_hostname() != hostname:
      maj_hostname(hostname)
      changed = True

    if return_new_ip != "source /etc/network/interfaces.d/*\n\nauto lo\niface lo inet loopback\n\nauto enp0s3\niface enp0s3 inet static\n  address " + add_ip + "\n  netmask " + netmask_ip + "\n  gateway " + gatway_ip:
      rename_file_interfaces()
      maj_address_ip(add_ip, netmask_ip, gateway_ip)
      changed = True

    if changed = False:
      module.exit_json(changed=changed, result="Il n'y a pas eu de changement")

    if changed = True:
      module.exit_json(changed=changed, result="Changement effectué")

if __name__ == "__main__":
    main()
 
