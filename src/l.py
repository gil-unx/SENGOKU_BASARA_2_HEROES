import glob
for name in sorted(glob.glob("CRC32_CHR/*.png")):
    print(name)