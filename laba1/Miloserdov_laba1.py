# по заданному варианту номер: 915783624
import csv
f = input("Введите путь до файла:")
num = input("Введите номер телеофна абонента: ")

rows = []
fields = []

T_out = 0
k_out = 2
T_inc = 0
k_inc = 0
N = 0
k_sms = 1

# чтение csv-файла
with open(f, 'r') as file:
	reader = csv.reader(file)
	fields = next(reader)
	for row in reader:
		rows.append(row)
		
# функция тарификации исходящих звонков		
def out_calls():
	global T_out
	global k_out
	for row in rows[:10]:
		if num in row[1]:
			T_out += float(row[3])
	X_out = T_out*k_out
	return X_out

# функция тарификации входящих звонков
def inc_calls():
	global T_inc
	global k_inc
	for row in rows[:10]:
		if num in row[2]:
			T_inc += float(row[3])
	X_inc = T_inc*k_inc	
	return X_inc

# функция тарификации смс
def sms():
	global N
	global k_sms	
	for row in rows[:10]:
		if num in row[1]:
			N += int(row[4])
	Y = (N - 10)*k_sms
	if Y < 0:
		Y = 0
	return Y

Total = sms()+out_calls()+inc_calls()
print("Результат тарификации абонента:", Total, "руб.")