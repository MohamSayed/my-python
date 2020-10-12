import csv


class CsvManager(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        file = open(self.file_path , 'r', newline='')
        csv_data = []
        columns = [[], []]
        reader = csv.reader(file, delimiter=',')
        c = 0
        for line in reader:
            csv_data.append(line)
            for column in line:
                columns[c].append(column)
                c += 1
            c = 0
        return columns

    def write(self):
        pass

if __name__ == "__main__":
	cm = CsvManager("SP500.csv")
	print(cm.read()[0])
