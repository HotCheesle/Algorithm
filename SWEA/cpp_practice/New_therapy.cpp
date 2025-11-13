#include <iostream>
// #include <bitset>

using namespace std;

void check_num(int number, int* bits);

int main() {
	int T, SHEP;
	cin >> T;
	for (int tc = 1; tc < T + 1; tc++) {
		cin >> SHEP;
		int shep = SHEP; int bit_mask = 0;
		while (bit_mask != 0b1111111111) {
			check_num(shep, &bit_mask);
			shep += SHEP;
			// cout << bitset<10>(bit_mask) << endl;
		}
		shep -= SHEP;
		cout << '#' << tc << ' ' << shep << endl;
	}

	return 0;
}

void check_num(int number, int* bits) {
	int num;
	while (number != 0) {
		num = number % 10;
		// cout << num << ' ';
		*bits |= (1 << num);
		number /= 10;
	}
	// cout << endl;
}