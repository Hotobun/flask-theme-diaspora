---
title: 常用排序算法
date: 2020-1-25 23:01:17
tags: 
- python
- c
- 算法
categories:
cover: /img/sort.jpg
---



| 排序方法 | 平均时间复杂度 | 最坏时间复杂度 | 最优时间复杂度 | 空间复杂度 | 稳定性 |
| :------- | :------------- | :------------- | :------------- | :--------- | :----- |
| 冒泡排序 | O(n²)          | O(n*n)         | O(n)           | O(1)       | 稳如狗 |
| 插入排序 | O(n²)          | O(n²)          | O(n)           | O(1)       | 稳如狗 |
| 选择排序 | O(n²)          | O(n²)          | O(n²)          | O(1)       | 不稳定 |
| 快速排序 | O(nlog2n)      | O(n²)          | O(nlog2n)      | O(nlog2n)  | 不稳定 |


***
<details>
  <summary> plt_show.py </summary>

``` python
from matplotlib import animation
from matplotlib import pyplot as plt 
import random
from pandas import DataFrame
from config import dcolor, test_data, interval

def show(sort_Iterable, title='', fig=None, filename=None, show=True):
    # data type: Iterable Dataframe({"number":array, "color":array})
    # rtype : None

    data = [] 
    if type(sort_Iterable) == list:
        data = sort_Iterable
    else:
        for item in sort_Iterable(test_data):
            data.append(item)

    if not fig:
        fig = plt.figure()   
 
    def animate(i): 
        plt.clf()
        plt.xticks([])
        plt.yticks([])
        plt.title(title) 
        rects = plt.bar(data[i].index, height = data[i]['number'] ,  color = data[i]['color'])
        return rects

    anim = animation.FuncAnimation(fig, animate, frames=len(data), interval=interval, repeat=False)
    if filename:
        anim.save(filename=filename)
    if show:
        plt.show()

if __name__ == "__main__": 
    array = list(range(1,33))
    random.shuffle(array)   
```

</details>  
  
  
*** 

#### 冒泡排序  
>冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。<br>
它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序（如从大到小、首字母从从Z到A）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。<br>这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端（升序或降序排列），就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名“冒泡排序”。
 
<details>
  <summary> c语言代码 </summary>

``` c
# include <stdio.h>
# define ARRAY_SIZE 23
/*
思路:
    遍历数组 如果一个数是大于下一个数 那么就互换这两个值
    使得最后的数永远是最大的
*/
 
void show(char* text, int * array, int size){
    int i = 0;
    printf("%s ", text);
    while ( i < size){
        printf("%2d ",array[i]);
        i++;
    }
    printf("\n");
}
 
int main(void){
    int array[ARRAY_SIZE] = {1, 19, 2, 7, 14, 15, 20, 18, 16, 3, 6, 21, 11, 23, 22, 17, 8, 5, 4, 12, 13, 10, 9};
    show("original",array, ARRAY_SIZE);
    int temp ;
    for(int i=0; i<ARRAY_SIZE; i++){
        for(int j=i+1; j < ARRAY_SIZE; j++){
            if (array[i] > array[j]){
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }      
        }
    }
    show("new_sort",array, ARRAY_SIZE);
    return 0;
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python
from config import dcolor, desc
from plt_show import show  

def bubble_sort(ordata): 
    '''gif每一帧的生成器'''
    # rtype : yield DataFrame
    data = ordata.copy(deep=True)
    i = len(data)
    while i > 1: 
        now_number = data['number'][0]
        data['color'][0] = dcolor['now']
        for j in range(1, i):
            target = data['number'][j]
            # desc 控制排序方式 默认为升序 即判断 now_number > target 否则 条件反过来
            # 如果成立 互换两个值
            if ( now_number < target if desc else now_number > target ):
                data['number'][j], data['number'][j-1] = now_number, data['number'][j]
                data['color'][j],data['color'][j-1] = data['color'][j-1],data['color'][j]
            # 如果不成立 now_number 应该等于更大的数 color互换
            else:
                now_number = data['number'][j]
                data['color'][j],data['color'][j-1] = data['color'][j-1],data['color'][j]
            # 如果本次循环已到尽头 这个数字判定为已排序 修改颜色
            if j == i-1:
                data['color'][j] = dcolor['done']
            yield data.copy(deep=True)      
        i -= 1
    # 到这一步 已经是只剩下一个数字 不需要判断 直接修改颜色
    data['color'][0] = dcolor['done']
    yield data
 
if __name__ == "__main__":  
    show(bubble_sort, title='bubble_sort', filename='gif/bubble_sort.gif')
```

