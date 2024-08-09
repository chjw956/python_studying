# powerset: 집합 A의 모든 부분집합을 모은 집합 (멱집합)
# 반복문의 중첩 횟수를 유연하게 조절하기 위해 재귀 함수를 사용함

# 입력된 비트 배열의 특정 인덱스에 0/1을 넣어주는 작업을 수행함
def powerset(bit_arr, idx):
    if idx == N:
        print(bit_arr)
        return

    for i in range(2):
        bit_arr[idx] = i
        powerset(bit_arr, idx + 1)    
        

arr = [1, 2, 3, 4, 5]
N = len(arr)

powerset([None] * N ,0)