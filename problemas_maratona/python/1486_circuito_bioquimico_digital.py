import array as arr

def compare(input, pnc):
    i = 0
    count = 0
    while(i < int(pnc[0])):
        a = 0
        j = 0
        while(j <= len(input)):
            if(j != len(input) and int(input[j][i]) != 0):
                a+=1
            else:
                if(a>=int(pnc[2])):
                    count+=1
                a=0
            j+=1
        i+=1
    return count

while True:
    line = input()
    arr2 = line.split()
    if(len(arr2) == 3 and int(arr2[0]) == 0 and int(arr2[1]) == 0 and int(arr2[2]) == 0):
        break
    else:
        arrInputs = []
        pnc = arr2
        for n in range(int(pnc[1])):
            line = input()
            arr2 = line.split()   
            arrInputs.append(arr2)
        print(compare(arrInputs, pnc))