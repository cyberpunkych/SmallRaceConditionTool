SmallRaceConditionTool
======================

+---------------------------+
| Small Race Condition Tool |
|       version: 0.1        |
|    cyber-punk@xakep.ru    |
+---------------------------+

usage: srct.py [-h] [--url URL] [--count COUNT] [--method METHOD]
               [--post-data POST_DATA] [--cookie COOKIE] [--debug]
               [--headers HEADERS [HEADERS ...]]

optional arguments:
  -h, --help                           show this help message and exit
  --url URL, -u URL                    Testing url
  --count COUNT, -c COUNT              Count of threads
  --method METHOD, -m METHOD           Method (GET or POST)
  --post-data POST_DATA, -d POST_DATA  POST-data for request
  --cookie COOKIE, -ck COOKIE          Add cookie to your request
  --debug, -dbg                        Show server responses
  --headers HEADERS [HEADERS ...]      Add your custom headers to request

Example: python srct.py --coint 100 --url 'http://google.com/vuln?money=31337' --method POST --post-data 'login=admin&pass=qwerty' --cookie 'auth=1&user=root' --header 'X-Forwarded-for: localhost' 'Referer: google.com'
