#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys
import requests


def dist(a, b):
    return (math.sqrt(
                    (((b[0] - a[0])) * (b[0] - a[0]))
                    + ((b[1] - a[1]) * (b[1] - a[1]))
                    ))

print(dist([10, 10], [10, 10]))
