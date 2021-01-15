#include <iostream>
#include <string>
#include <stack>
using namespace std;
stack <int>STACK;

int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        string str="";
        cin>>str;
        if (str == "push") {   
            int x; 
            cin >> x;
            STACK.push(x);
        }
        else if (str == "pop") {
            if (S.empty())
                cout << "-1" << "\n";
            else {
                cout << S.top() << "\n";
                STACK.pop();
            }
        }
        else if(str == "size") {
            cout << STACK.size() << "\n";
        }
     
        
        else if (str == "empty") {
            cout << STACK.empty() << "\n";
        }
        
        else{
            if (STACK.empty())
                cout << "-1"<<"\n";
            else 
                cout << STACK.top() << "\n";
        }
        
    }
    return 0;
}
