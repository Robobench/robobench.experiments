#!/bin/bash

$toolkit_dir/bin/operf --pid `pidof -x fsmt` --separate-thread --lazy-conversion --callgraph --session-dir /tmp/
echo 'done'

