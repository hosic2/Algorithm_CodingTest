class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]  # 양 끝에 0 추가 (경계 처리)
        count = 0
        
        for i in range(1, len(flowerbed) - 1):  
            if flowerbed[i-1:i+2] == [0, 0, 0]:  # 세 칸이 모두 0이면 꽃 심기 가능
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        
        return count >= n