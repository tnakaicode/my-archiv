import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import os
import glob
import tarfile
import argparse

if __name__ == '__main__':
    argvs = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--tar", dest="tar", default="../../Downloads/1908.03795")
    parser.add_argument("--url", dest="url", default="https://arxiv.org/e-print/2005.03337")
    opt = parser.parse_args()
    print(opt, argvs)

    basename = os.path.basename(opt.tar)
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