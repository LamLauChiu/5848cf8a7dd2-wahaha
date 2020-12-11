#!/bin/bash

#Count​ the total​ number​ ​of HTTP​ requests​ recorded​ by​ this​ access​ logfile
grep HTTP/ ./access.log | wc -l
