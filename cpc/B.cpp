#include <bits/stdc++.h>
using namespace std;

int main () {
  int N;
  cin >> N;
  int a[N];
  int b[N];
  for (int i=0; i < N; i++) {
    cin >> a[i];
  }
  for (int i=0; i < N; i++) {
    cin >> b[i];
  }
  int M;
  cin >> M;
  int c[M];
  int d[M];
  for (int i=0; i < M; i++) {
    cin >> c[i];
  }
  for (int i=0; i < M; i++) {
    cin >> d[i];
  }

  // 2^5 = pow(2, 5)
  int X, Y;
  X = 1;
  for (int i=0; i < N; i++) {
    X*=pow(a[i], b[i]);
  }
  Y = 1;
  for (int i=0; i < M; i++) {
    Y*=pow(c[i], d[i]);
  }
  // cout << X << " " << Y << endl;
  int count = 0;
  // cari pasangan p, q dari X ... Y
  for (int p=Y; p <= X; p += Y) {
    for (int q=Y; q <= X; q += Y) {
      if ( gcd (p,q) == Y && (p*q)/gcd (p,q) == X) {
        count +=1;
      }
    }
  }
  cout << count << endl;
}