import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import time

# 1. Synthetic Signal Generation
def generate_signal(fs=1000, duration=2.0):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    clean = np.sin(2 * np.pi * 10 * t)                      # 10 Hz target signal
    hum = 0.5 * np.sin(2 * np.pi * 50 * t)                   # 50 Hz powerline hum
    noise = 0.3 * np.random.normal(size=len(t))             # High-frequency noise
    return t, clean, clean + hum + noise

# 2. Main Processing & Benchmarking
def main():
    fs = 1000       # Sampling rate (Hz)
    cutoff = 25     # Cutoff frequency (Hz)
    t, clean_sig, raw_sig = generate_signal(fs=fs)

    # FIR Filter (Hamming Windowed Design)
    numtaps = 101
    fir_b = signal.firwin(numtaps, cutoff, fs=fs, window='hamming')

    # IIR Filter (4th-Order Butterworth)
    iir_order = 4
    iir_b, iir_a = signal.butter(iir_order, cutoff, fs=fs, btype='low')

    # Benchmarking Execution Time
    t0 = time.perf_counter()
    fir_out = signal.lfilter(fir_b, 1.0, raw_sig)
    fir_time = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    iir_out = signal.lfilter(iir_b, iir_a, raw_sig)
    iir_time = (time.perf_counter() - t0) * 1000

    print("=== DSP Filter Performance Benchmark ===")
    print(f"FIR Filter | Order: {numtaps-1} | Exec Time: {fir_time:.4f} ms")
    print(f"IIR Filter | Order: {iir_order}   | Exec Time: {iir_time:.4f} ms")

    # Plotting Results
    plt.figure(figsize=(10, 7))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, raw_sig, color='gray', alpha=0.7, label='Corrupted Input')
    plt.plot(t, clean_sig, 'k--', label='Target Signal (10 Hz)')
    plt.title('Corrupted Input Signal (10 Hz + 50 Hz Hum + Noise)')
    plt.legend(loc='upper right')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(t, fir_out, color='blue', label=f'FIR Filter (Order {numtaps-1})')
    plt.title('FIR Filter Output: Linear Phase (Constant Group Delay)')
    plt.legend(loc='upper right')
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(t, iir_out, color='red', label=f'IIR Filter (Order {iir_order})')
    plt.title('IIR Filter Output: Low Order, Non-Linear Phase Distortion')
    plt.xlabel('Time (seconds)')
    plt.legend(loc='upper right')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('filter_comparison.png')
    plt.show()

if __name__ == '__main__':
    main()