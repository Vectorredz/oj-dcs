#!/usr/bin/env python3
import glob, re, sys
import numpy             as np
import matplotlib.pyplot as plt
from scipy.stats         import mannwhitneyu

# =============================================================================
# EDIT THIS: pick the blocksize you tested
BLOCKSIZE = 512
# Patterns to match exactly three digits after the decimal
PAT0  = "lab8\\16k-runs-0\\transpose-0.[0-9][0-9][0-9].txt"
PATBS = f"lab8\\16k-runs-512\\transpose-{BLOCKSIZE}.[0-9][0-9][0-9].txt"
# =============================================================================

# Find and sort
FILES_0  = sorted(glob.glob(PAT0))
FILES_BS = sorted(glob.glob(PATBS))

print(f"Looking for {PAT0}: found {len(FILES_0)} files")
print(f"Looking for {PATBS}: found {len(FILES_BS)} files")

# Sanity checks
assert len(FILES_0)  == 100, f"Expected 100 files for bs=0, got {len(FILES_0)}"
assert len(FILES_BS) == 100, f"Expected 100 files for bs={BLOCKSIZE}, got {len(FILES_BS)}"

# now your parse_perf() and analysis loops…
def parse_perf(fname):
    text = open(fname).read()
    # parse accesses
    m = re.search(r'^\s*([\d,]+)\s+all_data_cache_accesses', text, re.MULTILINE)
    a = int(m.group(1).replace(',',''))
    # parse misses
    m = re.search(r'^\s*([\d,]+)\s+l2_cache_misses_from_dc_misses', text, re.MULTILINE)
    m2 = int(m.group(1).replace(',',''))
    # parse time
    m = re.search(r'([\d]+\.\d+)\s+seconds time elapsed', text)
    t = float(m.group(1))
    return t, a, m2

# collect arrays
t0,a0,m0 = [],[],[]
tb,ab,mb = [],[],[]
for f0,fbs in zip(FILES_0, FILES_BS):
    x0, y0, z0 = parse_perf(f0)
    xb, yb, zb = parse_perf(fbs)
    t0.append(x0);  a0.append(y0);  m0.append(z0)
    tb.append(xb);  ab.append(yb);  mb.append(zb)

t0  = np.array(t0)
tb  = np.array(tb)
mr0 = np.array(m0)/np.array(a0)
mrb = np.array(mb)/np.array(ab)

# Item 6a

print(f"AVERAGE RUNTIME across transpose-0: {t0.mean()} seconds")
print(f"AVERAGE RUNTIME across transpose-{BLOCKSIZE}: {tb.mean()} seconds")
plt.figure()
plt.boxplot([t0, tb], tick_labels=[ "blocksize=0", f"blocksize={BLOCKSIZE}" ])
plt.xlabel("Blocksize versions")
plt.ylabel("Runtime (in sec)")
plt.title("16k_Transpose Runtime")
plt.savefig("6a.png", dpi=150)

# 6b
print(f"AVERAGE CACHE MISS RATE across transpose-0: {mr0.mean()} seconds")
print(f"AVERAGE CACHE MISS RATE across transpose-{BLOCKSIZE}: {mrb.mean()} seconds")
plt.figure()
plt.boxplot([mr0, mrb], tick_labels=[ "transpose-0", "transpose-255" ])
plt.xlabel("Blocksize versions")
plt.ylabel("Cache miss rate")
plt.title("16k_Transpose Miss Rate")
plt.savefig("6b.png", dpi=150)


# 6c
speedup = t0 / tb
average_speedup = speedup.mean()

U_rt, p_rt = mannwhitneyu(t0, tb, alternative="greater")
print("Using the Mann–Whitney U test on the computed averages: ")
print("Average speedup:", average_speedup, f"U = {U_rt}, p = {p_rt}")

alpha_p = 0.05
if p_rt < alpha_p:
    print("The change is statistically significant (p < 0.05).")
else:
    print("The change is not statistically significant (p ≥ 0.05).")

print()

# 6d
improved_miss_rate = mr0 - mrb 
average_miss_rate_improvement = improved_miss_rate.mean()

U_rt, p_rt = mannwhitneyu(t0, tb, alternative="greater")
print("Using the Mann–Whitney U test on the computed averages: ")
print("Average speedup:", average_miss_rate_improvement, f"U = {U_rt}, p = {p_rt}")

alpha_p = 0.05
if p_rt < alpha_p:
    print("The change is statistically significant (p < 0.05).")
else:
    print("The change is not statistically significant (p ≥ 0.05).")