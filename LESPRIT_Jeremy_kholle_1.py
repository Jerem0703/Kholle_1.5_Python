#!/usr/bin/python3.6
#LESPRIT_Jeremy_kholle_1.py
#utilitaire en python
#LESPRIT Jérémy
#24/11/2018


import argparse
import csv
import statistics
from statistics import mean

parser = argparse.ArgumentParser()
parser.add_argument ("-l", help="affiche le contenu du fichier", action="store_true", dest="l")
parser.add_argument ("-a", help="écrit dans le fichier", action="store", dest="a", nargs='+')
parser.add_argument ("-c", help="supprime tous les éléments du fichier", action="store_true", dest="c")
parser.add_argument ("--max", help="affiche le plus grand nombre du fichier", action="store_true", dest="max")
parser.add_argument ("--min", help="affiche le plus petit nombre du fichier", action="store_true", dest="min")
parser.add_argument ("--moy", help="affiche la moyennes des nombres du fichier", action="store_true", dest="moy")
parser.add_argument ("--sum", help="affiche la somme des nombres du fichier", action="store_true", dest="sum")
parser.add_argument ("-t", help="affiche le contenu du fichier par ordre croissant", action="store_true", dest="t")
parser.add_argument ("--desc", help="affiche le contenu du fichier par ordre décroissant", action="store_true", dest="desc")
args = parser.parse_args()

tab = []
fname = "data.csv"
file = open(fname , "r")
try:
    reader = csv.reader(file)
    for row in reader:
        tab.append(int(row[0]))
finally:
    file.close()

if args.l == True:
    print (tab)

if args.a: 
    for elem in args.a:
        tab.append(int(elem))
    file = open(fname , "w")
    try:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows([elem] for elem in tab)
    finally:
        file.close()

if args.c == True:
    file = open(fname , "w")
    try:
        del (tab)
    finally: 
        file.close()

if args.max == True:
    file = open(fname , "r")
    try: 
        print (max(tab))
    finally:
        file.close()

if args.min == True:
    file = open(fname , "r")
    try: 
        print (min(tab))
    finally:
        file.close()

if args.moy == True:
    file = open(fname , "r")
    try: 
        list=tab
        moyenne=mean(list)
        print(moyenne)
    finally:
        file.close()

if args.sum == True:
    file = open(fname , "r")
    try: 
        list=tab
        somme = sum(list)
        print(somme)
    finally:
        file.close()

if args.t == True:
    file = open(fname , "r")
    try: 
        tab.sort()
        print(tab)
    finally:
        file.close()

if args.desc == True:
    file = open(fname , "r")
    try: 
        tab.sort(reverse=True)
        print(tab)
    finally:
        file.close()