</details>  
  
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_bubble_sort.gif" alt=""> 
 
***

#### 插入排序
>插入排序（Insertion sort）是一种简单直观且稳定的排序算法。如果有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，但要求插入后此数据序列仍然有序，这个时候就要用到一种新的排序方法——插入排序法,插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。<br>插入排序的基本思想是：每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。

* 这里python代码为了使图片更加直观 每次循环判断直接互换了两个元素 实际上算法本身一次循环只互换一次 

<details>
  <summary> c语言代码 </summary>

``` c
# include <stdio.h>
# define ARRAY_SIZE 23
/*
思路:
    每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
*/
 
void show(char* text, int * array, int size){
    int i = 0;
    printf("%s ", text);
    while ( i < size){
        printf("%2d ",array[i]);
        i++;
    }
    printf("\n");
}
 
int main(void){
    int array[ARRAY_SIZE] = {1, 19, 2, 7, 14, 15, 20, 18, 16, 3, 6, 21, 11, 23, 22, 17, 8, 5, 4, 12, 13, 10, 9};
    show("original",array, ARRAY_SIZE);
    int target; 
    for(int i=1; i<ARRAY_SIZE; i++){
        target = array[i];
        int j = i-1;
        // 当存在大于target的数 这个数往后移一位
        while (j>=0 && array[j] > target){
            array[j+1] = array[j];
            j--;
        }
        // 当while结束时 j+1 > target > j-1
        // 如果这个数 跟排序好的最后一个数相等就不用交换了
        if (j != i-1){
            array[j+1] = target;
        } 
    }
    show("new_sort",array, ARRAY_SIZE);
    return 0;
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python
from config import dcolor, desc
from plt_show import show  
 
def insertion_sort(ordata): 
    '''gif每一帧的生成器'''
    # rtype : yield DataFrame
    data = ordata.copy(deep=True)
    for i in range(len(data)):
        target = i
        temp = data['number'][target]
        data['color'][i] = dcolor['now']
        yield data.copy(deep=True)
        j = i-1 
        data['color'][i] = dcolor['done']
        while (j>=0) and (data['number'][j] > temp):
            data['number'][j+1] = data['number'][j] 
            data['number'][j] = temp
            data['color'][j] = dcolor['now']
            data['color'][j+1] = dcolor['done']
            j -= 1    
            yield data.copy(deep=True)  
            data['color'][j+1] = dcolor['done']
        yield data.copy(deep=True) 
 
if __name__ == "__main__":  
    show(insertion_sort, title='insertion_sort', filename='gif/insertion_sort.gif')
```

</details>  
  
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_insertion_sort.gif" alt=""> 
 
***

#### 选择排序 

>选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理是：第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾。以此类推，直到全部待排序的数据元素的个数为零。选择排序是不稳定的排序方法。
 
<details>
  <summary> c语言代码 </summary>

