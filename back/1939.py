import sys
input = sys.stdin.readline
# n = 섬수, m = 다리수
n, m = map(int, input().split())
for i in range(m):
    a, b, c = list(map(int, input().split()))