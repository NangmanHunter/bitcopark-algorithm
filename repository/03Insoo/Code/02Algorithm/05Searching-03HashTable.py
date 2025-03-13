class HashTable:
    def __init__(self, size):
        self.size=size
        self.table=[[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size
    def insert(self, key):
        hash_index=self.hash_function(key)
        self.table[hash_index].append(key)
    def search(self, key):
        hash_index=self.hash_function(key)
        if key in self.table[hash_index]:
            return f"키 {key}는 해시테이블의 {hash_index}번 인덱스에 있습니다."
        return f"키 {key}를 찾을수없습니다."

hash_table=HashTable(10)
hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(35)
print(hash_table.search(25))
print(hash_table.search(100))
