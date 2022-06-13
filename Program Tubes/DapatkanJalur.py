graf = {"a" : ["b","e","f"],
        "b" : ["a","c","d","f"],
        "c" :["b","d","g"],
        "d" :["b","c","g"],
        "e" :["a","f","g"],
        "f" :["a","b","e","g"],
        "g" :["c","d","e","f"]
        }

def cari_jalan(graf, awal, akhir, jalur=[]):
    jalur = jalur +[awal]
    if awal == akhir:
        return[jalur]
    if not awal in graf:
        return[]
    semua_jalur = []
    for titik in graf[awal]:
        if titik not in jalur:
            jalur_jalur = cari_jalan(graf, titik, akhir, jalur)
            for jalur_baru in jalur_jalur:
                if len(jalur_baru) == 7: 
                    semua_jalur.append(jalur_baru)
    return semua_jalur

def main(inputJalur):
    start = inputJalur[0]
    Finish = inputJalur[1]

    data_x = cari_jalan(graf, start, Finish)

    min = data_x[0]
    max = data_x[1]
    for x in data_x:
        if len(x) < len(min):
            min = x
        if len(x) > len(max):
            max = x

    data = []
    for x in range(0, len(data_x)): 
        data = data_x   
    return data