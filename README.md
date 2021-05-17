# ansible-playbook

Ce depot est fait pour la formation openclassroom pour le projet6

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

```
ansible-playbook add_ssh.key --user administrateur --ask-pass
```

### maj_hostname_ip.yml

Description: Permet de changer le nom de la machine et son adresse ip

```
ansible-playbook maj_hostname_ip.yml
```

### install-serveur.yml

Description: installe et configure apache et mariadb

```
ansible-playbook install-serveur.yml
```
