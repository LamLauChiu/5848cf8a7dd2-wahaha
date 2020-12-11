#!/bin/bash

#Find​ the top-10​ (host)​ hosts​ makes​ most​ requests​ from​ 2019-06-10​ 00:00:00​ to 2019-06-19​ 23:59:59,​ inclusively

# To map the date format from (yyyy-MM-dd HH:mm:ss) to log's format (dd/MM/yyyy HH:mm:ss) %d/%b/%Y:%H:%M:%S
# source: https://www.cyberciti.biz/faq/linux-unix-formatting-dates-for-display/
# (yyyy-MM-dd HH:mm:ss) to %d/%b/%Y:%H:%M:%S
date_from="["`date -d"2019-06-10 00:00:00" '+%d/%b/%Y:%H:%M:%S'`
date_to="["`date -d"2019-06-19 23:59:59" '+%d/%b/%Y:%H:%M:%S'`

# source: https://www.ruanyifeng.com/blog/2018/11/awk.html
# get all the list of hosts list by date bewteencat ./access.log |awk -v sd="$date_from=" -v ed="$date_to" '$4>='sd' && $4<'ed'' | grep HTTP | awk '{print$1}' > hosts.txt
# cat ./access.log |awk -v sd="$date_from=" -v ed="$date_to" '$4>='sd' && $4<'ed'' | grep HTTP | awk '{print$1}' > hosts.txt 

# Sort and count number of occurrence of lines
# source: https://unix.stackexchange.com/questions/170043/sort-and-count-number-of-occurrence-of-lines
# | sort | uniq -c      => Sort and count number of occurrence of lines
# cat ./access.log |awk -v sd="$date_from=" -v ed="$date_to" '$4>='sd' && $4<'ed'' | grep HTTP | awk '{print$1}' | sort | uniq -c > hosts.txt 


# Sort by number and reverse 
# source: https://www.geeksforgeeks.org/sort-command-linuxunix-examples/
#cat ./access.log |awk -v sd="$date_from=" -v ed="$date_to" '$4>='sd' && $4<'ed'' | grep HTTP | awk '{print$1}' | sort | uniq -c | sort -nr > hosts.txt

# To show first 10 lines
# source: https://www.cyberciti.biz/faq/unix-linux-show-first-10-20-lines-of-file/
# head -10 
#cat ./access.log |awk -v sd="$date_from=" -v ed="$date_to" '$4>='sd' && $4<'ed'' | grep HTTP | awk '{print$1}' | sort | uniq -c | sort -nr | head -10 > hosts.txt

###  
#    730 1.222.44.52
#    730 118.24.71.239
#    723 119.29.129.76
#    486 148.251.244.137
#    440 95.216.38.186
#    440 136.243.70.151
#    437 213.239.216.194
#    436 5.9.71.213
#    436 5.189.159.208
#    406 5.9.108.254
###

# To show hosts only
cat ./access.log |awk -v sd="$date_from=" -v ed="$date_to" '$4>='sd' && $4<'ed'' | grep HTTP | awk '{print$1}' | sort | uniq -c | sort -nr | head -10 | awk '{print$2}' > top_10_hosts.txt 

# Answer:
###  
#     1.222.44.52
#     118.24.71.239
#     119.29.129.76
#     148.251.244.137
#     95.216.38.186
#     136.243.70.151
#     213.239.216.194
#     5.9.71.213
#     5.189.159.208
#     5.9.108.254
###