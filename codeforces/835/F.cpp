#include <bits/stdc++.h>
using namespace std;

void solve()
{
    long long n, c, d;
    cin >> n >> c >> d;
    long long v[n];
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    sort(v, v + n, greater<long long>());
    int l = 0, r = d + 2;
    while (l < r)
    {
        int mid = l + (r - l + 1) / 2;
        long long tot = 0;
        for (int i = 0; i < d; i++)
        {
            if (i % mid < n)
            {
                tot += v[i % mid];
            }
        }
        if (tot >= c)
        {
            l = mid;
        }
        else
        {
            r = mid - 1;
        }
    }
    if (l > d)
        cout << "Infinity" << endl;
    else if (l == 0)
        cout << "Impossible" << endl;
    else
        cout << l - 1 << endl;

    return;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}