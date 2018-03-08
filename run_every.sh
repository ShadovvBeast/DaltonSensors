#!/bin/bash
while true
do
 python temperature.py
 python mcp3008.py
 sleep 5
done