index = 0

f1 = open('data/train.csv', 'w')
f2 = open('data/test.csv', 'w')

with open('data/ratings.csv', 'r') as f:
    r = f.readline()
    f1.write(r)
    f2.write(r)
    
    while r != '':
        r = f.readline()
        # print(r)
        x = r.split(',')
        if x[0] != index:
            f2.write(r)
            index = x[0]
        else:
            f1.write(r)
        # r = r.split(',')
        # f.write("hello")

f1.close()
f2.close()