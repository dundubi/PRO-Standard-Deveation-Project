import csv

with open("data1.csv") as f: 
    reader = csv.reader(f)
    file_data = list(reader)
    data = file_data[0]

#finding mean
def mean(data) :
    get_len = len(data)
    total = 0
    for x in data :
        total = total+int(x)
    mean = total/get_len
    print("data(mean) :-",mean)
mean(data)

#x-mean
squared_list = []
for number in data :
    f = int(number)
    a = f - mean(data)
    a = a**2
    squared_list.append(a)

print(squared_list)


