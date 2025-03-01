#include <bits/stdc++.h>
using namespace std;

int solve() {
    int n, k;
    cin >> n >> k;
    vector<int> ls(n);
    unordered_map<int, int> cnt;

    for (int i = 0; i < n; i++) {
        cin >> ls[i];
        cnt[ls[i]]++;
    }

    unordered_map<int, int> p;
    for (int x : ls) {
        p[x] = cnt[k - x];
    }

    if (k % 2 == 0 && p[k / 2]) {
        p[k / 2] /= 2;
    }

    int ans = 0;
    vector<pair<int, int>> sorted_pairs(p.begin(), p.end());
    sort(sorted_pairs.begin(), sorted_pairs.end());

    for (auto &[i, v] : sorted_pairs) {
        if (i < k / 2 + 1) {
            int x = p[i];
            int y = p[k - i];
            ans += min(x, y);
        } else {
            break;
        }
    }

    return ans;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int result = solve();
        cout << result << endl;
    }

    return 0;
}
