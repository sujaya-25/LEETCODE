char* longestCommonPrefix(char** strs,int strsSize){
    int i=0;
    while(1){
        char ch=strs[0][i];
        if(ch=='\0'){
            return strs[0];
        }
        for(int j=1;j<strsSize;j++){
            if(strs[j][i]!=ch){
                strs[0][i]='\0';
                return strs[0];
            }
        }
        i++;
    }
}