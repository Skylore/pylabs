#!/bin/python3

import math
import os
import random
import re
import sys

def bubble(arr):
    data = arr
    while True:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                a = data[i]
                data[i] = data[i + 1]
                data[i + 1] = a
                swapped = True;
        if not swapped: break
    return data

class Node:
  def __init__(self, val):
    self.value = val[0]
    self.width = 1
    ln = len(val)
    self.depth = ln
    if ln > 1: self.root = [Node(val[1:])]
    else: self.root = []
        
  def put(self, val):
    ln = len(val)
    if ln == 1: return 0
    dw = self.depth
    if ln > dw: self.depth = ln
    for i in self.root:
      if val[1] == i.value:
        dw = i.put(val[1:])
        self.width += dw
        return dw
    self.root.append(Node(val[1:]))
    if dw == 1: dw = 0
    else: dw = 1
    self.width += dw
    return dw

  def layout(self):
    sr = self.width - 1
    dd = (self.depth << 1) - 1
    lines = [''] * dd
    lines[0] = ' ' * sr + self.value + ' ' * sr
    if dd == 1: return lines
    srl = len(self.root)
    if srl == 1:
      lines[1] = ' ' * sr + '\u2502' + ' ' * sr
    else:
      sw = self.root[0].width - 1
      line = ' ' * sw + '\u250C' + '\u2500' * sw + '\u2500'
      for i in range(1, srl - 1):
        sw = self.root[i].width - 1
        line += '\u2500' * sw + '\u252C' + '\u2500' * sw + '\u2500'
      sw = self.root[-1].width - 1
      line += '\u2500' * sw + '\u2510' + ' ' * sw
      if line[sr] == '\u2500':
        lin = line[0:sr] + '\u2534' + line[sr + 1:]
      else:
        lin = line[0:sr] + '\u253C' + line[sr + 1:]
      lines[1] = lin
    for i in range(srl):
      a = self.root[i].layout()
      sw = self.root[i].width << 1
      for j in range(2, dd):
        try: lines[j] += a[j - 2] + ' '
        except: lines[j] += ' ' * sw
    for j in range(2, dd):
      lines[j] = lines[j][:-1]
    return lines

class Trie:

  def __init__(self):
    self.root = None
       
  def put(self, val):
    if val == '': return
    try: self.root.put('*' + val)
    except: self.root = Node('*' + val)

  def printout(self):
    a = self.root.layout()
    b = len(a)
    for i in range(b):
      print(a[i])
    return

if __name__ == '__main__':
  tree = Trie()
  wn = int(input())
  a = [None] * wn
  for i in range(wn):
   a[i] = input().strip()
  a = bubble(a)
  for i in range(wn):
    tree.put(a[i])
  tree.printout()
