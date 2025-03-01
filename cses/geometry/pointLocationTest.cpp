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
    P operator+(const P& b) const {
        return P(*this) += b; 
    }
    P operator-(const P& b) const {
        return P(*this) -= b;
    }
    P& operator+=(P b) {
        x += b.x;
        y += b.y;
        return *this;
    }
    P& operator-=(P b) {
        x -= b.x;
        y -= b.y;
        return *this;
    }
    long long distSq() {
        return x*x + y*y;
    }
    long long operator*(const P& b) const {
        return x * b.y - y * b.x;
    }
    long long compareAngle(const P& reference, const P& target) {
        return (target - *this) * (reference - *this);
    }
};

void solve() {
    P p1, p2, p3;
    cin >> p1 >> p2 >> p3;
    long long crossProduct = p1.compareAngle(p2, p3);
    if (crossProduct < 0) {
        cout << "LEFT" << endl;
    } else if (crossProduct > 0) {
        cout << "RIGHT" << endl;
    } else {
        cout << "TOUCH" << endl;
    }
}

int main() {
    int t; cin >> t;
    while(t--) solve();
}
