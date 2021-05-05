#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

def add_ssh_key(file_key, key):
    key = ''
    file = None
    try:
      file = open(file_key, "x")
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
    except:
      print("erreur dans la lecture du fichier")
    finally:
      file.close()
    return data

def main():
    fields = {
        "path_file_key": {"required": True, "type": "str"},
        "key_ssh": {"required": True, "type": "str"}
    }

    module = AnsibleModule(argument_spec=fields)

    file_key = module.params['path_file_key']
    key = module.params['key_ssh']

    add_ssh_key(file_key, key)
    data = read_file_key(file_key)
    module.exit_json(changed=False, result=data)

if __name__ == "__main__":
    main()
