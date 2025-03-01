#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    bool exist[200'005] = {false};
    for(int i = 0; i < n; ++i) {
        int x; cin >> x;
        exist[x] = true;
    }
    for(int i = 1; i <= n; ++i) {
        if(!exist[i]) {
            cout << i << endl;
            break;
        }
    }
}