t = int(input())

for x in range(1, t + 1):
    n = input()
    min_value = int(n)
    max_value = int(n)
    n_list = list(n)
    
    for i in range(len(n_list)):
        for j in range(i + 1, len(n_list)):
            n_list[i], n_list[j] = n_list[j], n_list[i]
            
            if n_list[0] != '0':
                new_number = int(''.join(n_list))
                min_value = min(min_value, new_number)
                max_value = max(max_value, new_number)
            
            n_list[i], n_list[j] = n_list[j], n_list[i]
    
    print(f"#{x} {min_value} {max_value}")