#include <iostream>
#include <string>

using namespace std;

int main() {
	int input1, input2;
	cin >> input1;

	for (int i = 0; i < input1; i++) {
		cin >> input2;
		int* arr = new int[input2];

		double sum = 0, avg = 0;

		for (int j = 0; j < input2; j++) {
			cin >> arr[j];

			sum += arr[j];
		}
		avg = sum / input2;
		double overAvg = 0;

		for (int j = 0; j < input2; j++) {
			if (arr[j] > avg) {
				overAvg++;
			}
		}
		cout << fixed;
		cout.precision(3);
		cout << overAvg / input2 * 100 << "%\n";
	}
	return 0;
}