"""
3 5
1 2 4
2 3 4 5 6
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set()
B = set()
A = set(input().split())
B = set(input().split())

print(len((A-B) | (B-A)))

