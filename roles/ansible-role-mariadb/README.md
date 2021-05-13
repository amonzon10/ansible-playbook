# Role Ansible : mariadb

Installe et configure mariadb

## Prérequis

* Ansible
* Debian

## Variables du role

* mysqluser_name = nom de l'uilisateur à créer
* mysqluser_host = autorisation de connexion de l'uilisateur à créer
* mysqluser_password = mot de passe de l'uilisateur à créer
* mysqluser_privileges = droit de l'uilisateur à créer
* mariadb_user = nom de l'utilisateur root
* mariadb_password = mot de passe de l'utilisateur root
* mysqldatabase_name = nom de la base à créer

## How to use

```
- hosts: server
  roles:
    - ansible-role-mariadb
```
