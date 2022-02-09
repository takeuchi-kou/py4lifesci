f = open("C:\Github_repo\py4lifesci\gene_expression.txt",'r')
lines = f.readlines()
sum = 0
count = 0
for line in lines:
    try:
        level = float(line)
    except ValueError:
        print("line is not a number:", line)
    print(level)
    sum += 1
    count += 1
print('average: %.4f' % (sum/float(count)))
f.close()