#!/bin/bash
$@
retval=$?
echo $retval
if [[ -z $retval ]]; then
   echo "RUN STATUS: failed"
else
   echo "RUN STATUS: succeeded"
fi
