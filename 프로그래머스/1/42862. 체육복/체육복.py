def solution(n, lost, reserve):
    st = [1] * (n + 2)
    for i in lost:
        st[i] -= 1
    for i in reserve:
        st[i] += 1
    for i in range(1, n + 1):
        if st[i] == 2 and st[i - 1] == 0:
            st[i - 1 : i + 1] = [1, 1]
        elif st[i] == 2 and st[i + 1] == 0:
            st[i : i + 2] = [1, 1]
            
    return len([i for i in st[1 : -1] if i > 0])