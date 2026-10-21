int lengthOfLastWord(char* s) {
    int n=strlen(s);
    int c=0;
    for(int i=n-1;i>=0;i--){
        if(s[i]=='\n'){
            continue;
        }
        else if(s[i]!=' '){
            c++;
        }
        else if(c>0){
            break;
        }
    }
    return c;
}