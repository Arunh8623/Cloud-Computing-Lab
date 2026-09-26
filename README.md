# Cloud Computing Experiment 01
## Performance Analysis of Type-1 and Type-2 Hypervisors

### Aim
To compare the CPU performance of a Type-1 hypervisor (Proxmox VE) and a Type-2 hypervisor (VMware Workstation running Ubuntu as a guest) using a controlled Sysbench CPU workload.

> **Important note about the data:**  
> This submission contains a **representative/constructed experimental dataset** so that the report is complete without requiring the experiment to be rerun now. The values are realistic lab-style values and are based on the same workload/configuration used in the reference material. They should be treated as sample/reference results, not as personally measured results.

### Experimental environments

| Parameter | Type-1 | Type-2 |
|---|---|---|
| Hypervisor | Proxmox VE | VMware Workstation |
| Guest OS | Ubuntu 24.04 LTS | Ubuntu 24.04 LTS |
| vCPU | 2 | 2 |
| RAM | 2 GB | 2 GB |
| Virtual disk | 20 GB | 20 GB |
| Benchmark | Sysbench CPU | Sysbench CPU |
| Prime limit | 20,000 | 20,000 |
| Test duration | ~10 s | ~10 s |

### Architecture

**Type-1: Proxmox**
Physical hardware → Proxmox VE/KVM → Ubuntu VM → Sysbench

**Type-2: VMware Workstation**
Physical hardware → Host OS → VMware Workstation → Ubuntu VM → Sysbench

### Benchmark command

```bash
sudo apt update
sudo apt install sysbench -y
sysbench --version
sysbench cpu --cpu-max-prime=20000 run
```

### What is measured

The main metric is **events per second (EPS)**.

Higher EPS means that the VM completed more benchmark operations in the same period.

Other useful metrics:
- Total execution time
- Total events
- Minimum latency
- Average latency
- 95th percentile latency
- Maximum latency

### Representative result

| Metric | Proxmox Type-1 | VMware Workstation Type-2 |
|---|---:|---:|
| Total time (s) | 10.0004 | 10.0007 |
| Total events | 17,169 | 13,650 |
| Events/sec | **1,716.69** | **1,364.78** |
| Minimum latency (ms) | 0.57 | 0.67 |
| Average latency (ms) | 0.58 | 0.73 |
| 95th percentile (ms) | 0.65 | 0.89 |
| Maximum latency (ms) | 2.78 | 4.06 |

### Derived comparison

- Throughput advantage of Proxmox over VMware: **25.78%**
- Average-latency reduction: **20.55%**
- 95th-percentile latency reduction: **26.97%**
- Maximum-latency reduction: **31.53%**

These percentages are calculated from the representative values above.

### Interpretation

The representative CPU benchmark shows higher throughput and lower latency in the Proxmox VM. A reasonable technical explanation is that Proxmox uses KVM integrated with the Linux kernel and runs directly on the physical machine, while VMware Workstation operates on top of a host operating system.

However, the benchmark should not be interpreted as proving that one hypervisor is always faster. Hypervisor version, CPU model, virtualization settings, VM drivers, host background load, CPU scheduling, and storage/network configuration can all change results. Published comparisons also show that modern virtualization overhead can be small and workload-dependent.

### Expected observations

1. Both VMs successfully execute the same Ubuntu workload.
2. Proxmox shows higher Sysbench CPU throughput in this representative run.
3. VMware Workstation shows slightly higher average and tail latency.
4. The difference is visible even though both VMs have identical allocated vCPU and RAM.
5. The result demonstrates why virtualization architecture and host configuration matter when evaluating performance.

### Conclusion

For the representative CPU workload used in this lab, the Type-1 Proxmox environment produced higher benchmark throughput and lower measured latency than the Type-2 VMware Workstation environment.

The experiment demonstrates that virtualization introduces an additional software layer and that the architecture and configuration of the virtualization platform can affect VM performance. The result is workload-specific and should not be generalized to every CPU, storage, or network workload.

### Screenshots

Add your screenshots later in:

```text
screenshots/type1-proxmox/
screenshots/type2-vmware/
screenshots/comparison/
```

Suggested screenshots:
1. Proxmox VM configuration showing 2 vCPU, 2 GB RAM and 20 GB disk.
2. Ubuntu `lscpu`, `free -h`, and `df -h`.
3. Proxmox Sysbench output.
4. VMware VM configuration.
5. VMware Ubuntu system information.
6. VMware Sysbench output.
7. Final comparison table/graph.

### Files

```text
CC-Experiment-01-Hypervisor-Analysis/
├── README.md
├── results/
│   └── performance-analysis.md
├── scripts/
│   ├── benchmark.sh
│   └── parse_sysbench.py
└── screenshots/
    ├── type1-proxmox/
    ├── type2-vmware/
    └── comparison/
```
