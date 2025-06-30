from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)
        increase = True
        while start < end:
            mid = (start + end) // 2
            if numbers[mid] > target:
                end = mid
                increase = True
            else:
                start = mid + 1
                increase = False
        print(increase, mid)
        if not increase:
            for i in range(0, mid+1):
                for j in range(i+1, mid+1):
                    if numbers[i] + numbers[j] == target:
                        return [i,j]
        else:
            for i in range(mid, len(numbers)):
                for j in range(mid+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i,j]
                
        
print(twoSum([-1,0], -1))