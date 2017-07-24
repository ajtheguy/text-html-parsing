import string
import urllib2
import sys
from BeautifulSoup import BeautifulSoup

	
def getcontent(site):	
	g = open('outfile_file.csv','a')
	#choice between local txt file or URL html file opener
	#f = open('input_file.html','r')
	f = urllib2.urlopen('http://natweb.eng.t-mobile.com/sites/Reporting/Reports/Homer/TTWOINCHistoryReport.aspx?SiteID='+site).read()
	soup = BeautifulSoup(f)
	#alternatively can filter the td with id attribute, but using recursive from table ->row->column give more control over how many rows to get)
	t = soup("table", {'id' : 'ctl00_ReportBody_gdvHomerTTHistory' })
	
	
	for table in t:
		rows = table.findAll('tr')
		for tr in rows[1:3]:
								
			cols = tr.findAll('td')
			g.write( site+',')
			for td in cols:
				#urllib and local file library handle html in a different way, to get the content out of a tag, use different string/list methods.
				
				#for urllib. findAll returns all td as elements in a list, use strip method join elements into a new string.
				#print ''.join(td.findAll(text=True)).strip('\n')				
				g.write(''.join(td.findAll(text=True)).strip('\n')+',')
				
				#for local file. find returns string include txt caused long whitespace between words, a pythonic way to remove all whitespace, string method split() source string to a list, string method join()  them into string again				
				#print ''.join(str(td.find(text=True)).split())
				#g.write(''.join(str(td.find(text=True)).split())+',')
				
			g.write("\n")
	print "1 down"
	g.close


if len(sys.argv) != 2:  # the program name and the two arguments
  # stop the program and print an error message
  sys.exit("Must provide import file name")

	
inputfile = str(sys.argv[1])
f = open(inputfile,'r')
list = f.readlines()
f.close
i=0

for site in list:
	siteid=site.strip('\n')
	getcontent(siteid)
	i=i+1
	if i== len(list):
		print 'All done'
	
		