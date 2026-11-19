#include <string.h>

char* longestCommonPrefix(char** strs,int strsSize){
    int len=strlen(strs[0]);

    for(int i=1;i<strsSize;i++){
        while(strncmp(strs[0],strs[i],len)!=0){
            len--;
        }
    }

    strs[0][len]='\0';
    return strs[0];
}