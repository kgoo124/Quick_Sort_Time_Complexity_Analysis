import random
import time
import statistics

def quick_sort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   return alist

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

def generate_list(n): # generates a list of size n
    lst = []
    for _ in range(n):   # 
        lst.append(random.randint(0, 10000000))
    return lst

def main():
    # records samples times for merge sort and quick sort
    quick_file = "quick_times.txt"
    quick_double_file = "quick_double_times.txt"
    quick = open(quick_file,"w")
    quick_double = open(quick_double_file, "w")
    quick_sample_times = []
    quick_double_sample_times = []
    for _ in range(550):    # generates 550 samples
        for _ in range(800):   # each sample contains 800 averages
            quick_lst = generate_list(200)   # each list contains 200 items
            
            start = time.time()
            quick_sort(quick_lst)   # quick sort on list
            stop = time.time()
            elapsed_time = stop - start
            quick_sample_times.append(elapsed_time * 1000) # append the time(ms) taken to quick sort samples

            quick_lst = generate_list(400)  # each list contains 400 items
            start = time.time()
            quick_sort(quick_lst)   # quick sort on list
            stop = time.time()
            elapsed_time = stop - start
            quick_double_sample_times.append(elapsed_time * 1000) # append the time(ms) taken to quick sort samples

        quick.write(str(statistics.mean(quick_sample_times)) + '\n')
        quick_double.write(str(statistics.mean(quick_double_sample_times)) + '\n')
        quick_sample_times = []
        quick_double_sample_times = []
    quick.close()
    quick_double.close()

if __name__ == '__main__': 
    main()