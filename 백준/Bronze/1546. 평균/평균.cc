#include <iostream>

using namespace std;

int main() {
	int num, max = 0, arr[1000] = {};
	double sum = 0;

	cin >> num;

	for (int i = 0; i < num; i++) {
		cin >> arr[i];
		if (arr[i] > max) {
			max = arr[i];
		}
		sum += arr[i];
	}

	cout << fixed;
	cout.precision(2);
	cout << (sum / max * 100) / num;

	return 0;
}