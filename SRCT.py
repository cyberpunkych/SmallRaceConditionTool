import sys
import os
from multiprocessing import Process, freeze_support
import urllib2
import urllib
import argparse

print """
+---------------------------+
| Small Race Condition Tool |
|       version: 0.1        |
|    cyber-punk@xakep.ru    |
+---------------------------+
"""


ap = argparse.ArgumentParser(epilog="Example:  python "+sys.argv[0]+" --count 100 --url 'http://google.com/vuln?money=31337' --method POST --post-data 'login=admin&pass=qwerty' --cookie 'auth=1&user=root' --headers 'X-Forwarded-for: localhost' 'Referer: google.com'", prog='srct.py',
  formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50))
ap.add_argument('--url', '-u', nargs=1, help="Testing url")
ap.add_argument('--count', '-c', nargs=1, help="Count of threads")
ap.add_argument('--method', '-m', nargs=1, help="Method (GET or POST)")
ap.add_argument('--post-data', '-d', nargs=1, help="POST-data for request")
ap.add_argument('--cookie', '-ck', nargs=1, help="Add cookie to your request")
ap.add_argument('--debug', '-dbg', action='store_const', const=1, help="Show server responses")
ap.add_argument('--headers', nargs='+', help="Add your custom headers to request")

opts = ap.parse_args()
headers = {}
if opts.headers is not None:
	for i in xrange(len(opts.headers)):
		headers[opts.headers[i].split(' ')[0][:-1]]=opts.headers[i].split(' ')[1]
print headers

if opts.cookie is not None:
	cookie = str(opts.cookie[0])
else:
	cookie = None
thr_count=int(opts.count[0])
method=str(opts.method[0])
if method == "POST":
	post_data=str(opts.post_data[0])
else:
	post_data = ""
site = str(opts.url[0])
debug = opts.debug





def POST(url, post_data):
	if cookie is not None:
		headers['Cookie']=cookie
	req = urllib2.urlopen(urllib2.Request(url, post_data, headers))
	try: req
	except URLError as e:
		print e.reason
	if debug==1:
		print req.read()

def GET(url):
	request = urllib2.Request(url, headers=headers)
	if cookie is not None:
		request.add_header("Cookie", cookie)

	req = urllib2.urlopen(request)
	try: req
	except URLError as e:
		print e.reason
	if debug==1:
		print req.read()
		print

def fun( url ):
	if method == "GET":
		GET(site)
	elif method == "POST":
		POST(site, post_data)
	if debug!=1: print ".",

if __name__ == '__main__':
	freeze_support()
	nproc = len( sys.argv ) > 1 and thr_count or 1
	print 'Count of Threads: ', nproc 
	procs = []
	for i in range( nproc ):
		procs.append( Process( target = fun, args = ( i, ) ) )
	for i in range( nproc ):
		procs[ i ].start()
	for i in range( nproc ):
		procs[ i ].join()

print "\nDone!"
