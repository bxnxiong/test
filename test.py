with open('test.txt') as f:
    for lines in f:
        w = lines.split('\t')
        print w[0]
        # print w[1]
        print
