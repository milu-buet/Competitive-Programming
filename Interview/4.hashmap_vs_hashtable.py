

# https://stackoverflow.com/questions/40471/differences-between-hashmap-and-hashtable

# Hastable
# Hashtable is synchronized. So it it thread safe.
# Does not allow null as key or value.
# Hashtable is a legacy class.
# Hashtable is slow.
# Hashtable is internally synchronized and can't be unsynchronized.
# Hashtable is traversed by Enumerator and Iterator.
# Enumerator in Hashtable is not fail-fast.
# Hashtable inherits Dictionary class.



# Hashmap
# Manual synchronization is needed. Or there are thread safe implementations are there: ConcurrentHashMap.
# Allow one null key and any number of null values.
# New codes always use hashmap.
# is a new class introduced in JDK 1.2.
# HashMap is fast.
# HashMap is traversed by Iterator.
# Iterator in HashMap is fail-fast.





# fail-fast iterator 
# means if one thread is iterating over hashmap and other thread trying to modify hashmap structurally it will throw ConcurrentModification 
# Exception and fail immediately 

# fail-safe iterator
# in fail-safe iterator Iterations is done on copy of collection object instead of original.




