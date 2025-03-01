#include <iostream>
#include <unordered_map>
#include <numeric>

using namespace std;

int main() {
    int n;
    cin >> n;

    unordered_map<int, int> cnt;
    for (int i = 0; i < n; i++) {
        int m, _;
        cin >> m >> _;
        cnt[m]++;
    }

    int num_values = cnt.size();
    int prod_values = accumulate(cnt.begin(), cnt.end(), 1,
                                 [](int a, const auto& p) { return a * p.second; });
    cout << prod_values * (num_values * (num_values - 1) / 2) << endl;

    return 0;
}
