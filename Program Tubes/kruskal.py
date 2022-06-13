import DapatkanJalur as co
import pandas as pd

#Config nilai 1
configNilai = {
    "ab":[17],
    "ae":[5],
    "af":[8],

    "ba":[17],
    "bc":[13],
    "bd":[9],
    "bf":[9],
        
    "cb":[13],
    "cd":[2],
    "cg":[12],

    "db":[9],
    "dc":[2],
    "dg":[10],

    "ea":[5],    
    "ef":[20],
    "eg":[13],
    
    "fa":[8],
    "fb":[9],
    "fe":[20],
    "fg":[8],
    
    "gc":[12],
    "gd":[10],
    "ge":[13],
    "gf":[8]
}

jalur = {
    "ab":[],
    "ac":[],
    "ad":[],
    "ae":[],
    "af":[],
    "ag":[],

    "bc":[],
    "bd":[],
    "be":[],
    "bf":[],
        
    "cd":[],
    "ce":[],
    "cf":[],
    "cg":[],

    "de":[],
    "df":[],
    "dg":[],
        
    "ef":[],
    "eg":[],
    
    "fg":[]
}

terkecil = {}
greedy = {}

inputJalur = {
    "ab":['a', 'b'],
    "ac":['a', 'c'],
    "ad":['a', 'd'],
    "ae":['a', 'e'],
    "af":['a', 'f'],
    "ag":['a', 'g'],

    "bc":['b', 'c'],
    "bd":['b', 'd'],
    "be":['b', 'e'],
    "bf":['b', 'f'],
        
    "cd":['c', 'd'],
    "ce":['c', 'e'],
    "cf":['c', 'f'],
    "cg":['c', 'g'],

    "de":['d', 'e'],
    "df":['d', 'f'],
    "dg":['d', 'g'],
        
    "ef":['e', 'f'],
    "eg":['e', 'g'],
    
    "fg":['f', 'g']
}

for key in inputJalur:
    data = co.main(inputJalur[key])
    jalur.update({key : data})

def kruskal():
    for key in inputJalur:
        h = 0
        for i in range(len(jalur[key])-1):
        
            index1 = jalur[key][i][0] + jalur[key][i][1]
            try:
                index2 = jalur[key][i+1][0] + jalur[key][i+1][1] 
            except IndexError:
                pass

            nilaijalur1 = configNilai[index1]
            nilaijalur2 = configNilai[index2]

            if nilaijalur1 < nilaijalur2:
                up = {key:nilaijalur1}
                terkecil.update(up)
                h+=1
            elif nilaijalur2 < nilaijalur1:
                up = {key:nilaijalur2}
                terkecil.update(up)
                h+=1
            try:    
                if  h <= 0:
                    up = {key:nilaijalur2}
                    terkecil.update(up)
            except KeyError:
                pass
    return terkecil