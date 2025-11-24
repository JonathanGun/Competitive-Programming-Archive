#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    bitset<100> b(s);
    cout << b.count() << endl;
    return 0;
}