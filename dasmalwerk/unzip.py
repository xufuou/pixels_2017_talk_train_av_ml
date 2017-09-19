import zipfile
import os
import shutil

IN_DIR = "archive"
OUT_DIR = "binaries"
PASS = "infected"

if not os.path.isdir(OUT_DIR):
    os.makedirs(OUT_DIR)


if os.path.isdir(IN_DIR):
    for z in os.listdir(IN_DIR):
        print "Unpacking %s ..." %(os.path.join(IN_DIR,z))
        zip_ref = zipfile.ZipFile(os.path.join(IN_DIR,z), 'r')
        zip_ref.extractall(OUT_DIR)
        temp = os.path.join(OUT_DIR,'zippedMalware')
        if not os.path.isdir(temp):
            continue
        for b in os.listdir(temp):
            print "Unpacking %s " %(os.path.join(temp,b))
            zip_ref = zipfile.ZipFile(os.path.join(temp,b), 'r')
            zip_ref.extractall(OUT_DIR,pwd=PASS)
        shutil.rmtree(temp) 


