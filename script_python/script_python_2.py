file_key = "/home/administrateur/.ssh/authorized_keys"
key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDH+RFhsJels4tiIM7domsHxDiKQ7hJIqAvqAGuZY1+hjGekLutnVXkb+r4cbmQ6wrbrfH8M9+rn+ZVVWQLWonR28LPQf1YAX0kYmt5nhXMBwDWYLhtor4/7nW4exjN21ZbEru5QLEikyIc5CcmT16/MIfr0i7JYnTQ0yDurr8LPsmxglzxQiATh1v671BeBDwIMhgpwY20Y+xa8pKQeKAuIsnorCxMFzvYRdCozfgpoUPmByLwhw2PufC88CtE/S3LB4e8kRBXekd3F3QTMzsmBx+Z3+Af50qljRuk4mWejp6k1M76hI5+TdLEQ8yY7MXKb2XgfmEy6SgoJYpWoYcMohFS1ULeRX930oa1a4+MLNcr6X6OxUH/HYXo0UySe07dncPVQbPpHC/IZt2KL3FKh6OXpUU7+20YHUwPWn9JeL8/ZB3si2l9VZdRDLErkln7fcgBZHhrkzeK7GTejBmAVONVQD60cimRa7ktzLQMiandtNHnCWRTcxAgNp+sojCHjxctxL/WT6XRH9Ft7P5zgDbNKeGaViPsSvfBtfxBfZonsA/wuw0I11URnpFYnZqdumOZaIsNnQs7gznz0sxSJTRDIpYxdN+URxMHJ8YoRxB4uvoMkbWAOD2trkEFOuwKDfz30e2Q6N3ToVVSTExUCQZzq2hDgNf7FmnwYE0P3w== ansible"

def add_ssh_key(file_key, key):
    file = open(file_key, "x")
    file.write(key)
    file.close()

def read_file_key(file_key):
    file = open(file_key, "r")
    print(file.read())

add_ssh_key(file_key, key)
read_file_key(file_key)

