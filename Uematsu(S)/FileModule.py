import csv
def Clear(fileName):
    with open(fileName, 'w') as f:

    	return

def AddRow(fileName, word):
    with open(fileName, 'a') as f:
        writer = csv.writer(f, lineterminator='\n') 
        writer.writerow(word)     # list 1d
        #writer.writerows(word) # array2d
