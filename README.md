SmallRaceConditionTool
======================

Example: 

python srct.py --coint 100 --url 'http://google.com/vuln?money=31337' --method POST --post-data 'login=admin&pass=qwerty' --cookie 'auth=1&user=root' --header 'X-Forwarded-for: localhost' 'Referer: google.com'
