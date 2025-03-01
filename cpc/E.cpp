#include <bits/stdc++.h>
using namespace std;

int main () {  
  int N, Q;
  cin >> N >> Q;
  long long arr[Q];
  for (int i = 0; i < Q; i++) {
    cin >> arr[i];
  }
  long long biaya;
  biaya = 0;
  long long posisi;
  posisi = 1;
  long long hargaKmrn = arr[0];
  for (int i = 0; i < Q; i++) {
    int tipe;
    cin >> tipe;
    if (tipe == 1) {
      int X, Y;
      cin >> X >> Y;
      biaya += (abs (posisi-X))*min(hargaKmrn, arr[i]);
      biaya += (abs (X-Y) )*arr[i];
      posisi = Y;
      hargaKmrn = arr[i];
    } else {
      int tmp;
      cin >> tmp;
      hargaKmrn = min(hargaKmrn, arr[i]);
    }
  }
  cout << biaya << endl;
}