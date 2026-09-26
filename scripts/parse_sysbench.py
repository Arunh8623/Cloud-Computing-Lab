# Representative values used in the report.
# These are reference/constructed values, not claimed as a measurement.

proxmox_eps = 1716.69
vmware_eps = 1364.78

difference = proxmox_eps - vmware_eps
percentage = difference / vmware_eps * 100

print(f"Throughput difference: {difference:.2f} events/sec")
print(f"Relative difference: {percentage:.2f}%")
