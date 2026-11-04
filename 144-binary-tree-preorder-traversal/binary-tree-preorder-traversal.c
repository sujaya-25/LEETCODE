void preorder(struct TreeNode *root,int *arr,int *len){
    if(root==NULL)
    return;
    arr[*len]=root->val;
    (*len)++;
    preorder(root->left,arr,len);
    preorder(root->right,arr,len);
}
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int *arr=malloc(100*sizeof(int));
    *returnSize=0;
    preorder(root,arr,returnSize);
    return arr;
}