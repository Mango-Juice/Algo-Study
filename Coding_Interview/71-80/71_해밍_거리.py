#해밍 거리
#https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y #XOR 연산
        return bin(xor).count('1') #이진수로 변환 후 1의 갯수 출력
