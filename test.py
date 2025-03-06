traceoutput = """traceroute to google.com (142.250.69.238), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  0.365 ms  0.290 ms  0.213 ms
 2  10.103.1.254 (10.103.1.254)  2.183 ms  2.135 ms  2.086 ms
 3  * * *
 4  * * *
 5  199.96.184.2 (199.96.184.2)  3.666 ms  6.906 ms  4.216 ms
 6  199.96.191.254 (199.96.191.254)  3.187 ms  5.027 ms  4.857 ms
 7  192.43.217.170 (192.43.217.170)  4.720 ms  4.381 ms  3.516 ms
 8  72.14.194.239 (72.14.194.239)  4.869 ms  4.008 ms  3.889 ms
 9  142.251.49.27 (142.251.49.27)  5.598 ms  5.062 ms  5.392 ms
10  142.251.61.183 (142.251.61.183)  3.750 ms  3.963 ms  4.148 ms
11  den08s05-in-f14.1e100.net (142.250.69.238)  3.170 ms  3.105 ms  3.951 ms"""

line = 2
linelist = traceoutput.split('\n')
hopnum = linelist[line][:2].strip()
rawtimes = linelist[line].split(')  ')[1].split(' ')
times = [rawtimes[0], rawtimes[3], rawtimes[6]]
ip = (linelist[line].split('(')[1]).split(')')[0]
hostname = linelist[line].split('  ')[1].split(' (')[0]
if hostname == ip:
    hostname = 'None'
else:
    None
dictionary = {'hop': hopnum, 'ip': ip, 'hostname': hostname, 'rtt': times}

print(linelist)