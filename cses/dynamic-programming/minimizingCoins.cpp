#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;

int main() {
    int n, x; cin >> n >> x;
    int coins[n];
    for(int i = 0; i < n; ++i) {
        cin >> coins[i];
    }
    int dp[x + 5];
    dp[0] = 0;
    for(int i = 1; i <= x; ++i) {
        dp[i] = INT_MAX;
        for(int j = 0; j < n; ++j) {
            if(i - coins[j] >= 0 && dp[i-coins[j]] != INT_MAX) {
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }
    cout << (dp[x] == INT_MAX ? -1 : dp[x]) << endl;
}
