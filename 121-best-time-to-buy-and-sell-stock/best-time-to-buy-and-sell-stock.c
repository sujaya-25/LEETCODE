int maxProfit(int prices[],int n){
    int min=prices[0];
    int prof=0;
    for(int i=1;i<n;i++){
        if(prices[i]<min){
            min=prices[i];
        }
        else if(prices[i]-min>prof){
            prof=prices[i]-min;
        }
    }
    return prof;
}