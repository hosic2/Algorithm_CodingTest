#include <iostream>

using namespace std;

int main() {
	int count;

	cin >> count;

	for (int i = 1; i <= count; i++) {
		for (int j = count - 1; j >= i; j--) {
			cout << " ";
		}
		for (int j = 1; j <= i; j++) {
			cout << "*";
		}
		cout << "\n";
	}
	return 0;
}