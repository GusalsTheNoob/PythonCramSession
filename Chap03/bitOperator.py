bit1 = 0x61 # 01100001
bit2 = 0x62 # 01100010

print(hex(bit1 & bit2)) # 01100000 == 0x60
print(hex(bit1 | bit2)) # 01100011 == 0x63
print(hex(bit1 ^ bit2)) # 00000011 == 0x3
print(hex(bit1 >> 1))   # 00110000 == 0x30
print(hex(bit2 << 2))   #110001000 == 0x188