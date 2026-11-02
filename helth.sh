#!/bin/bash
echo "=====system health check====="
echo "cpu usage:"
mpstat 1 1
echo "memory usage:"
free -h
echo "disk usage:"
df -h /
echo "ssh service"
if systemctl is-active --quiet ssh
then 
   echo "shh is runing"
else
   echo "shh is not runing"
fi
echo "=====check completed======="

