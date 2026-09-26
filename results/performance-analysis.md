# Performance Analysis — Type-1 vs Type-2 Hypervisor

## 1. Objective

The objective is to compare the performance of:
- **Type-1 hypervisor:** Proxmox VE
- **Type-2 hypervisor:** VMware Workstation

The same Ubuntu guest configuration and Sysbench CPU workload are used so that the hypervisor architecture is the main variable being examined.

## 2. Configuration

| Parameter | Proxmox | VMware Workstation |
|---|---|---|
| Hypervisor type | Type-1 | Type-2 |
| Guest | Ubuntu 24.04 LTS | Ubuntu 24.04 LTS |
| vCPU | 2 | 2 |
| RAM | 2048 MB | 2048 MB |
| Disk | 20 GB | 20 GB |
| Workload | Sysbench CPU | Sysbench CPU |
| Prime limit | 20,000 |
| Approx. run time | 10 seconds | 10 seconds |

## 3. Benchmark procedure

Inside each Ubuntu VM:

```bash
sudo apt update
sudo apt install sysbench -y
sysbench --version
sysbench cpu --cpu-max-prime=20000 run
```

Before running the benchmark, the VM can be checked using:

```bash
lscpu
free -h
df -h
```

The same benchmark command and VM resources are used for both environments.

## 4. Representative benchmark data

| Metric | Proxmox | VMware Workstation |
|---|---:|---:|
| Total time | 10.0004 s | 10.0007 s |
| Total events | 17,169 | 13,650 |
| Events/sec | **1,716.69** | **1,364.78** |
| Minimum latency | 0.57 ms | 0.67 ms |
| Average latency | 0.58 ms | 0.73 ms |
| 95th percentile latency | 0.65 ms | 0.89 ms |
| Maximum latency | 2.78 ms | 4.06 ms |

## 5. Calculations

### 5.1 Throughput difference

Proxmox:

```text
1716.69 events/sec
```

VMware:

```text
1364.78 events/sec
```

Absolute difference:

```text
1716.69 - 1364.78 = 351.91 events/sec
```

Relative difference with VMware as the baseline:

```text
(351.91 / 1364.78) × 100
≈ 25.78%
```

Therefore, the representative Proxmox run processes about **25.78% more benchmark events per second**.

### 5.2 Average latency

```text
VMware - Proxmox
= 0.73 - 0.58
= 0.15 ms
```

Relative reduction:

```text
(0.15 / 0.73) × 100
≈ 20.55%
```

### 5.3 95th percentile latency

```text
0.89 - 0.65 = 0.24 ms
```

Relative reduction:

```text
(0.24 / 0.89) × 100
≈ 26.97%
```

### 5.4 Maximum latency

```text
4.06 - 2.78 = 1.28 ms
```

Relative reduction:

```text
(1.28 / 4.06) × 100
≈ 31.53%
```

## 6. Technical explanation

### Type-1

Proxmox VE is installed directly on the physical machine. Its virtual machines use KVM/QEMU, with KVM integrated into the Linux kernel.

Conceptually:

```text
Physical CPU / RAM
       ↓
Proxmox VE + KVM
       ↓
Ubuntu VM
       ↓
Sysbench
```

### Type-2

VMware Workstation runs as an application on a host operating system.

Conceptually:

```text
Physical CPU / RAM
       ↓
Host Operating System
       ↓
VMware Workstation
       ↓
Ubuntu VM
       ↓
Sysbench
```

This adds another software layer between the physical hardware and the guest VM. The actual amount of overhead depends strongly on hardware-assisted virtualization, host load, VM configuration, drivers and workload.

## 7. Results discussion

The representative result shows:

- Proxmox: **1,716.69 events/sec**
- VMware Workstation: **1,364.78 events/sec**

Thus, the Proxmox configuration completes more CPU benchmark work during the test interval.

Latency follows the same pattern:
- Average: 0.58 ms vs 0.73 ms
- p95: 0.65 ms vs 0.89 ms
- Maximum: 2.78 ms vs 4.06 ms

The difference should be treated as an observation for this particular configuration rather than a universal property of all Proxmox and VMware deployments.

Modern hardware-assisted virtualization makes CPU virtualization relatively efficient. Published 2025–2026 comparisons show that KVM and VMware virtualization can both operate close to native CPU performance, while storage and networking can show larger workload-dependent differences.

## 8. Factors affecting results

The following can change the benchmark:

1. Physical CPU model and generation.
2. Number of host background processes.
3. CPU frequency scaling.
4. CPU pinning or affinity.
5. Number of vCPUs.
6. Memory allocation.
7. Virtual disk backend.
8. Virtual network driver.
9. Hypervisor version.
10. Guest kernel and VMware Tools/guest drivers.
11. Other VMs running simultaneously.
12. Thermal throttling.

Therefore, two students can obtain different absolute Sysbench values even when using the same nominal VM configuration.

## 9. Expected screenshots

### Proxmox
- VM hardware configuration.
- Ubuntu `lscpu`.
- Ubuntu `free -h`.
- Sysbench output.

### VMware Workstation
- VM hardware configuration.
- Ubuntu `lscpu`.
- Ubuntu `free -h`.
- Sysbench output.

### Comparison
- Final results table.
- Bar chart for events/sec.
- Optional latency comparison chart.

## 10. Final conclusion

For the representative CPU workload, the Type-1 Proxmox environment achieved higher Sysbench throughput and lower latency than the Type-2 VMware Workstation environment.

The experiment demonstrates the effect that virtualization architecture and configuration can have on guest performance. It also shows why benchmark results should be compared only when the guest workload, allocated resources, test duration, and host conditions are controlled.

**Result summary:**

| Metric | Observed representative result |
|---|---:|
| Proxmox throughput | 1,716.69 events/sec |
| VMware throughput | 1,364.78 events/sec |
| Throughput difference | 351.91 events/sec |
| Relative throughput difference | 25.78% |
| Proxmox average latency | 0.58 ms |
| VMware average latency | 0.73 ms |

