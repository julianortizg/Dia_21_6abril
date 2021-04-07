   
import calendar  
    
# using calendar to print calendar of year  
print ("The calender of year 2020 is : ")  
print (calendar.calendar(2020, 2, 1, 6)) 
print ("The calender of May 2021 is : ")  
calendar.prmonth(2021, 5)
#calendar, nos proporciona el método "day_name", el cual es un diccionario con los nombres de los días de la semana (en ingles), podemos recorrer este diccionario con un bucle y nos quedaría algo así
for x in calendar.day_name:
  print(x)
#Igual que el método "day_name", también tenemos el método "month_name", que de igual manera es un diccionario, con todos los nombres de los meses del año
for x in calendar.month_name:
  print(x)
#El método iterweekdays () devuelve un iterador para los números de los días de la semana que se utilizarán durante una semana. El primer número del iterador será el mismo que el número devuelto por firstweekday ().
cal= calendar.Calendar(firstweekday=0)
for x in cal.iterweekdays():
	print(x)
#El método itermonthdates () devuelve un iterador para el mes (1-12) del año, Este iterador devolverá todos los días (como objetos datetime.date) del mes y todos los días antes del inicio del mes o después del final del mes que se requieren para obtener una semana completa.
for x in cal.itermonthdates(2021, 5):
	print(x)
#El método itermonthdays2 () se usa para obtener un iterador para el mes del año similar a itermonthdates (). Los días devueltos serán tuplas que constan de un número de día y un número de día de la semana.
for x in cal.itermonthdays2(20211, 5):
	print(x)
#El método itermonthdays () devuelve un iterador de un mes y un año especificados. Los días devueltos serán simplemente números de días. El método es similar a itermonthdates ()
for x in cal.itermonthdays(2021, 5):
  print(x)
#El método monthdatescalendar () se utiliza para obtener una lista de las semanas del mes del año como semanas completas. Las semanas son listas de siete objetos datetime.date
print(cal.monthdatescalendar(2021, 5))
#El método monthdays2calendar () se utiliza para obtener una lista de las semanas del mes del año como semanas completas. Las semanas son listas de siete tuplas de números de días y números de días de la semana
print(cal.monthdays2calendar(2021, 5))
#El método monthdayscalendar () se utiliza para obtener una lista de las semanas del mes del año como semanas completas. Las semanas son listas de números de siete días.
print(cal.monthdayscalendar(2021, 5))
#El método yeardatescalendar () se utiliza para obtener los datos del año especificado listos para formatear, el valor de retorno es una lista de filas de meses. Cada fila de mes contiene hasta meses de ancho, cada mes contiene entre 4 y 6 semanas y cada semana contiene entre 1 y 7 días. Los días son objetos datetime.date
print(cal.yeardatescalendar(2021, 3))
#El método yeardays2calendar () se utiliza para obtener los datos del año especificado listos para formatear. El método es similar a yeardatescalendar (), las entradas en las listas de la semana son tuplas de números de días y números de días de la semana,Los números de días fuera de este mes son cero.
print(cal.yeardays2calendar(2021, 2))
#El método yeardayscalendar () se utiliza para obtener los datos del año especificado listos para formatear. El método es similar a yeardatescalendar (), Las entradas en las listas de la semana son números de días. Los números de días fuera de este mes son cero
print(cal.yeardayscalendar(2021, 2))