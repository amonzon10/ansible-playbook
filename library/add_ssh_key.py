#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

def add_ssh_key(file_key, key):
    file = open(file_key, "x")
    file.write(key)
    file.close()

def read_file_key(file_key):
    file = open(file_key, "r")
    data = file.read()
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
    read_file_key(file_key)

    module.exit_json(changed=False, meta=data)

if __name__ == "__main__":
    main()
