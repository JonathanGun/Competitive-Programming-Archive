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
