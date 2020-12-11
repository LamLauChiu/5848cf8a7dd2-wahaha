#!/bin/bash

#Find​ the top-10​ (host)​ hosts​ makes​ most​ requests​ from​ 2019-06-10​ 00:00:00​ to 2019-06-19​ 23:59:59,​ inclusively
startdate="["`date -d"2019-06-10 00:00:00" '+%d/%b/%Y:%H:%M:%S'`
enddate="["`date -d"2019-06-19 23:59:59" '+%d/%b/%Y:%H:%M:%S'`
#awk -v sd="$startdate" -v ed="$enddate" '$4>='sd' && $4<'ed''
cat ./access.log |awk -v sd="$startdate" -v ed="$enddate" '$4>='sd' && $4<'ed'' | grep HTTP |awk '{print $1}' | sort | uniq -c | sort -r | head -n10 | awk '{print $2}' >host.txt