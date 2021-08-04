import os
import sys
import requests

def print_usage():
	print("Usage: pdfdiscovery [URL]                                                     ")
	print("								  		     ")
	print("Example: pdfdiscovery http://somedomain.com/documents/                        ")
	print("										     ")
	print("Date format supported: year:month:day , year:day:month, day:month:year        ")
	print("										     ")
	


def print_header():
	print("-------------------------------PDFDISCOVERY-----------------------------------")
	print("|            Tool written by LukeGix [https://github.com/LukeGix]            |")
	print("------------------------------------------------------------------------------")

def main(argv):
	print_header()

	try:
		url = argv[1]
	except:
		print_usage()
		sys.exit(0)



	days = list(range(0,32))
	months = list(range(1,13))
	
	year = input("Year: ")
	

	for day in days:
		for month in months:
			req = requests.get(url + year + '-' + '{d:02d}-'.format(d = day) + '{m:02d}-'.format(m = month) + 'upload.pdf')
			if req.status_code == 200:
				print("File " + year + '-' + '{d:02d}-'.format(d = day) + '{m:02d}'.format(m = month) + " Found!")
				with open(year + '-' + '{d:02d}-'.format(d = day) + '{m:02d}-'.format(m = month) + 'upload.pdf', 'wb+') as document:
					document.write(req.content)
				
			
			

if __name__ == '__main__':
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		print("Exiting...")
		sys.exit(0)
