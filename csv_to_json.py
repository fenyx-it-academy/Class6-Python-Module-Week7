import csv
with open('data.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
    def toJson(self):
        jsonCon = csv.dumps(self.__dict__)
        return jsonCon