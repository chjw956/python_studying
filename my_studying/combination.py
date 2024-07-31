# 리스트에서 뽑을 수 있는 모든 경우의 수 (조합)
# 출처: https://velog.io/@sloools/Python-%EC%88%9C%EC%97%B4Permutation-%EC%A1%B0%ED%95%A9Combination

from pprint import pprint

nums = [1, 2, 3, 4, 5]

ans_list = []

def combination(n, ans):
    if n == len(nums):
        temp = [i for i in ans]
        ans_list.append(temp)
        return

    ans.append(nums[n])
    combination(n+1, ans)
    ans.pop()
    combination(n+1, ans)

combination(0, [])
pprint(ans_list)