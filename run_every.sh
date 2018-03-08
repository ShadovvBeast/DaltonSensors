#!/bin/bash
while true
cnt = 0
do
    if ! ((cnt % 60)); then
        python yfs201.py
    fi
    python temperature.py
    python mcp3008.py
    sleep 5
    ((cnt += 5))
done