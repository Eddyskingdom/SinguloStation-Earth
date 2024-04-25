##TODO: MAKE THIS COMPATIBLE WITH NON-TGS INSTALLATIONS!!

import os
import shutil
import time

currdir = os.path.dirname(os.path.abspath(__file__))
lines = open(os.path.join(currdir,"paths.txt"))
all_lines = lines.readlines()
mdir = all_lines[1]
mdir = mdir.replace("\n", "")
mdir = mdir.replace("mdir:", "")
port = all_lines[2]
port = port.replace("\n", "")
port = port.replace("port:", "")
byonddir = all_lines[3]
byonddir = byonddir.replace("\n", "")
byonddir = byonddir.replace("byond_dir:", "")
print(port)
t1 = time.time()

os.chdir("{}SinguloStation-Earth".format(mdir))
print("Rebuilding binaries...")

os.system('"{}/bin/dm earth.dme'.format(byonddir))
os.system("cd")

print("Copying binaries...")
dmb = os.path.join(mdir,'SinguloStation-Earth/Game/Live/earth.dmb')
rsc = os.path.join(mdir,'SinguloStation-Earth/Game/Live/earth.rsc')

shutil.copyfile(dmb, '{}earth.dmb'.format(mdir))
shutil.copyfile(rsc, '{}earth.rsc'.format(mdir))

t2 = time.time() - t1

print("Finished updating all directories in {} seconds".format(t2))
print("Started server on port {}.".format(port))
os.system("{}dreamdaemon {}SinguloStation-Earth/Game/Live/earth.dmb {} -trusted -logself -webclient".format(byonddir,mdir,port))
