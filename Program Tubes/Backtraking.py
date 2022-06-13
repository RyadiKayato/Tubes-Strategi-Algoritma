import DapatkanJalur as co

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

#fungsi algoritma backtracking

for key in inputJalur:
    data = co.main(inputJalur[key])
    jalur.update({key : data})

pilihan = 10000
u = 0
for key in jalur:
    for i in range(len(jalur[key])):
        total = 0
        for j in range(len(jalur[key][i])):
            try:
                index1 = jalur[key][i][j]
                index2 = jalur[key][i][j+1]
                index = index1 + index2
                nilai = configNilai[index]
                total = total + nilai[0]
            except IndexError:
                pass
            if total > pilihan :
                total = pilihan
                break  
        if total < pilihan :
            pilihan2 = key
            pilihan1 = jalur[key][i]
            pilihan = total

print("Rute yang terpilih adalah => ",pilihan1)
print("Dengan panjang Rute",pilihan,"KM")