#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            path_file_key    = dict(required=True, type='str'),
            key_ssh         = dict(required=True, type='str'),
        )
    )

file_key = module.params.get('path_file_key')
key = module.params.get('key_ssh')

def add_ssh_key(file_key, key):
    file = open(file_key, "x")
    file.write(key)
    file.close()

def read_file_key(file_key):
    file = open(file_key, "r")
    print(file.read())

add_ssh_key(file_key, key)

results = print(read_file_key(file_key))

module.exit_json(changed=False, results=resultat)  

if __name__ == "__main__": 
    main()
