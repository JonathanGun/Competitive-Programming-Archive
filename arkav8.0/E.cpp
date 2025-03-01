#include <iostream>
#include <unordered_map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n, x;
    cin >> n >> x;

    vector<int> val(n);
    for (int i = 0; i < n; i++) {
        cin >> val[i];
    }

    unordered_map<int, vector<int>> tree;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    set<int> vis;
    queue<int> q;
    q.push(x);
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        vis.insert(cur);
        for (int child : tree[cur]) {
            if (vis.count(child) == 0) {
                val[child - 1] = min(val[child - 1], val[cur - 1]);
                q.push(child);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << val[i] << " ";
    }
    cout << endl;

    return 0;
}
