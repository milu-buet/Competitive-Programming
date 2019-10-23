
# Stability in sorting algorithms
# input: people('bb', age:10), people('alex', age:10), people('aa', age:4), people('alex',age:3)
# sort by name
# Output: people('aa', age:4), people('alex', age:10), people('alex',age:3), people('bb', age:10)
# It is stable since the relative order of 'alex''s in input-output are same.

# in-place sorting
# O(1) aux space


#online sorting



# MergeSort: Stable, not-inplace
# T(n) = 2*T(n/2) + theta(n) = theta(nlogn)
# S(n) = stack+merge = O(n)
# same time for worst, average, best = theta(nlogn)
# Perfect for Linked list
# stable
# inplace is possible if data is positive interger.  the division and modulus can be used to two number at one place.



# QuickSort: Unstable, inplace
# T(n) =  theta(n) + T(k) + T(n-k-1)  # k is the pivot
# S(n) = stack
# worst when we always pick the pivot that is largest or smallest.
# worst when data is reversely sorted and we picked the pivot at start/end: O(n^2) 
# best when we pick the median as pivot. O(nlogn)
# average: O(nlogn)
# randomised pivot selection is used in practise.
# best for sorting array.
# not suitable for linked list since it needs to access element at random index.
# typical implementation is not stable. it needs O(n) space to make it stable. because we do swapping of elements according to pivot’s position (without considering their original positions).



# Insertion Sort
# best when data is almost sorted: O(n)
# worst when data is reversely sorted: O(n^2)
# S(n) = O(1)


# Counting sort
# Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.
# It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data.
# It is often used as a sub-routine to another sorting algorithm like radix sort.
# Counting sort uses a partial hashing to count the occurrence of the data object in O(1).
# Counting sort can be extended to work for negative inputs also.
# S(n) = O(n+k)
# T(n) = O(n+k)


# radix-sort