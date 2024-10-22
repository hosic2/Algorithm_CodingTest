#include <iostream>

using namespace std;

int main() {
	int arr[9], max = 0, number = 0;

	for (int i = 0; i < 9; i++) {
		cin >> arr[i];

		if (arr[i] > max) {
			max = arr[i];
			number = i + 1;
		}
	}
	cout << max << endl;
	cout << number;
	return 0;
}