``` c
# include <stdio.h>
# define ARRAY_SIZE 23
/*
思路:
    找到未排序的元素的最小值
    然后和数组中未排序的 最前面的值互换
*/
 
void show(char* text, int * array, int size){
    int i = 0;
    printf("%s ", text);
    while ( i < size){
        printf("%2d ",array[i]);
        i++;
    }
    printf("\n");
}
 
int main(void){
    int array[ARRAY_SIZE] = {1, 19, 2, 7, 14, 15, 20, 18, 16, 3, 6, 21, 11, 23, 22, 17, 8, 5, 4, 12, 13, 10, 9};
    show("original",array, ARRAY_SIZE);
    int target;
    int temp;
    for(int i=0; i<ARRAY_SIZE; i++){
        target = i;
        for(int j=i+1; j < ARRAY_SIZE; j++){
            if (array[target] > array[j]){
                target = j;
            }      
        }
        temp = array[i];
        array[i] = array[target];
        array[target] = temp;
    }
    show("new_sort",array, ARRAY_SIZE);
    return 0;
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python
from config import dcolor, desc
from plt_show import show  
 
def selection_sort(ordata): 
    '''gif每一帧的生成器'''
    # rtype : yield DataFrame
    data = ordata.copy(deep=True)
    for now_index in range(len(data)):
        target = now_index
        data['color'][now_index] = dcolor['now']
        for new_target in range(now_index+1,len(data)):
            data['color'][new_target] = dcolor['target'] 
            yield data.copy(deep=True)
            if ( data['number'][target] < data['number'][new_target] if desc\
                    else data['number'][target] > data['number'][new_target] ):
                data['color'][target] = dcolor['default']
                yield data.copy(deep=True)
                target = new_target
                data['color'][target] = dcolor['now'] 
            else:
                data['color'][new_target] = dcolor['default']
            yield data.copy(deep=True)
        data['color'][now_index] = dcolor['now']
        yield data.copy(deep=True)
        data['number'][now_index], data['number'][target] = data['number'][target],data['number'][now_index]
        data['color'][target] = dcolor['default']
        data['color'][now_index] = dcolor['done']
        yield data.copy(deep=True)
 
if __name__ == "__main__":  
    show(selection_sort, title='selection_sort', filename='gif/selection_sort.gif')
    
```

</details>  
  
<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_selection_sort.gif" alt=""> 


***
#### 快速排序
>快速排序（Quicksort）是对冒泡排序的一种改进。<br>
快速排序由C. A. R. Hoare在1960年提出。它的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

顾名思义 比较快  

<details>
  <summary> c语言代码 </summary>

``` c
# include <stdio.h>
# define SIZE 9 
 
void sort(int* array, int l, int r){
    if (l >= r){
        return;
    }
    int i, j, target;
    i = l;
    j = r; 
    target = array[l];  
    while (i < j){
        while (i<j && array[j] > target ){ 
            // 循环退出后 j是未排序范围 最右边的比target小的数的下标
            // 把这个值放到左边
            j--;
        }
        array[i] = array[j];
        while (i<j && array[i] <= target ){
            // 循环退出后 i是未排序范围 最左边的比target大的数的下标
            // 把这个值放到右边
            i++;
        } 
        array[j] = array[i];
    }
    // 走出上面循环后 下标i与j是相等的 这个位置就是target在排序后合适的位置
    // 比target小的数已经全部在左边 大的数在右边
    array[i] = target; 

    // 剩下的两组数据递归下去 同样的方法 直到找出所有合适位置
    sort(array,l,i-1);
    sort(array,i+1,r);
}
   
void show(char * text, int * array){
    int i = 0;
    printf("%s", text);
    while (i<SIZE){
        printf("%d ",array[i]);
        i++;
    }
    printf("\n");
}
 
int main(void){
    int array[SIZE] = {2,54,6,1,55,7,23,31,8};
    show("original : ", array);
    sort(array, 0,SIZE-1);
    show("new sort : ", array);
    return 0;
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python
from config import dcolor, desc
from plt_show import show  
from config import test_data, array, dcolor
from pandas import DataFrame
 
def quick_sort(ordata, l = 0, r = None): 
    # rtype : yield DataFrame
    data = ordata 
    if not r:
        r = len(data) -1
         
    if l>=r:
        colors[r] = dcolor['done']
        queue.append(DataFrame({"number":temp_list+data, 'color':temp_color+colors}))
        return
 
    i, j = l, r
    target = data[l] 
    temp_list[1] = target
    while i < j: 
        colors[j] = dcolor['target'] 
        queue.append(DataFrame({"number":temp_list+data, 'color':temp_color+colors}))
        while i<j and data[j] > target: 
            colors[j] = dcolor['default'] 
            j -= 1 
            colors[j] = dcolor['target']
            queue.append(DataFrame({"number":temp_list+data, 'color':temp_color+colors}))
        data[i] = data[j] 
        colors[i] = dcolor['target']
        queue.append(DataFrame({"number":temp_list+data, 'color':temp_color+colors})) 
        while i<j and data[i] <= target: 
            colors[i] = dcolor['default']
            i += 1 
            colors[i] = dcolor['target']
            queue.append(DataFrame({"number":temp_list+data, 'color':temp_color+colors}))
        data[j] = data[i]  
        queue.append(DataFrame({"number":temp_list+data, 'color':temp_color+colors})) 
    data[i] = target  
    colors[i] = dcolor['done'] 
    temp_list[1] = 0
    queue.append(DataFrame({"number":temp_list+data, 'color':temp_color+colors}))
    quick_sort(data  , l, i-1)
    quick_sort(data  , i+1, r)    
 
def main(): 
    data = array 
    quick_sort(data) 
    show(queue, title='quick_sort', filename='gif/quick_sort.gif')
     
if __name__ == "__main__":   
    temp_list = [0] * 3
    temp_color = [dcolor['now']] * 3 
    colors = [dcolor['default'],]* len(array)  
    queue = []
    main() 
```

