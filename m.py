
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&````&`&&&&`&``&&&`&``````&&&&`&&&&`&&&`&&
&&`&&&&&`&&`&&`&`&&`&&&``&&&&&`&*&&&&`&`&&&
&&````&&&``&&&`&&`&`&&&``&&&&&```&&&&&`&&&&
&&&&&`&&&``&&&`&&```&&&``&&&&`&&&`&&&`&`&&&
&&````&&&``&&&`&&&``&&&``&&&`&&&&`&&`&&&`&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import math as mp
import numpy as np

hfile = open(“?”, “r”)
msg_k = ?

t = str()
s = BeautifulSoup(hfile, “html.parser”)
with open(“swift.key”, “rb”) as f_key:
	key = f_key.read()
fernet = Fernet(key)

def f_decyrpt(f_name):
	with open(f_name, “rb”) as f:
		encrypt = f.read()
	decyrpt_s = fernet.decrypt(encrypt)
	return decrypt_s

for m in s.find_all(“p”, class=f_decrypt(“toy.var”)):
	t += m.get_text()

if (isinstance(msg_k, int) == 1):
    x = t.split()
    x = [xp.strip(“.,!;()[]”) for xp in x]
    x = [xp.replace(“’s”, “”) for xp in x]

    p = 
