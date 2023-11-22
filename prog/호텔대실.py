def solution(book_time):
    n = len(book_time)
    result = []
    visi = []
    
    for i in book_time:
        arr = []
        for j in i:
            t, m = j.split(':')
            ti = int(t) * 60 + int(m)
            arr.append(ti)
        result.append(arr)
        
    result.sort()
    
    while result:
        go, out = result.pop(0)
        for i in range(len(visi)):
            if visi[i] <= go - 10:
                visi[i] = out
                break

        else:
            visi.append(out)

    return len(visi)