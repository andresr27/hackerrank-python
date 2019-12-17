#!/usr/bin/python3
import numpy as np

MOD = 10**8

def matrix_exp(A, b):
  if b == 1:
    return A
  res = matrix_exp(A, b // 2)
  res = (res @ res) % MOD
  if b % 2 == 1:
    res = (A @ res) % MOD
  return res

N = 5*10**18 - 1
M = 9
A = np.zeros((M, M), dtype=int)
A[0][5] = A[0][8] = 1
A[1][8] = 1
A[2][4] = A[2][5] = 1
A[3][5] = A[3][8] = 1
A[4][2] = A[4][5] = 1
A[5][5] = A[5][8] = 1
A[6][0] = A[6][2] = 1
A[7][3] = A[7][4] = 1
A[8][0] = A[8][1] = A[8][3] = A[8][6] = A[8][7] = 1

x = np.zeros((M, 1), dtype=int)
x[8][0] = 1

res = matrix_exp(A, N) @ x
print((res[5][0] + res[8][0]) % MOD)
