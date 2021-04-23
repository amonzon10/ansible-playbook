file_key = "/home/administrateur/.ssh/id_rsa.pub"

#recupérer la clef ssh local
def recup_local_key(file_key):
  file = open(file_key, "r")
  key = file.read() 
  file.close()
  return key
