#include<iostream>
#include<algorithm>
using namespace std;
typedef struct time {
	int s;
	int e;
}T;
bool cmp(T f, T s) {
	if (f.e == s.e)
		return f.s < s.s;
	else
		return f.e < s.e;
}
int main(void) {
	int n;
	cin >> n;

	T *num = new T[n]; 
	for (int i = 0; i < n; i++) 
		cin >> num[i].s >> num[i].e;	

	sort(num, num + n, cmp);


	int answer = 1;
	int index = 0;

	for (int i = 1; i < n; i++) {
		if (num[index].e <= num[i].s) {
			index = i;
			answer++;
		}
	}

	cout << answer;
}
