def getDatalist(datas):
    datalist = []

    i = 0

    for temp1 in datas.strip(' ').split('\n') :

        if '' != temp1 and temp1 is not None :
            datalist.append([])

            for temp2 in temp1.split(' '):
                if '' != temp2 and temp2 is not None and 'Average:' != temp2 :
                    datalist[i].append(temp2)
        i = i + 1

    return datalist