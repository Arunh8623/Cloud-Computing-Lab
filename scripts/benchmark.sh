#!/bin/bash
# Representative experiment helper.
# Run this inside each Ubuntu VM when actual measurements are required.

echo "===== SYSTEM INFORMATION ====="
lscpu | head -n 20
echo
free -h
echo
df -h
echo
echo "===== SYSBENCH ====="
sysbench cpu --cpu-max-prime=20000 run
