#!/usr/bin/env python
"""extractinv.py - try to get contents of INVN.DAT (inventory) from a
really old version of QuickBooks Point of Sale
note: this won't be useful for most users, so feel free to disregard it
(i.e., it's just a quick and hackish script)"""

import re

invn_file = open('QBPOS/RPRO/INVN.DAT', 'rb')
invn_contents = invn_file.read()
invn_file.close()

# the file may be upwards of 75% '\x00' at the end
# so remove the garbage
invn_contents = re.sub(b'\x00+$', b'', invn_contents)

# find first entry (index of first occurrence of \t (\x09), usually)
start = invn_contents.find(b'\x09') + 1
invn_contents = invn_contents[start:]
entry_size = 224        # seems to be constant throughout the file
entry_count = len(invn_contents) / entry_size
entries = []
# last entry may be slightly shorter due to removal of padding
for i in range(entry_count+1):
    entries.append(invn_contents[i*entry_size:(i+1)*entry_size])

# known indices for entry components:
# 0:    Department
# 10:   Vendor
# 17:   Description 1
# 48:   Description 2
# 79:   Attribute
# if a field is present, it's usually preceded by a non-\x00 byte
# if not, it's completely replaced by \x00's
