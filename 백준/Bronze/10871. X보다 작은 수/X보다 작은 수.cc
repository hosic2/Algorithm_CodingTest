#include <iostream>

using namespace std;

int main() {
	int count, a, num;

	cin >> count >> a;

	for (int i = 0; i < count; i++) {
		cin >> num;

		if (num < a) {
			cout << num << " ";
		}
	}
	return 0;
}