# 순열 생성

lst = [2, 3, 5, 7, 7, 7]

# 재귀 이용 (ver.1)
def permutation(arr, r):                        
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]             # [0, 0, 0, 0, 0, 0]
                                                    # used = [0]* len(arr)

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3. len(arr) = 6임
        for i in range(len(arr)):
            # 해당 인덱스의 값이 존재하지 않으면(?) / 값이 0이면..?
            if not used[i]:
                # 카운팅 정렬 방법이랑 유사한데..?
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)                              # used = [0, 0, 0, 0, 0, 0]

permutation(lst, 6)                      # 주어진 리스트를 바탕으로 6개의 원소를 가지는 리스트 순열 생성