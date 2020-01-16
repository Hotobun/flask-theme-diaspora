---
title: 01背包问题
date: 2019-12-04 23:40:53
tags: 
- 算法
- c语言
- python
categories: 算法
cover: /img/knapsack.jpg
---

有n个物品，它们有各自的体积和价值，现有给定容量20的背包，如何让背包里装入的物品具有最大的价值总和？  
  
编号|重量|价格  
:--:|:--:|:--:  
1|2|3  
2|3|4  
3|4|5  
4|5|8  
5|9|10  

变量B存储图表 w物品列表 v物品对应价格    
k，C遍历物品及背包容量

例如：    

![](/img/archive_img/knapsack.png)

极端条件 最后一个物品 重量等于背包容量20 而这个物品价值999    
k的循环最后一次是    
`k=5 C=1 C<W`  
`w[5] = 20`  
`w[5] > C` 
条件成立 这件物品的重量大于背包剩下容量 无法添加  
B[5][1] 直接装入前一个格子的最优价格 依次类推  
跳过一部分。。。  
到最后一个物品的最后一次遍历背包容量时  
`k=5, C=20`  
判断 `w[k] > C` 不成立  
这件物品不能装入背包 然后else考虑 偷这件物品和不偷这件物品的收益  
偷的情况:  
* `B[k-1][C-w[k]]` C-w[k]是整个背包容量 减去偷这件物品的容量 得到下标
* 代入计算的出 B[4][0] 这个位置的价值是0
* `int value1 = B[k - 1][C - w[k]] + v[k];` 加上v[k]这个物品的价格
* 得出 value1 = 0 + 999 = 0  

不偷的情况：  
* 直接放入上一个容量的最优价钱 
 
最后对比 得出这个容量的最优价钱

<details>
  <summary> c </summary>  

``` c
# include <stdio.h>
# include <stdlib.h>
# define N 6
# define W 21
 
int B[N][W] = { 0 };
int w[6] = { 0,2,3,4,5,9 };
int v[6] = { 0,3,4,5,8,10 };
 
void knapsack() {
	int k, C;
	for (k = 1; k < N; k++) {
		for (C = 1; C < W; C++) {
			if (w[k] > C) {
				B[k][C] = B[k - 1][C];
			}
			else {
				int value1 = B[k - 1][C - w[k]] + v[k];
				int value2 = B[k - 1][C];
				if (value2 > value1) {
					B[k][C] = value2;
				}
				else {
					B[k][C] = value1;
				}
			}
		}
	}
}
 
int main(void) {
	knapsack();
	printf("%d \n", B[5][20]);
	system("pause");
	return 0;
}  
```  
</details>   
  
  
<details>  
  <summary> python </summary>  
  
``` python  
def func():
    W = 21
    w = [0,2,3,4,5,9]
    v = [0,3,4,5,8,10]
    N = len(w)
    B = [[0 for i in range(W)] for i in range(N)]
    
    for k in range(N):
        for C in range(W):
            if w[k] > C:
                B[k][C] = B[k-1][C]
            else:
                value1 = B[k-1][C-w[k]] + v[k]
                value2 = B[k-1][C]
                B[k][C] = max(value1,value2)
    return B[-1][-1]
```  
  
</details>    
