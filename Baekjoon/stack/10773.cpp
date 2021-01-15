#include <stdio.h>
#include <stdlib.h>
#include <stack>
using namespace std;
int main(){
    int K,n;
    scanf("%d", &K);
 
    stack<int> stack;
    for(int i=0; i<K; i++){
        scanf("%d",&n);
        if (n)
            stack.push(n);
        else
            stack.pop();
    }
 
    int sum=0;
    while (!stack.empty()){
        sum += stack.top();
        stack.pop();
    }
    printf("%d\n",sum);
  
}
