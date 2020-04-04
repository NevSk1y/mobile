import csv
import time
import matplotlib.pyplot as plt

filename = input("Введите путь до файла .csv: ")
ipaddr = input("Введите IP-адрес: ")

rows = []
fields = []
inc_time = []
inc_traf = []
out_traf = []
out_time = []
k = 0.5
Q_inc = 0
Q_out = 0
#чтение csv файла
with open(filename, 'r') as file:
	reader = csv.reader(file)
	fields = next(reader)
	for row in reader:
		rows.append(row)
#функция счета выходного трафика
def out_traffic():
	global Q_out
	for row in rows[:reader.line_num]:
		if ipaddr in row[3]:
			Q_out += int(row[12])
			out_time.append(row[0])
			out_traf.append(Q_out)
	print(Q_out, "байт выходного трафика")
	return Q_out
#функция счета входного трафика	
def inc_traffic():
	global Q_inc
	for row in rows[:reader.line_num]:
		if ipaddr in row[4]:
			Q_inc += int(row[12])
			inc_time.append(row[0])
			inc_traf.append(Q_inc)
	return Q_inc
#ведется подсчет суммы трафика в Мб
summ_traffic_Mb = (inc_traffic() + out_traffic()) / 1048576
Total = summ_traffic_Mb * k
print(Total, "руб. необходимо заплатить")

#построение графика
inc_time.sort()
inc_traf.sort()
out_traf.sort()
out_time.sort()
#это условия для универсальности программы, так как может не быть
#входного или выходного трафика
if len(out_traf) == 0: 
	print("Графики входного и общего трафика совпадают, так как выходной трафик равен 0")
	plt.plot(inc_time,inc_traf, label='Входной и общий график')
elif len(inc_traf) == 0:
	print("Графики выходного и общего трафика совпадают, так как входной трафик равен 0")
	plt.plot(out_time,out_traf, label='Выходной и общий график')
else:
	plt.plot(inc_time,[x+y for x, y in zip(inc_traf, out_traf)], label='Общий график')
	plt.plot(inc_time,inc_traf, label='Входной трафик')
	plt.plot(out_time,out_traf, label='Выходной трафик')
plt.xlabel('Время')
plt.ylabel('Байт трафика')
plt.title('Графики зависимости потребления трафика от времени\n')
plt.legend()