#include <iostream>
using namespace std;
int main() {
	int num[1001];
	int a;
	int swap=0;
	cin >> a;
	for (int i = 0; i < a; i++)
	{
		cin >> num[i];
	}
	for (int i = 0; i < a - 1; i++)
	{
		for (int j = i + 1; j < a; j++)
		{
			if (num[i] > num[j])
			{
				swap = num[i];
				num[i] = num[j];
				num[j] = swap;
			}
		}
	}
	for (int i = 0; i < a; i++)
	{
		cout << num[i]<<endl;
	}
	return 0;
}
