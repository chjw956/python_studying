# 강사님이 주신 heapq 뼈대 코드

# heap : 완전 이진 트리 >>> 배열에 표현가능
heap = [0] * 100  # 넉넉하게...
# 삽입할 때 : 맨 뒤에 넣기..
# 삭제할 때 : 맨 뒤에 있는애 루트로 올리기...
heap_count = 0  # 맨 뒤 요소의 위치를 알려주는 변수


# data를 tree에 삽입
def heap_push(data):
    global heap_count
    # 1. 맨 마지막에 새 요소 넣어주고
    # 2. 부모보다 크면 부모랑 자리 바꾸기
    # 3. 새 요소가 부모보다 작거나, 루트가 되기 전까지 2번 반복
    # 맨 마지막 위치에 요소 추가
    heap_count += 1
    heap[heap_count] = data

    current = heap_count
    parent = current // 2  # 배열로 표현된 이진트리에서 부모요소는 자식번호//2
    while parent > 0 and heap[current] > heap[parent]:
        heap[current], heap[parent] = heap[parent], heap[current]
        #   바꿨으니까....현재 번호는 아까 부모 번호
        current = parent
        parent = current // 2


# tree의 최대값을 삭제 및 반환
def heap_pop():
    global heap_count
    # 1. 루트 값 반환(저장해 뒀다가 나중에 반환)
    result = heap[1]
    # 2. 가장 마지막 원소를 root에 저장하기
    heap[1] = heap[heap_count]
    # 마지막 원소가 없어졌으니...heap_count 하나 줄여주기
    heap_count -= 1
    # (자식들 중 더 큰 값과 비교하기)
    parent = 1
    child = parent * 2  # 일단 왼쪽 자식
    if child + 1 <= heap_count:  # 오른쪽 자식이 있음
        if heap[child] < heap[child + 1]:  # 오른쪽이 더 크다면
            child += 1  # 비교 대상을 오른쪽 자식으로 바꿔주기

    # 3. 부모에 올라간 요소가 자식 보다 작으면 자식과 위치 바꿔주기
    # 4. 자리를 바꾸고 나면 3번 과정을 반복하기
    #    (부모가 더 크거나 혹은 자식이 없으면 멈추기)
    while child <= heap_count and heap[child] > heap[parent]:
        # 자식이 더 크다면...부모와 자리 바꿔주기
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
        child = parent * 2
        if child + 1 <= heap_count:
            if heap[child] < heap[child + 1]:
                child += 1
    return result


# 여러번 넣었을 때..제일 큰 값이 루트에 있으면 됩니다.
heap_push(1)
heap_push(5)
heap_push(4)
heap_push(7)
heap_push(6)
heap_push(8)
print(heap)
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())
print(heap_pop())