</details>  
  

<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_quick_sort.gif" alt=""> 


***
#### 归并排序
>归并排序（MERGE-SORT）是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。归并排序是一种稳定的排序方法。

<details>
  <summary> c语言代码 </summary>

``` c 
# include <stdio.h>
# define SIZE  9
 
void merge(int * arr,int * temp, int L, int M, int R){ 
    int i, j, k ;
    i = L, j = M+1, k = L;
    while (i!=M+1 && j!=R+1){
        if (arr[i] > arr[j]){
            temp[k++] = arr[j++];
        }
        else{
            temp[k++] = arr[i++];
        }
    }
    while (i != M+1){
        temp[k++] = arr[i++];
    }
    while (j != R+1){
        temp[k++] = arr[j++];
    }
    for ( i=L; i<=R; i++){
        arr[i] = temp[i]; 
    } 
}
 
void mergeSort(int * arr,int * temp, int L, int R){
    if (L >= R){
        return ;
    }
    else{
        int M = (L + R) /2;
        mergeSort(arr, temp, L, M);
        mergeSort(arr, temp, M+1, R);
        merge(arr, temp, L, M, R);
    }
}
 
int main(void){
    int arr[SIZE] = {5,33,21,51,44,12,88,30,67};
    int temp[SIZE];

    mergeSort(arr, temp, 0, SIZE-1);
    for (int i=0; i<SIZE; i++){
        printf("%d ", arr[i]);
    }
}
```

</details>  
  
  
<details>
  <summary> python绘图代码 </summary>

``` python 
from config import dcolor, desc, test_data, array, dcolor
from plt_show import show   
from pandas import DataFrame
 
def merge(arr, temp, L, M, R): 
    i, j, k = L, M+1, L 
    for index in range(L,R+1):
        colors[index] = dcolor['target']
    queue.append(DataFrame({"number":[]+arr, 'color':colors}))
    while i!=M+1 and j!=R+1: 
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            j += 1
        else:
            temp[k] = arr[i]
            i += 1
        k += 1
    while i != M+1:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j != R+1:
        temp[k] = arr[j]
        j += 1
        k += 1
    i = L
    while i<=R:
        arr[i] = temp[i]
        colors[i] = dcolor['done']
        i += 1
        queue.append(DataFrame({"number":[]+arr, 'color':colors}))
 
def mergeSort(arr, temp, L, R):
    if L >= R:
        return
    else: 
        M = (L + R) // 2
        mergeSort(arr, temp, L, M) 
        mergeSort(arr, temp, M+1, R) 
        merge(arr, temp, L, M, R) 
        queue.append(DataFrame({"number":[]+arr, 'color':colors}))
 
if __name__ == "__main__": 
    queue = []
    colors = [dcolor['default']]* len(array) 
    temp = [None] * len(array)
    mergeSort(array, temp, 0, len(array)-1)
    print(array) 
    show(queue, title='merge_sort', filename='gif/merge_sort.gif')
```

</details>  
  

<img style="display: block; margin-left: auto; margin-right: auto;" src="/static/img/archive_img/sort_merge_sort.gif" alt=""> 

