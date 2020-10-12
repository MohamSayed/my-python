import csv_manager
if __name__ == "__main__":
	cm = csv_manager.CsvManager("SP500.csv")
	print(cm.read()[0])
