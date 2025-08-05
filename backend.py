import csv
import mysql.connector

def get_food_id(food_name):
	#e.g. 171372,Zwieback    783961,Zabaglione   789191,Yokan
	with open('food-list.csv', mode='r') as csv_file:
		csv_reader=csv.DictReader(csv_file)
		for row in csv_reader:
			if row['name']==food_name:
				return row['ID']
	return -1

def get_food_list(substr):
	food_list=list()
	f=0
	with open('food-list.csv', mode='r') as csv_file:
		csv_reader=csv.DictReader(csv_file)
		for row in csv_reader:
			if substr in row['name'].lower():
				f=1
				food_list.append(row['name'])
	if f==1:
		return food_list
	return -1

def get_food_data(food_id):
	#connecting to sql server and selecting the food database
	databaseConnection=mysql.connector.connect(
	host='localhost',
	user="root",
	password="root",
	database='food_database'
	)

	cursorObj=databaseConnection.cursor()
	cursorObj.execute("select * from food_data where ID="+str(food_id))
	for tableRecord in cursorObj:
		return tableRecord
def update_user_data(date, calories):
	with open('user-data.csv', mode='a', newline='') as csv_file:
		csv_writer=csv.writer(csv_file)
		csv_writer.writerow([date,calories])
def get_user_data():
	dic={}
	with open('user-data.csv', mode='r') as csv_file:
		csv_reader=csv.DictReader(csv_file)
		for row in csv_reader:
			if row['date'] in dic.keys():
				dic[row['date']]=dic[row['date']]+float(row['calories'])
			else:
				dic[row['date']]=float(row['calories'])
	return dic
#print(get_food_data(169823))
#print(get_food_id('Agutuk Fish With Shortening (Alaskan Ice Cream) (Alaska Native)'))
#print(get_user_data())