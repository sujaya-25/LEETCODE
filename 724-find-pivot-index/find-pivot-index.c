int pivotIndex(int* nums, int numsSize) {
    int n,i,j,l,r;
    n=numsSize;
    for(int i=0;i<n;i++){
        l=0;
        r=0;
    for(int j=0;j<i;j++){
        l=l+nums[j];
    }
    for(int j=i+1;j<n;j++){
        r=r+nums[j];
    }
    if(l==r){
        return i;
        return 0;
    }
    }
    return -1;
    return 0;
}