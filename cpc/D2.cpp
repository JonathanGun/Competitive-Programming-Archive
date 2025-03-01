#include <bits/stdc++.h>
using namespace std;

int main () {    
  int N, M, K;
  cin >> N >> M >> K;

  int arr[M];
  for (int i = 0; i < N;  i++) {
    for (int j = 0; j < M; j++) {
      cin >> arr[j];
    }
  }
  sort(arr, arr + M);

  long long max, dompet;
  dompet = 0;
  for (int i = K-1; i < M; i++) {
    dompet += arr[i];
  }
  cout << dompet << endl;
}