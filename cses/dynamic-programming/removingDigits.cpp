#include <bits/stdc++.h>
#define MOD 1'000'000'007
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> dp(n + 5);
    for(int i = 0; i < n + 5; ++i) dp[i] = INT_MAX;
    dp[0] = 0;
    for(int i = 1; i < 10; ++i) dp[i] = 1;
    for(int i = 10; i <= n; ++i) {
        int x = i;
        while (x > 0) {
            if (x % 10) {
                dp[i] = min(dp[i], dp[i - x % 10] + 1);
            }
            x /= 10;
        }
    }
    cout << dp[n] << endl;
}
