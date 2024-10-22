#include <iostream>

using namespace std;

int main() {
	int n, min = 1000001, max = -1000001;

	cin >> n;

	int *arr = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];

		if (arr[i] < min) {
			min = arr[i];
		}
		if (arr[i] > max) {
			max = arr[i];
		}
	}
	cout << min << " " << max << endl;
	return 0;
}