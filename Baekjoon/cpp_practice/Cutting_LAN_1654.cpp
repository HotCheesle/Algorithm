#include <iostream>
#include <vector>

using namespace std;

int get_count(vector<int> lans, int cut_len) {
	int cnt = 0;
	for (vector<int>::iterator iter = lans.begin(); iter != lans.end(); iter++) {
		cnt += *iter / cut_len;
	}
	return cnt;
}

int main() {
	int K, N, lan, lan_cm, cut_cnt = 0, tot_len = 0;
	cin >> K >> N;

	vector<int> lans;
	for (int i = 0; i < K; i++) {
		cin >> lan;
		lans.push_back(lan);
		tot_len += lan;
	}

	lan_cm = tot_len / N;

	while (N > cut_cnt) {
		cut_cnt = get_count(lans, lan_cm--);
    cout << cut_cnt << ' ';
	}

	cout << endl << ++lan_cm << endl;

	return 0;
}

