#include <iostream>
using namespace std;

int ans[9];
int visited[9];
int N, M;

void recursion(int x)
{
	if (x == M + 1)
	{
		for (int i = 1; i <= M; i++)
		{
			cout << ans[i] << " ";
		}
		cout << "\n"; 
	}
	else
	{
		for (int i = 1; i <= N; i++)
		{
			if (visited[i] == 0)
			{
				visited[i] = 1;
				ans[x] = i;
				recursion(x + 1);
				visited[i] = 0;
			}
		}
	}
}

int main()
{
	cin >> N >> M;
	recursion(1);
}
