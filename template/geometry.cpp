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
    // detect side of Point target relative to Line this->reference
    // return negative if target on the LEFT side of this->reference
    // return 0 if colinear
    // return positive if target on the RIGHT side of this->reference
    long long detectSide(const P& reference, const P& target) const {
        return (target - *this) * (reference - *this);
    }
    // uses bounding box, treat p1 and p2 as diagonal point of rectangle
    // then check this.x and this.y is inside the box
    // return true if P this inside segment p1->p2
    bool isInsideSegment(const P& p1, const P& p2) const {
        if ((*this).detectSide(p1, p2) != 0) return false;
        return (
            min(p1.x, p2.x) <= x && x <= max(p1.x, p2.x) &&
            min(p1.y, p2.y) <= y && y <= max(p1.y, p2.y)
        );
    }
    // uses trick from errichto
    // imagine vertical line from this to positive infinity (top), but tilted ever slightly to the right
    // set p1 MORE LEFT than p2
    // segment p1->p2 will intersect Y axis if:
    // * p1.x is on the left (inclusive) and p2.x is on the right (exclusive).
    // * p2 is on the RIGHT side of this->p1 line
    bool isSegmentIntersectYAxis(P p1, P p2) const {
        if (p2 < p1) swap(p1, p2);
        if (p1.x <= x && x < p2.x && (*this).detectSide(p1, p2) > 0) return true;
        return false;
    }
};

bool isIntersect(P from, P to, P p1, P p2) {
    if ((to - from) * (p2 - p1) == 0) {
        if (from.detectSide(to, p1) != 0) {
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
        long long p1Pos = from.detectSide(to, p1);
        long long p2Pos = from.detectSide(to, p2);
        if (p1Pos > 0 && p2Pos > 0) return false;
        if (p1Pos < 0 && p2Pos < 0) return false;
        swap(from, p1); swap(to, p2);
    }
    return true;
}

long long polygonArea(vector<P>& polygon) {
    long long area = 0;
    for(int i = 1; i < polygon.size() - 1; ++i) {
        area += polygon[0].detectSide(polygon[i], polygon[i + 1]);
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
                if (last2.detectSide(last, next) < 0) {
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
