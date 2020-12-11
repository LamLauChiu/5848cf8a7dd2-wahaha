#!/bin/bash

#Find​ out the​ country​ with​ most​ requests​ originating​ from​ (according​ ​to the source​ IP)

# While loop in script to read line of file
# Source: https://bash.cyberciti.biz/guide/While_loop

file=./top_10_hosts.txt
while IFS= read -r line
    do 
        #result= '$(curl -s 'https://ipvigilante.com/${line}')'
        #echo "result: '$result'"
        curl -s https://ipinfo.io/${line}| jq '.country'
    done < "$file"

# Example result of curl -s https://ipinfo.io/${line}:
#     {
#   "ip": "136.243.70.151",
#   "hostname": "static.151.70.243.136.clients.your-server.de",
#   "city": "Mannheim",
#   "region": "Baden-Württemberg",
#   "country": "DE",
#   "loc": "49.4891,8.4669",
#   "org": "AS24940 Hetzner Online GmbH",
#   "postal": "68159",
#   "timezone": "Europe/Berlin",
#   "readme": "https://ipinfo.io/missingauth"
# }

# Answer: 
# "KR"
# "CN"
# "CN"
# "DE"
# "DE"
# "DE"
# "DE"
# "DE"
# "DE"
# "DE"

# DE (Deutschland) -> CN (China) -> KR (Korea)