#include <bits/stdc++.h>
using namespace std;

int main () {    
  int N, M, K;
  cin >> N >> M >> K;

  if (N == 1) {
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
  } else if (K == 1) {
    int arr[N][M];
    for (int i = 0; i < N;  i++) {
      for (int j = 0; j < M; j++) {
        cin >> arr[i][j];
      }
    }

    long long max, dompet;
    dompet = 0;
    // buat masing kolom cari baris paling besar
    for (int j = 0; j < M; j++) {
      max = arr[0][j];
      for (int i = 0; i < N; i++) {
        if (arr[i][j] > max) {
          max = arr[i][j];
        }
      }
      dompet+=max;
    }
    cout << dompet << endl;
  } else {
    // N == 2, K == 2
    int arr[N][M];
    for (int i = 0; i < N;  i++) {
      for (int j = 0; j < M; j++) {
        cin >> arr[i][j];
      }
    }

    long long max, dompet, maxI, maxJ;
    dompet = 0;
    // buat masing kolom cari baris paling besar
    for (int j = 0; j < M - K + 1; j++) {
      max = arr[0][j];
      maxI = 0;
      maxJ = j;
      for(int k = 0; k < K; k++) {
        for (int i = 0; i < N; i++) {
          // cout << i << " " << j + k << " check:" << arr[i][j + k] << endl;
          if (arr[i][j + k] > max) {
            max = arr[i][j + k];
            maxI = i;
            maxJ = j + k;
          }
        }
      }
      arr[maxI][maxJ] = 0;
      // cout << max << " ";
      dompet+=max;
    }
    // cout << endl;
    cout << dompet << endl;
  }
}
