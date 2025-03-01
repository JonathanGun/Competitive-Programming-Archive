#include <bits/stdc++.h>
using namespace std;

struct P {
    long long x, y;
    P() {}
    P(long long x, long long y): x(x), y(y) {}
    friend istream& operator>>(istream& is, P& p) {
        is >> p.x >> p.y;
        return is;
    }
    friend ostream& operator<<(ostream& os, const P& p) {
        os << p.x << " " << p.y;
        return os;
    }
    P operator+(const P& other) const {
        return P(*this) += other;
    }
    P operator-(const P& other) const {
        return P(*this) -= other;
    }
    P& operator+=(P other) {
        x += other.x;
        y += other.y;
        return *this;
    }
    P& operator-=(P other) {
        x -= other.x;
        y -= other.y;
        return *this;
    }
    long long distSq() {
        return x*x + y*y;
    }
    long long operator*(const P& other) const {
        return x * other.y - other.x * y;
    }
    long long compareAngle(const P& reference, const P& target) const {
        return (target - *this) * (reference - *this);
    }
};

bool isIntersect(P from, P to, P p1, P p2) {
    if ((to - from) * (p2 - p1) == 0) {
        if (from.compareAngle(p1, to) != 0) {
            return false;
        }
        for (int rep = 0; rep < 2; ++rep) {
            if (!(max(from.x, to.x) >= min(p1.x, p2.x) && max(from.y, to.y) >= min(p1.y, p2.y))) {
                return false;
            }
            swap(from, p1); swap(to, p2);
        }
        return true;
    }
    for (int rep = 0; rep < 2; ++rep) {
        long long p1Angle = from.compareAngle(to, p1);
        long long p2Angle = from.compareAngle(to, p2);
        if (p1Angle > 0 && p2Angle > 0) return false;
        if (p1Angle < 0 && p2Angle < 0) return false;
        swap(from, p1); swap(to, p2);
    }
    return true;
}

long long polygonArea(vector<P>& polygon) {
    long long area = 0;
    for(int i = 1; i < polygon.size() - 1; ++i) {
        area += polygon[0].compareAngle(polygon[i], polygon[i + 1]);
    }
    return area;
}

int main() {
    int n; cin >> n;
    vector<P>polygon(n);
    for(int i = 0; i < n; ++i) {
        cin >> polygon[i];
    }
    cout << abs(polygonArea(polygon)) << endl;
}
