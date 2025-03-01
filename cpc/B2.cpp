#include <bits/stdc++.h>
#include <map>
#include <set>
#define MOD 998244353
using namespace std;


int mpow(long long x, unsigned int y, int p) {
  int res = 1;
  x = x % p;
  if (x == 0) return 0;
  while (y > 0) {
    if (y & 1) res = (res*x) % p;
    y = y >> 1;
    x = (x * x) % p;
  }
  return res;
}

int main () {
  set<int> allNum;

  int N; cin >> N;
  int a[N];
  map<int, int> b;
  for (int i=0; i < N; i++) {
    cin >> a[i];
    allNum.insert(a[i]);
  }
  for (int i=0; i < N; i++) {
    int x; cin >> x;
    b.insert(make_pair(a[i], x));
  }

  int M; cin >> M;
  int c[M];
  map<int, int> d;
  for (int i=0; i < M; i++) {
    cin >> c[i];
    allNum.insert(c[i]);
  }
  for (int i=0; i < M; i++) {
    int x; cin >> x;
    d.insert(make_pair(c[i], x));
  }

  for(int num: allNum) {
    if (b.find(num) == b.end()) {
      b.insert(make_pair(num, 0));
    }
    if (d.find(num) == d.end()) {
      d.insert(make_pair(num, 0));
    }
  }

  map<int, int> kpk, fpb;
  int diff = 0;
  for(int num: allNum) {
    // cout << num << " " << b[num] << " " << d[num] << endl;
    int cur = b[num] - d[num];
    if (cur < 0) {
      cout << 0 << endl;
      return 0;
    }
    diff += cur;
    // kpk.insert(make_pair(num, max(b[num], d[num])));
    // fpb.insert(make_pair(num, min(b[num], d[num])));
  }

  // long long kpkNum = 1;
  // for(pair<int, int> pii: kpk) {
  //   kpkNum *= pow(pii.first, pii.second);
  // }
  // cout << kpkNum << endl;

  // long long fpbNum = 1;
  // for(pair<int, int> pii: fpb) {
  //   fpbNum *= pow(pii.first, pii.second);
  // }
  // cout << fpbNum << endl;

  cout << mpow(2, max(0, diff - 1), MOD) << endl;
  // cout << pow(2, diff - 1) << endl;
}