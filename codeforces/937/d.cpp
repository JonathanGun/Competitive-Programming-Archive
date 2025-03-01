#include <iostream>
#include <string>

using namespace std;

int main() {
	int tsc;
	cin >> tsc;
	int bin[32] = {
    10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111,
    10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111, 11000, 11001, 11010,
	11011, 11100, 11101, 11110, 11111, 100000 
	};
    // sort bin array descend
    sort(bin, bin + 32, greater<int>());
	for(int i = 0; i < tsc; i++){
		int inp;
		cin >> inp;
		for(int j = 0; j < 31; j++){
			if(inp % bin[j] == 0){
				inp /= bin[j];
				j = 0;
			}
		}
        cout << inp << endl;
		
		if(inp != 1){
			cout << "NO" << endl;
		} else {
			cout << "YES" << endl;
		}
	}
    return 0;
}
