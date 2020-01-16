---
title: C语言结构体封装
date: 2019-12-04 23:00:51
tags: c语言
categories: 基础
cover: img/c_encapsulation.jpg
---

### main.c
``` c
# include <stdio.h>
# include "student.h"
# include <stdlib.h>
 
int main(void) {
    struct Student *cocoa = Create_newstudent("cocoa", 12, 18);
    printf("age = %d\nname = %s\n",getAge(cocoa),getName(cocoa));
    Free(cocoa);
    system("pause");
 
	return 0;
}
```
  
### student.h
``` c
# pragma once  
struct Student;  
struct Student * Create_newstudent(char *name, int age, int student_id);  
void Free(struct Student* student);  
char * getName(struct Student * student);  
int getAge(struct Student * student);  
int getId(struct Student * student);  
```
 
### student.c 
``` c
# include <malloc.h>
 
struct Student {
    char *name;
    int age;
    int student_id;
};
 
struct Student *Create_newstudent(char *name, int age, int student_id) {
    struct Student * new = (struct Student *)malloc(sizeof(struct Student));
    new->name = name;
    new->age = age;
    new->student_id = student_id;
    return new;
}
 
char * getName(struct Student * student) {
    return student->name;
}
 
int getAge(struct Student * student) {
    return student->age;
}
 
int getId(struct Student * student) {
    return student->student_id;
}
 
void Free(struct Student *student) {
    free(student);
}
```