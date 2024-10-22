#include<iostream>
#include<stdio.h>
using namespace std;

const int MAX =10000;

bool arr[10000] = {0,};

void d_n(int i);

int main()
{
    for(int i = 1; i<= MAX ; i++)
    {
        if(arr[i] ==true)
           continue;
        printf("%d\n",i);
        d_n(i);
    }
    return 0;
}
void d_n(int i)
{
    if(i > MAX)
        return;
    int a= i;
    while(i)
    {
        a += i%10;
        i /= 10;
    }
    arr[a] = true;
    d_n(a);
}
