import os
import csv
#import pdb; pdb.set_trace()

def openFile(filename):	
	csvpath = os.path.join(filename)	

	candidates = list()
	votesPerCandidate = list()

	with open(csvpath, 'r') as csvFile:
		csvReader = csv.reader(csvFile, delimiter = ',')

		csvHeader = next(csvReader)

		cont = 0
		indexVotesPerCandidate = 0
		contVotesPerCandidate = 0

		for row in csvReader:
			indexVotesPerCandidate = 0
			if not row[2] in candidates:
				candidates.append(row[2])
				votesPerCandidate.append(0)
			
			indexVotesPerCandidate = 0
			for candidate in candidates:
				if candidate == row[2]:				
					indexVotesPerCandidate = ( indexVotesPerCandidate + 1 ) - 1
					break
				indexVotesPerCandidate += 1
			    
			contVotesPerCandidate = votesPerCandidate[indexVotesPerCandidate] + 1	
			votesPerCandidate[indexVotesPerCandidate] = contVotesPerCandidate			
			cont  += 1
	
	print(f'Election Results')
	print(f'-------------------------')
	print(f'Total Votes: {cont}')
	print(f'-------------------------')
	
	f = open("Election_Results.txt", "wt")
	f.write(f'Election Results\n')
	f.write(f'-------------------------\n')
	f.write(f'Total Votes: {cont}\n')
	f.write(f'-------------------------\n')	

	indexVotesPerCandidate = 0
	winner = ""
	totalWinner = 0

	#print(f'{candidates}')
	for x in candidates:
		print(f'{x}: {(votesPerCandidate[indexVotesPerCandidate] * 100) / cont}% ({votesPerCandidate[indexVotesPerCandidate]})')
		f.write(f'{x}: {(votesPerCandidate[indexVotesPerCandidate] * 100) / cont}% ({votesPerCandidate[indexVotesPerCandidate]})\n')		
		
		if indexVotesPerCandidate == 0:
			winner = x
			totalWinner = votesPerCandidate[indexVotesPerCandidate]
		else:
			if votesPerCandidate[indexVotesPerCandidate] > totalWinner:				
				winner = x
			totalWinner = votesPerCandidate[indexVotesPerCandidate]
		#indexWiner		
		indexVotesPerCandidate += 1
	
	print(f'-------------------------')		
	print(f'Winner: {winner}')
	print(f'-------------------------')	

	f.write(f'-------------------------\n')		
	f.write(f'Winner: {winner}\n')
	f.write(f'-------------------------\n')

file = "election_data.csv"
openFile(file)