def computeSimple(string):
    sum = 0
    for i in string:
        sum+=ord(i)
    

    return sum

def computeByIndex(string):
    sum = 0
    # start writing here


    return sum

def main():
    string = input('> ')
    sumSimple = computeSimple(string)
    sumByIndex = computeByIndex(string)
    print('sumSimple:', sumSimple, '\nsumByIndex:', sumByIndex)

main()
