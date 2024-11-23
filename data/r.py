import os
import random
import string

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "_"

did = '/tmp/' + ''.join(random.choice(chars) for _ in range(10))

print("print exit to quit this os")
os.system(f"mkdir {did}\n"
          f"chmod 700 {did}\n"
          f"cd {did}\n"
          "wget https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/x86/alpine-minirootfs-3.20.3-x86.tar.gz\n"
	  "mkdir alpine\n"
          "tar -xzf alpine-minirootfs-3.20.3-x86.tar.gz -C alpine\n"
	  "chroot alpine /bin/sh")
os.system(f"rm -rdf {did}")
exit()
