#recupérer la clef ssh local
def recup_local_key(file_key)
  file = open(file_key, "r")
  key = file.read() 
  file.close()
