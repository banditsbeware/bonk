import os

def read():

  with open('bonk/directory.txt', 'r') as f: B = f.read()

  X = dict()
  for line in B.split('\n'):
    tok = line.split(',')
    X[int(tok[0])] = { 'title': tok[1], 'date': tok[2] }

  return X
    