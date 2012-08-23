#!/usr/bin/env python3
"""extractinv.py - try to get contents of INVN.DAT (inventory) from a
really old version of QuickBooks Point of Sale
note: this won't be useful for most users, so feel free to disregard it
(i.e., it's just a quick and hackish script)"""

import re

invn_file = open('QBPOS/RPRO/INVN.DAT', 'rb')
invn_contents = invn_file.read()
invn_file.close()

# the file may be upwards of 75% '\x00' at the end
invn_contents = re.sub(b'\x00+$', b'', invn_contents)

# this approach probably not ideal since not all entries have all fields;
# better to just extract each entry and then figure out what to do with it
# groups, respectively:
#                 DEPT       VENDOR       DESC1
#item_format = b'\t(\w+) *\x03(\w+)\x00{3}.(.+?)\x00+'
#items = re.findall(item_format, invn_contents)
