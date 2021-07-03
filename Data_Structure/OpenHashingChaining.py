hash_table = [0 for i in range(8)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data,value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    #해당하는 주소에 값이 있을 때
    if hash_table[hash_address] != 0:
        # 값이 있다면 체이닝 기법에 의해 리스트로 되어 있으므로 전체탐색
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key,value])
    else:
        hash_table[hash_address] = [[index_key,value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address]!=0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None
print (hash('Dave') % 8)
print (hash('Dd') % 8)
print (hash('Data') % 8)
save_data('Dave', '1201023010')
save_data('Dd', '3301023010')
print(read_data('Dave'))
print(hash_table)