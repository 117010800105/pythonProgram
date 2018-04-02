#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 10:06:49 2018

@author: weizhong
"""

from Bio.Blast.Applications import NcbipsiblastCommandline
from Bio import SeqIO
from Bio.SubsMat import MatrixInfo
import csv
import os

blosumMatrix = MatrixInfo.blosum62
aa = 'A   R   N   D   C   Q   E   G   H   I   L   K   M   F   P   S   T   W   Y   V  B  Z  X *'
aalist = aa.split()

def getPSSMFiles(fastafile,outfileprefix,dbName='swissprot'):
    inputfile = 'input.fasta'
    
    for seq_record in SeqIO.parse(fastafile, 'fasta'):
        print('{} is calculating pssm'.format(seq_record.id),end=" ")
        if os.path.exists(inputfile):
            os.remove( inputfile)
        pssmfile = "".join( (outfileprefix, seq_record.id, '.txt'))
        SeqIO.write( seq_record, inputfile, 'fasta')
        psiblast_cline = NcbipsiblastCommandline( query = inputfile, db=dbName, evalue=0.001,
                                                 num_iterations=3, out_ascii_pssm=pssmfile)
        stdout,stderr=psiblast_cline()
        
        # If seq_record does not have pssm, generating it by blosum62 Matrix
        if not os.path.exists(pssmfile):
            print('\r{} does not have pssm'. format(seq_record.id))
            with open(pssmfile,'w') as pw:
                pw.writelines("  \n")
                pw.writelines("last position-specific scoring matrix computed, weighted \n")
                pw.writelines(aa + '\n')
                s = seq_record.seq
                k = 1
                line=str(k) + ' '
                for alphabet in s:
                    line = line + alphabet + " "
                    for a in aalist:
                        line = line + str( blosumMatrix[(alphabet, a)]) + ' '
                    line = line + '\n'
                    pw.writeline(line)
            
def savePSSMFile2CSV(pssmfilesdir, csvfilesdir):
    listfile = os.listdir(pssmfilesdir)
    for eachfile in listfile:
        filename = eachfile.split('.')
        pssm=[]
        with open(pssmfilesdir + '/' + eachfile, 'r') as pf:
            count = 0
            for eachline in pf:
                count += 1
                if count <=3:
                    continue
                if not len(eachline.strip()):
                    break
                line = eachline.split()
                pssm.append(line[2:22])
        with open(csvfilesdir + '/' + filename + '.csv', 'w') as csvfile:
            cfw = csv.writer( csvfile)
            cfw.writerows(pssm)
    