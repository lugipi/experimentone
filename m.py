
#############################################
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#&&````&`&&&&`&``&&&`&``````&&&&`&&&&`&&&`&&#
#&&`&&&&&`&&`&&`&`&&`&&&``&&&&&`&*&&&&`&`&&&#
#&&````&&&``&&&`&&`&`&&&``&&&&&```&&&&&`&&&&#
#&&&&&`&&&``&&&`&&```&&&``&&&&`&&&`&&&`&`&&&#
#&&````&&&``&&&`&&&``&&&``&&&`&&&&`&&`&&&`&&#
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
#############################################

from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
import math as mp
import numpy as np

hfile = open(“?.html”, “r”)
msg_k = ?

f_m = "toy.var"
f_p = "1.f"
f_b = "2.f"
f_k = "swift.key"

t = str()
s = BeautifulSoup(hfile, “html.parser”)

with open(f_k, “rb”) as f_key:
	key = f_key.read()
fernet = Fernet(key)

def f_decyrpt(f_name):
	with open(f_name, “rb”) as f:
		encrypt = f.read()
	decyrpt_s = fernet.decrypt(encrypt)
	return decrypt_s

for m in s.find_all(“p”, class=f_decrypt(f_m)):
	t += m.get_text()

if (isinstance(msg_k, int) == 1):
    x = t.split()
    x = [xp.strip(“.,!;()[]”) for xp in x]
    x = [xp.replace(“’s”, “”) for xp in x]

    p = f_decyrpt(f_p).split()
    b = f_decrypt(f_b).split()
 
    i = 0
    y = []
    for ix in b:
	y.append(round(mp.log(float(ix), int(p[len(x)+i]))*100))
	i=i+1

    xu = []
    for xp in x:
	if xp not in xu:
		xu.append(xp)
    xu.sort()

    for yv in y:
	m += xu[yv]

###################################################    
