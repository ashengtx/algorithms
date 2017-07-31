## Searching

### sequential search 顺序查找

- unordered sequential search

item is present

best case: O(1)
worst case: O(n)
average: O(n/2)

item is not present

best case: O(n)
worst case: O(n)
average: O(n)

- ordered sequential search

item is present

the same

item is not present

best case: O(1)
worst case: O(n)
average: O(n/2)

### The Binary Search 二分查找

the binary search using slice will not perform in strict logarithmic time.
使用slice的二分查找并非严格的O(log(n))复杂度

### Hashing

*hash table*  
*slot*  
*hash function*  
*perfect hash function*
 
#### Collision Resolution 冲突解决

*open addressing* 开放寻址
*linear probing* 线性探测

A disadvantage to linear probing is the tendency for clustering.
线性探测会导致相同hash值的item聚集在一起

*rehashing*
*quadratic probing*

#### Implementing the Map Abstract Data Type

- Map()
- put(key, val)
- get(key)
- del
- len()
- in

如何处理slot满了的情况？

#### Analysis of Hashing

看不懂

### search summary

sequential search O(n)
binary search O(log(n))
hashing O(1)

## Sorting

### The Bubble Sort 冒泡排序 

复杂度 O(n^2)

A bubble sort is often considered the most inefficient sorting method since it must exchange items before the final location is known.
冒泡排序被认为是最低效的，因为在最终位置确定之前就需要多次换位。

不过，如果在一次遍历中，发现没有发生exchange，就说明这个list已经是有序的，就不需要继续下去，可以提前终止。这种修改后的算法叫做short bubble。

### The Selection Sort 选择排序

复杂度 O(n^2) 
但相比冒泡排序，交换次数更少

The selection sort improves on the bubble sort by making only one exchange for every pass through the list.
和冒泡排序相比，选择排序的改进是，每次遍历，只交换一次。

### The Insertion Sort 插入排序

复杂度 O(n^2)

In general, a shift operation requires approximately a third of the processing work of an exchange since only one assignment is performed.

shift操作的时间是exchange的1/3，因此，尽管都是O(n^2)复杂度，插入排序要稍微优于选择排序。

### The Shell Sort 希尔排序
