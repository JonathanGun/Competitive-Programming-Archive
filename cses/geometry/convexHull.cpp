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
    bool operator<(const P& other) const {
        return make_pair(x, y) < make_pair(other.x, other.y);
    }
    long long compareAngle(const P& reference, const P& target) const {
        return (target - *this) * (reference - *this);
    }
    bool isInsideSegment(const P& p1, const P& p2) const {
        if ((*this).compareAngle(p1, p2) != 0) return false;
        return (
            min(p1.x, p2.x) <= x && x <= max(p1.x, p2.x) &&
            min(p1.y, p2.y) <= y && y <= max(p1.y, p2.y)
        );
    }
    bool isSegmentIntersectYAxis(P p1, P p2) const {
        if (p2 < p1) swap(p1, p2);
        if (p1.x <= x && x < p2.x && (*this).compareAngle(p1, p2) > 0) return true;
        return false;
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

void convexHull(vector<P>& hull, vector<P>& points) {
    int n = points.size();
    sort(points.begin(), points.end());
    for(int rep = 0; rep < 2; ++rep) {
        int S = hull.size();
        for(int i = 0; i < n; ++i) {
            P next = points[i];
            while(hull.size() >= S + 2) {
                P last = hull.end()[-1];
                P last2 = hull.end()[-2];
                if (last2.compareAngle(last, next) < 0) {
                    hull.pop_back();
                } else {
                    break;
                }
            }
            hull.push_back(next);
        }
        hull.pop_back();
        reverse(points.begin(), points.end());
    }
}

int main() {
    int n; cin >> n;
    vector<P>points(n);
    for(int i = 0; i < n; ++i) {
        cin >> points[i];
    }
    vector<P>hull;
    convexHull(hull, points);
    cout << hull.size() << endl;
    for(P p: hull) cout << p << endl;
}
