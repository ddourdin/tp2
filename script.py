#!/usr/bin/env python

import sys

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)

print(factorielle(int(sys.argv[1])))

