#include <stdio.h>
void rotate(int* nums, int numsSize, int k) {
    if(numsSize==0) return;
    k=k%numsSize;
    int *temp=malloc(numsSize*sizeof(int));
    for(int i=0;i<numsSize;i++){
        int newp=(i+k)%numsSize;
        temp[newp]=nums[i];
    }
    for(int i=0;i<numsSize;i++){
        nums[i]=temp[i];
    }
    free(temp);
}