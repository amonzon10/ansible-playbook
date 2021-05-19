# ansible-playbook

Ce depot sert à automatiser des taches répétitives comme ajouter une clef ssh, modifier le nom et l'adresse ip sur un serveur distant.
Il permet aussi d'automatiser l'installation et de configuration d'un serveur Lamp

## Comment l'utiliser

### Prérequis

- Installation des prérequis

```
# On Debian
apt install git python3-pip ansible
```
- Avoir un utilisateur 'administrateur' disposant de tout les droits

- Cloner le depot

```
git clone https://github.com/amonzon10/ansible-playbook.git
cd ansible-playbook
```

### Run

- Mettre à jour le depot

```
git pull
```

- Jouer ansible

```
ansible-playbook playbook_name.yml
```

## Playbook à disposition

### add_ssh.yml

Description: Dépose une clef ssh dans un fichier
Script: library/add_ssh_key.py

```
ansible-playbook add_ssh.key --user administrateur --ask-pass
```

### maj_hostname_ip.yml

Description: Permet de changer le nom de la machine et son adresse ip
Script: library/maj_hostname_ip.py

```
ansible-playbook maj_hostname_ip.yml
```

### install-serveur.yml

Description: installe et configure apache et mariadb
Roles: ansible-role-apache2, ansible-role-mariadb

```
ansible-playbook install-serveur.yml
```
