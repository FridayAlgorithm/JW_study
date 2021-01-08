#include <iostream>
#include <vector>
using namespace std;
 
int main(void) {
    int N, K;    
    cin >> N >> K;
    int money;  
    vector<int> value;
    for (int i = 0; i < N; i++) {   
        cin >> money;
        value.push_back(money);
    }
 
    int cnt = 0;  
    for (int i = N - 1; i >= 0; i--) {
        while (K / value[i]) {
            cnt += (K / value[i]);
            K %= value[i];
        }
    }
    cout << cnt;
    return 0;
}
