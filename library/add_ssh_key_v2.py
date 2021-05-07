#!/usr/bin/python
# -*- coding: utf-8 -*-


DOCUMENTATION='''
module: add_ssh_key
author: Antoine MONZON
description: Module qui permet d'ecrit du text dans un fichier

option:
  path_file_key:
    description: chemin du fichier ou mettre la cle ssh
    required: yes
  key_ssh:
    description: clef ssh
    required: yes
'''

EXEMPLES='''
- name: "add ssh key in file authorized_key"
  add_ssh_key:
    path_file_key: /home/administrateur/.ssh/authorized_key
    key: clef ssh 
'''

RETURN='''
results:
  description: clef ssh
'''


from ansible.module_utils.basic import *

def add_ssh_key(file_key, key):
    file = None
    try:
      file = open(file_key, "w")
      file.write(key)
    except: 
      print("erreur dans l'ecriture de la clef")
    finally:
      file.close()

def read_file_key(file_key):
    data = ''
    file = None
    try:
      file = open(file_key, "r")
      data = file.read()
      file.close()
    except:
      return ''  
    return data

def main():
    changed = False
    fields = {
        "path_file_key": {"required": True, "type": "str"},
        "key_ssh": {"required": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=fields)

    file_key = module.params['path_file_key']
    key = module.params['key_ssh']
    
    if read_file_key(file_key) != key:
      add_ssh_key(file_key, key)
      changed=True
    data = read_file_key(file_key)
    module.exit_json(changed=changed, result=data)

if __name__ == "__main__":
    main()
