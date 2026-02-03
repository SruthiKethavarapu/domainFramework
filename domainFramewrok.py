#CRUD framework

import os

FIELDS_FILE = "fields.cfg"
MENU_FILE = "menu.cfg"
RECORDS_FILE = "records.dat"

fieldsCount = 0
fields = []
records = []
exitOption = True
MESSAGES = {
	"recordCreated": "Record created successfully!",
	"recordUpdated": "Record updated successfully!",
	"recordDeleted": "Record deleted successfully!"
}

def loadFields():
	global fieldsCount
	if os.path.exists(FIELDS_FILE):
		with open(FIELDS_FILE, "r") as fpFields:
			fields = eval(fpFields.read().strip())
			if not fields:
				return [] 
		fieldsCount = len(fields)
		return fields
	return []

def loadMenu():
	if os.path.exists(MENU_FILE):
		with open(MENU_FILE, "r") as fpMenu:
			menu = fpMenu.read()
			if not menu:
				return ""
			return menu
	return ""

def loadRecords():
	if os.path.exists(RECORDS_FILE):
		with open(RECORDS_FILE, "r") as fpRecords:
			records = fpRecords.read().strip()
			if not records:
				return []
			return eval(records)
	return []

def saveRecords(records):
	with open(RECORDS_FILE, "w") as recordsFile:
		recordsFile.write(str(records))

def findRecord(key):
	for record in records:
		if record[0] == key:
			return record
	return None

def createRecord():
	record = []
	for field in fields:
		if field.lower() == "status":
			record.append("Active")
		else:		
			record.append(input(f"Enter {field}:"))
	records.append(record)
	saveRecords(records)
	print(MESSAGES["recordCreated"])

def showAllRecords():
	for record in records:
		for i, field in enumerate(fields):
			print(f"{field}: {record[i]}")
		print("-" * 20)

def updateRecord():
	key = input("Enter key to update: ")
	record = findRecord(key)
	if record:
		record[fieldsCount - 2] = input(f"Enter new value for {fields[fieldsCount - 2]}: ")
		saveRecords(records)
		print(MESSAGES["recordUpdated"])

def deleteRecord(): 
	key = input("Enter key to delete: ")
	record = findRecord(key)
	if record:
		record[fieldsCount - 1] = "Inactive"
		saveRecords(records)
		print(MESSAGES["recordDeleted"])
def exit():
	global exitOption
	exitOption = False

def main():
	global fieldsCount, fields, records
	fields = loadFields()
	records = loadRecords()
	while exitOption:
		print(loadMenu())
		choice = int(input("Enter your choice: "))
		options = [createRecord, showAllRecords, updateRecord, deleteRecord, exit]
		if 1<= choice <= 5:
			options[choice - 1]()
		else:
			print("Invalid choice")

if __name__  == "__main__":
	main()