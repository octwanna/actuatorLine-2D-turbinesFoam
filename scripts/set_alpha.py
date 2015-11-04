#!/usr/bin/env python

import sys

alpha_deg = sys.argv[1]

with open("system/fvOptions", "w") as f:
    with open("system/fvOptions.template") as template:
        txt = template.read()
    f.write(txt.format(alpha_deg=alpha_deg))
