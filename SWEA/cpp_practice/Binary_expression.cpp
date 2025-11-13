#include <iostream>
// #include <bitset>

using namespace std;

int main() {
	int T;
	cin >> T;
	int sequence, number, mask;
	for (int tc = 1; tc < T + 1; tc++) {
		cin >> sequence >> number;
		mask = (1 << sequence) - 1;
		// cout << bitset<16>(sequence) << endl;
		int result = number & mask;
		if (result == mask) {
			cout << '#' << tc << " ON" << endl;
		}
		else {
			cout << '#' << tc << " OFF" << endl;
		}
	}

	return 0;
}
