import re

'''
line = '192.168.0.1 25/Oct/2012:14:46:34 "GET /api HTTP/1.1" 200 44 "http://abc.com/search" "Mozilla/5.0"'
reg = re.compile('^(?P<remote_ip>[^ ]*) (?P<date>[^ ]*) "(?P<request>[^"]*)" (?P<status>[^ ]*) (?P<size>[^ ]*) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"')
regMatch = reg.match(line)
linebits = regMatch.groupdict()
for k, v in linebits.items() :
    print(k+": "+v)
'''

'''
line = '47.92.115.203 - - [10/Jun/2019:07:20:27 +0800] "GET / HTTP/1.1" 200 5654 "-" "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D))"'
reg = re.compile('^(?P<date>[^\]]*)')
regMatch = reg.match(line)
linebits = regMatch.groupdict()
for k, v in linebits.items() :
    print(k+": "+v)
'''


line = "<html><body><h1>[hello world]</h1></body></html>"
print(re.search(re.compile("(?<=\[)[^\]]*(?=\])"), line).group(0))
print(re.search(re.compile("(?<=<h1>).+?(?=</h1>)"), line).group(0))

# line = '47.92.115.203 - - [10/Jun/2019:07:20:27 +0800] "GET / HTTP/1.1" 200 5654 "-" "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D))"'
line = '80.82.70.187 - - [10/Jun/2019:07:06:52 +0800] "GET http://www.baidu.com/cache/global/img/gs.gif HTTP/1.1" 404 461 "-" "Mozilla"'
print(re.search(re.compile("[^ ]*"), line).group(0))
print(re.search(re.compile("(?<=\[)[^\]]*(?=\])"), line).group(0))
print(re.search(re.compile("(?<=\")[^\"]*(?=\")"), line).group(0))
