n = input()
n_list = map(int, input().split())
m = input()
m_list = map(int, input().split())

t_dict = {}

for i in n_list:
    if i in t_dict:
        t_dict[i] += 1
    else:
        t_dict[i] = 1
        
for i in m_list:
    if i in t_dict:
        print(t_dict[i], end = ' ')
    else:
        print(0, end = ' ')