#include <iostream>

using namespace std;

int main() {
	int arr[42] = {0}, count = 0, num = 0;

	for (int i = 0; i < 10; i++) {
		cin >> num;

		if (!arr[num % 42]) {
			arr[num % 42] = true;
			count++;
		}
	}
	cout << count;
	return 0;
}