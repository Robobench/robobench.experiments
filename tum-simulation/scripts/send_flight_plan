#!/bin/bash
filename=$1
topicname=/tum_ardrone/com


while read line; do
    echo $line
    rostopic pub -1 $topicname std_msgs/String "c $line"    
done < $filename
