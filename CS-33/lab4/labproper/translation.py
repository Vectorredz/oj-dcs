# # Assumptions
# # MEM[PTEaddr] = PTE
PTBR = [0x100, 0x108, 0x110, 0x118, 0x128, 0x130, 0x138]
# PTE_BASE_ADDR = [hex(i) for i in range(0x100, 0x147)]
# dp = [""] * 100 
# for i, item in enumerate(range(0x100, 0x147)):
#     item = str(hex(item))
#     if i <= 1:
#         if i == 0:
#             dp[i] = item
#         else:
#             dp[i] += dp[0] + item
#     else:
#         if i % 2 != 0:
#             dp[i] = dp[i-1] + item
#         else:
#             dp[i] = item
            

# print(list(map(lambda x: x, dp)))
# # print(PTE_BASE_ADDR)
# pte_addr = {base: "" for base in pte_base_addr}
# pte_byte = [
#     [0xf8, 0xf3, 0xb4, 0xb8, 0x11, 0x12, 0x19, 0x1f],
#     [0xbc, 0xbd, 0x1e, 0x80, 0x24, 0x25, 0xb1, 0x6e],
#     [0xb2, 0x34, 0xc1, 0xf4, 0xf3, 0xbf, 0xd1, 0xe4],
#     [0xb4, 0xb3, 0x98, 0x10, 0x11, 0xbe, 0x76, 0xb7],
#     [0xef, 0xf1, 0xdf, 0x34, 0x45, 0xfe, 0x100, 0xb3],
#     [0x31, 0x34, 0x23, 0x14, 0xfe, 0x13, 0x13, 0x33],
#     [0xcc, 0x4d, 0x4b, 0x4d, 0x9f, 0xfe, 0xee, 0xab],
#     [0xef, 0x09, 0x88, 0x34, 0xff, 0x52, 0x11, 0x10],
# ]

# for idx, base in enumerate(pte_base_addr):
#     temp = []
#     for j in range(8):
#         for i in range(2):
#             temp.append(hex(pte_byte[idx][i])[2:])
#         pte_addr[base] = f"0x{temp[0] + temp[1]}"

# 2. compute VPN bits
PTE_bits = 16
PPN_bits = 15
OFFSET_BITS = 8
# VB = 1
# VA = 0x1ebc
# VPN = (VA & (31 << OFFSET_BITS)) >> OFFSET_BITS
# PTE_ADDR = PTBR[0] + (VPN * PTE_bits)
# OFFSET = VA & (2**OFFSET_BITS - 1)
# PHYS_ADDR = (MEM[PTE_ADDR].PFN  << 8) | OFFSET

# 3. Physical address
# PHYS_ADDR = 0x1ebc
# PPN = PHYS_ADDR & ((2**PPN_bits - 1 )<< OFFSET_BITS)
# 0x10A -> 0x10B
VA = 0
OFFSET = VA & (2**OFFSET_BITS - 1)
# print(hex(PPN))
