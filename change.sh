#!/bin/bash

jam=`awk 'FNR == 9' $1 `
echo $jam
sed -i "s/`awk 'FNR==9' $1`/env.hosts=['3.238.118.13','3.236.13.154']/" $1
