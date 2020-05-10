import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
import glob
import tarfile
import shutil
import requests
from optparse import OptionParser

def split_filename(filename="../temp_20200408000/not_ignore.txt"):
    name = os.path.basename(filename)
    dir_name = os.path.dirname(filename)
    sub_name = os.path.basename(os.path.dirname(filename))
    rootname, ext_name = os.path.splitext(name)
    return name, dir_name, sub_name

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--tar", dest="tar", default="../../Downloads/1908.03795")
    parser.add_option("--url", dest="url", default="https://arxiv.org/e-print/2005.03337")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    filename, url_name, sub_name = split_filename(opt.url)
    print(opt.url)
    res = requests.get(opt.url, stream=True)
    with open("./tmp/" + filename, 'wb') as fp:
        shutil.copyfileobj(res.raw, fp)

    basename = os.path.basename(opt.url)
    base_dir = "arXiv." + basename
    dirnum = len(glob.glob(base_dir))
    print(basename)
    print(dirnum)
    if dirnum == 0:
        os.makedirs("arXiv." + basename)
    
    print(os.getcwd())
    #os.chdir(base_dir)
    tar = tarfile.open(opt.file, "r")
    tar.extractall(base_dir)
    
    #tar = tarfile.open(tar_name, "w")
    #tar.add("./src/")
    #tar.close()
    #
    # python -m tarfile -c monty.tar  spam.txt eggs.txt
    # python -m tarfile -c monty.tar life-of-brian_1979/
    # python -m tarfile -e monty.tar
    # python -m tarfile -e monty.tar  other-dir/
    # python -m tarfile -l monty.tar
    # 
    # Compression
    # tar -zcvf filename.tar.gz directoryname
    #
    # Thaw
    # tar -zxvf filename.tar.gz
    #