import os,builtins

# 读取文件
def readFile(filename):

    datalist = []
    with open(filename, "rt") as handle:
        datas = [ln.strip("\n").split(" ") for ln in handle]
        # print(datas)

        i = 0

        for temp1 in datas:
            datalist.append([])
            if isinstance(temp1,list):
                for temp2 in temp1:
                    if temp2 == "" or temp2 is None or temp2 == "Average:":
                        continue
                    else:
                        datalist[i].append(temp2)
                i = i + 1
            else:
                print("It is not list!")
    handle.close()
    # print(datalist)
    return datalist

readFile('test.txt')