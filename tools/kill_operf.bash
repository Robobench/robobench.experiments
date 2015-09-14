#!/bin/bash
killall -s SIGINT operf
while [ $(ps -ef | grep -v grep | grep operf | wc -l) -lt 1 ];
do
echo "waiting for operf to die"
sleep 1
done
echo "done"
