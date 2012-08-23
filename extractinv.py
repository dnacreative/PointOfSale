#!/usr/bin/env python3
"""extractinv.py - try to get contents of INVN.DAT (inventory) from a
really old version of QuickBooks Point of Sale
note: this won't be useful for most users, so feel free to disregard it
(i.e., it's just a quick and hackish script)"""

import re

invn_file = open('QBPOS/RPRO/INVN.DAT', 'rb')
invn_contents = invn_file.read()
invn_file.close()

# groups, respectively:
#                 DEPT       VENDOR       DESC1
item_format = b'\t(\w+) *\x03(\w+)\x00{3}.(.+?)\x00+'
items = re.findall(item_format, invn_contents)
