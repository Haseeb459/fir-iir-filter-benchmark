# Dual Digital Filter (FIR vs. IIR) Benchmark Engine

A Python-based Digital Signal Processing (DSP) framework designed to compare **Finite Impulse Response (FIR)** and **Infinite Impulse Response (IIR)** filter architectures for noise suppression and signal restoration.

---

## Overview

In practical DSP and software-defined radio (SDR) applications, choosing between FIR and IIR filters involves balancing **phase linearity**, **computational complexity**, and **filter stability**. 

This engine simulates a real-world scenario where a low-frequency target signal ($10\text{ Hz}$) is corrupted by high-frequency noise and severe $50\text{ Hz}$ powerline hum. It then applies both filter topologies to evaluate execution speed, group delay, and filtering performance.

---

## Filtering Methodologies

### 1. FIR Filter (Hamming Windowed LPF)
* **Equation:** $y[n] = \sum_{k=0}^{N} b_k x[n-k]$
* **Key Characteristic:** Non-recursive structure with all poles at the origin ($z=0$), guaranteeing absolute stability.
* **Trade-off:** Requires a higher filter order ($N=100$) to achieve sharp cutoff transitions, but preserves **linear phase** (constant group delay across all frequencies).

### 2. IIR Filter (4th-Order Butterworth LPF)
* **Equation:** $y[n] = \sum_{k=0}^{M} b_k x[n-k] - \sum_{k=1}^{N} a_k y[n-k]$
* **Key Characteristic:** Recursive feedback structure using both poles and zeros.
* **Trade-off:** Achieves a sharp frequency response with a significantly lower filter order ($N=4$), drastically reducing CPU cycles, but introduces **non-linear phase distortion** near the cutoff frequency.

---

## Architectural Comparison

| Performance Metric | FIR Filter (Hamming) | IIR Filter (Butterworth) |
| :--- | :---: | :---: |
| **Filter Order** | $100$ | $4$ |
| **Phase Response** | Perfectly Linear | Non-Linear |
| **Group Delay** | Constant ($N/2$ samples) | Frequency Dependent |
| **Stability** | Unconditionally Stable | Conditionally Stable |
| **Computational Overhead** | Higher ($O(N)$ taps) | Lower ($O(N)$ feedback taps) |

---

## Results & Output Plots

Running the benchmark generates time-domain waveforms illustrating the trade-off between the delayed linear output of the FIR filter and the computationally efficient output of the IIR filter:

![Filter Comparison](filter_comparison.png)

---

## Repository Structure

```text
fir-iir-filter-benchmark/
├── docs/                      # Documentation and generated figures
│   └── filter_comparison.png
├── src/                       # Source code directory
│   └── filter_benchmark.py   # Main Python benchmark script
├── README.md                  # Project documentation
└── requirements.txt           # Dependency management