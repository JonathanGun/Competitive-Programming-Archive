#include <iostream>

using namespace std;

const int BIT_N = 200005;

struct
{
    int arr[BIT_N + 1] = {0};
    int diff[BIT_N + 1] = {0};

    void init(int n)
    {
        for (int i = 1; i <= n; ++i)
        {
            diff[i] = 0;
        }
    }

    int lowbit(int x)
    {
        return x & (-x);
    }

    void add(int x, int v, int n)
    {
        for (int i = x; i <= n; i += lowbit(i))
            diff[i] += v;
    }

    int ask(int x)
    {
        int ans = 0;
        for (int i = x; i >= 1; i -= lowbit(i))
            ans += diff[i];
        return ans;
    }

    int sumdigit(int x)
    {
        int ans = 0;
        while (x > 0)
        {
            ans += x % 10;
            x /= 10;
        }
        return ans;
    }
} bit;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        int n, q;
        cin >> n >> q;
        int nums[n];

        for (int i = 0; i < n; ++i)
        {
            cin >> nums[i];
        }

        while (q--)
        {
            int op;
            cin >> op;
            if (op == 1)
            {
                int l, r;
                cin >> l >> r;
                bit.add(l, 1, n);
                bit.add(r + 1, -1, n);
            }
            else if (op == 2)
            {
                int j;
                cin >> j;
                int cnt = min(bit.ask(j), 3);
                int ans = nums[j - 1];
                for (int i = 0; i < cnt; ++i)
                {
                    ans = bit.sumdigit(ans);
                }
                cout << ans << endl;
            }
        }
    }
    return 0;
}
