#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        carry.next = a and b
        soma.next = (not a and b) or (a and not b)
        pass

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]  # (1)

    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()



@block
def adder2bits(x, y, soma, carry):
    c = Signal(bool(0))
    ha = halfAdder(x[0], y[0], soma[0], c)
    fa = fullAdder(x[1], y[1], c,  soma[1], carry )
    return instances()


@block
def adder(x, y, soma, carry):
    n = len(x)
    c = [Signal(bool(0)) for i in range(n + 1)]
    faList = [None for i in range(n)]
    
    for i in range(n):
        faList[i] = fullAdder(x[i], y[i], c[i], soma[i], c[i - 1])
    def comb():
        pass

    return instances()
