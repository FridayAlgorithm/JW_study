#include <iostream>
#include <algorithm>
using namespace std;

bool cmp1(pair<int, int>* a, pair<int, int>* b) { return a->second < b->second; }
bool cmp2(pair<int, int>* a, pair<int, int>* b) { return a->first < b->first; }
int main()
{
	int N = 0;
	int iCurrTime = 0;
	pair<int, int>* pValue[100000];
	int iResult = 0;
	cin >> N;
	for (int i = 0; i < N; ++i)
	{
		pValue[i] = new pair<int, int>;
		cin >> pValue[i]->first >> pValue[i]->second;
	}
	sort(pValue, pValue + N, cmp1);
	for (int i = 0; i < N; ++i)
	{
		if (iCurrTime <= pValue[i]->first)
		{
			int j = i + 1;
			while ((j < N) && (pValue[i]->second == pValue[j]->second))
			{
				j++;
			}
			sort(pValue + i, pValue + j, cmp2);
			iCurrTime = pValue[i]->second;
			iResult++;
		}
	}
	cout << iResult << endl;
	return 0;
}
