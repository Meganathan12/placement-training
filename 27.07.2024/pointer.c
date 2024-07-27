
#include<stdio.h>
#include<stdlib.h>
 
int main()
{
    char a ='A', b ='B';
    const char *ptr = &a;
    
    printf( "value pointed to by ptr: %c\n", *ptr);
    ptr = &b;
    printf( "value pointed to by ptr: %c\n", *ptr);
}
