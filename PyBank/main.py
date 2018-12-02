import os
import csv
#import pdb; pdb.set_trace()

def openFile(filename):	
	csvpath = os.path.join(filename)	
	minValue = 0
	maxValue = 0

	with open(csvpath, 'r') as csvFile:
		csvReader = csv.reader(csvFile, delimiter = ',')

		csvHeader = next(csvReader)

		cont = 0
		valueInt = 0
		total = 0
		difTotal = 0
		months = list()
		difBtwMonths = list()
		oldMonthValue = 0
		maxMonth = ""
		minMonth = ""

		for row in csvReader:
			valueInt = int(row[1])
			#Variables initialization, only the first time in the loop
			if cont == 0:
				minValue = valueInt
				maxValue = valueInt
				maxMonth = row[0]
				minMonth = row[0]
				#oldMonthValue = valueInt
			#Find min and max values, commented since it is not used
			#else:
			#	if valueInt < minValue:
			#		minValue = valueInt
			#		minMonth = row[0]
			#	if valueInt > maxValue:
			#		maxValue = valueInt
			#		maxMonth = row[0]
			if cont > 0:
				difBtwMonths.append(valueInt - oldMonthValue)
			
			oldMonthValue = valueInt
		
			total += valueInt
			cont  += 1

			months.append(row[0])

		indexMax = 0
		indexMin = 0
		cont = 0
		for month in difBtwMonths:
			#Variables initialization, only the first time in the loop
			if cont == 0:
				minValue = valueInt
				maxValue = valueInt	
			#Find min and max values on the difference between months			
			else:
				if month < minValue:
					minValue = month
					indexMin = cont
				if month > maxValue:
					maxValue = month
					indexMax = cont
			difTotal += month
			cont += 1

		difTotal = difTotal / cont
		#print(f'Indice Min: {indexMin}')
		#print(f'Indice Max: {indexMax}')
		print(f'Financial Analysis')
		print(f'----------------------------')	
		print(f'Total Months: {len(months)}')
		print(f'Total: ${total}')
		print(f'Average Change: ${difTotal}')
		print(f'Greatest Increase in Profits: {months[indexMax + 1]} (${maxValue})')	
		print(f'Greatest Decrease in Profits: {months[indexMin + 1]} (${minValue})')		
		#print(f'Max Month: {maxMonth}')	
		#print(f'Min Month: {minMonth}')
	
		#print(f'{difBtwMonths}')
		#print(f'Min: {minValue}')
		#print(f'Max: {maxValue}')
		f = open("Financial_Analysis.txt", "wt")
		f.write(f'Financial Analysis\n')
		f.write(f'----------------------------\n')	
		f.write(f'Total Months: {len(months)}\n')
		f.write(f'Total: ${total}\n')
		f.write(f'Average Change: ${difTotal}\n')
		f.write(f'Greatest Increase in Profits: {months[indexMax + 1]} (${maxValue})\n')	
		f.write(f'Greatest Decrease in Profits: {months[indexMin + 1]} (${minValue})\n')	
		f.close()	

file = "budget_data.csv"
openFile(file)