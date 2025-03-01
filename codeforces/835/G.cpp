#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<vector<pair<int, int>>> tree;
set<int> pathA;

int n, a, b;

void dfs(int cur, int parent, int x)
{
    if (cur == b)
    {
        return;
    }
    pathA.insert(x);
    for (auto &neighbor : tree[cur])
    {
        int neigh = neighbor.first;
        int w = neighbor.second;
        if (neigh == parent)
        {
            continue;
        }
        dfs(neigh, cur, x ^ w);
    }
}

bool dfsB(int cur, int parent, int x)
{
    if (cur != b && pathA.count(x))
    {
        return true;
    }
    for (auto &neighbor : tree[cur])
    {
        int neigh = neighbor.first;
        int w = neighbor.second;
        if (neigh == parent)
        {
            continue;
        }
        if (dfsB(neigh, cur, x ^ w))
        {
            return true;
        }
    }
    return false;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        cin >> n >> a >> b;
        tree.assign(n + 1, vector<pair<int, int>>());
        for (int i = 0; i < n - 1; ++i)
        {
            int u, v, w;
            cin >> u >> v >> w;
            tree[u].emplace_back(v, w);
            tree[v].emplace_back(u, w);
        }

        pathA.clear();
        dfs(a, -1, 0);
        if (dfsB(b, -1, 0))
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}
