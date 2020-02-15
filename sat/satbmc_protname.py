#!/usr/bin/env python3
import sys
import os
from satbmc import * 
from genResults import *
realpath = (os.path.dirname(os.path.realpath(__file__)))
BIN = "../bin"



def main():
    if len(sys.argv) != 2:
        print("python3 satbmc_protname.py nameOfTheProtocol")
        exit(1)
    print(realpath +"/" + sys.argv[1])
    prot_path = realpath +"/" + sys.argv[1]
    prot_name = sys.argv[1]
    verify(prot_name, prot_path)
    



def afterVerification(nameWithoutNta, k):
    genResultsSMT(nameWithoutNta, k)
    bmc, smt, all = sumResults(nameWithoutNta)
    executeRemoveCommand(createRemoveCommand(nameWithoutNta))
    print("BMC time \t BMC memory")
    print(bmc)
    print()
    print("minissat time \t minisat memory")
    print(smt)
    print()
    print("Time \t\t MAX memory")
    print(all)
    fopen = open(nameWithoutNta + ".dat", 'w')
    fopen.write("BMC time \t BMC memory\n")
    fopen.write(bmc + "\n\n")
    fopen.write("minisat time \t minisat memory\n")
    fopen.write(smt + "\n\n")
    fopen.write("Time \t\t MAX memory\n")
    fopen.write(all + "\n")
    fopen.close()
    print("\nResults saved in " + nameWithoutNta + ".dat")
    print("\nResults saved")
    print()
    print()
    input("Press ENTER to continue")



def verify(prot_name, prot_path):
    nta = prot_path + "/" + prot_name 
    efo = prot_path + "/" + prot_name
    print(nta)
    print(efo)
    k = bmcAlg(nta, BIN, efo, 40)
    afterVerification(nta, k)



main()
