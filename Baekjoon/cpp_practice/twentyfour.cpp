#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
using namespace std;

int main() {
	string cur, end;
	cin >> cur >> end;

	int cur_h = stoi(cur.substr(0, 2));
	int cur_m = stoi(cur.substr(3, 2));
	int cur_s = stoi(cur.substr(6, 2));

	int cur_sec = cur_h * 3600 + cur_m * 60 + cur_s;

	int end_h = stoi(end.substr(0, 2));
	int end_m = stoi(end.substr(3, 2));
	int end_s = stoi(end.substr(6, 2));
	
	int end_sec = end_h * 3600 + end_m * 60 + end_s;

	int remain = 0;
	if (cur_sec > end_sec) {
		remain = (24 * 3600) - (cur_sec - end_sec);
	}
	else {
		remain = end_sec - cur_sec;
	}
	int times[3];
	for (int i = 2; i > -1; i--) {
		times[i] = remain / (int)pow(60, i);
		remain %= (int)pow(60, i);
	}

	printf("%02d:%02d:%02d\n", times[2], times[1], times[0]);

	return 0;
}