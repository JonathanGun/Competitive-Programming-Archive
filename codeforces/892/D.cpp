#include <bits/stdc++.h> 
using namespace std;

// range L->B, ans = B, recursively -> cannot be done, for each Q need log time.
// store in multiset, containing all B in current x

// scanline from right
// on B -> add furthest reachable B to multiset (store furthest reachable B in a separate list)
// on L -> remove from multiset
// on X -> answer query, get max(X, top multiset)

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int furthestPortal[n];
        // 1st: value: (x coord of each type)
        // 2nd: type (2: B, 1: X, 0: L) --> important: this is to sort event from B -> X -> L
        // 3rd: index
        vector<tuple<int, int, int>> events;
        for (int i = 0; i < n; i++)
        {
            int l, r, a, b;
            cin >> l >> r >> a >> b;
            furthestPortal[i] = b;
            events.emplace_back(b, 2, i);
            events.emplace_back(l, 0, i);
        }

        int q;
        cin >> q;
        int queries[q];
        for (int i = 0; i < q; i++)
        {
            int x;
            cin >> x;
            queries[i] = x;
            events.emplace_back(x, 1, i);
        }

        sort(events.begin(), events.end());
        reverse(events.begin(), events.end());
        int currentOpenPortal = -1;
        int nOpenPortal = 0;
        // scanline from right
        // on B (2) -> add furthest reachable B to multiset (store furthest reachable B in a separate list)
        // on X (1) -> answer query, get max(X, furthest B)
        // on L (0) -> remove from multiset
        for (auto [value, type, i] : events)
        {
            if (type == 2)
            {
                if (nOpenPortal > 0)
                {
                    furthestPortal[i] = currentOpenPortal;
                }
                currentOpenPortal = furthestPortal[i];
                nOpenPortal++;
            }
            else if (type == 1)
            {
                if (nOpenPortal > 0)
                {
                    queries[i] = max(queries[i], currentOpenPortal);
                }
            }
            else
            {
                nOpenPortal--;
                if (nOpenPortal == 0) currentOpenPortal = -1;
            }
        }
        for (int i = 0; i < q; i++)
        {
            cout << queries[i] << " ";
        }
        cout << endl;
    }
    return 0;
}