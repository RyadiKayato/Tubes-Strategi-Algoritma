from sys import excepthook
import kruskal as gr
import DapatkanJalur as co
jalurTerpilih = {}
jalurTerpilih = gr.kruskal()
greedy = {}

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

terpilih = {}
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

for key in inputJalur:
    data = co.main(inputJalur[key])
    jalur.update({key : data})


#pengunaan fungsi kruskal untuk mendapatkan nilai terkecil
kruskal = jalurTerpilih["ab"]
for key in jalurTerpilih:
    test_key = key
    temp = iter(jalurTerpilih)
    for key in temp:
        if key == test_key:
            res = next(temp,None)
    try:
        if kruskal > jalurTerpilih[res]:
            kruskal = jalurTerpilih[res]
    except KeyError:
        pass

for key in jalurTerpilih:
    if jalurTerpilih[key] == kruskal:
        kunci = key
        masuk = {kunci:jalur[kunci]}
        greedy.update(masuk)

#fungsi greedy
for key in greedy:
    i = 0
    rute = []
    for j in range(len(greedy[key][i])):
        for i in range(len(greedy[key])):
            try:
                index1 = greedy[key][i][j] 
                index2 = greedy[key][i][j+1]
                index = index1 + index2
                titik1 = configNilai[index]
            except IndexError:
                pass
            try:
                index1 = greedy[key][i+1][j]
                index2 = greedy[key][i+1][j+1]
                index11 = index1 + index2
                titik2 = configNilai[index11]
            except  IndexError:
                pass
            if titik1 < titik2:
                terpilihh = index1
            elif titik2 < titik1:
                terpilihh = index11
            elif titik1 == titik2:
                terpilihh = index1
                
        rute.append(terpilihh)
        masuk = {key:[rute]}
        terpilih.update(masuk)

#fungsi yang digunakan untuk menampilkan rute
nilaii={}
for key in terpilih:
    for i in range(len(terpilih[key])):
        total = 0
        for j in range(len(terpilih[key][i])):
            try:
                index1 = terpilih[key][i][j]
                index2 = terpilih[key][i][j+1]
                index = index1 + index2
                nilai = configNilai[index]
                total = total + nilai[0]
            except IndexError:
                pass
        masuk = {key:[total]}
        nilaii.update(masuk)


min_val = min(terpilih.values())
print("Dengan rute => {}" .format (min_val))
min_val = min(nilaii.values())
print("Dan panjang rute =>",min_val,"KM")