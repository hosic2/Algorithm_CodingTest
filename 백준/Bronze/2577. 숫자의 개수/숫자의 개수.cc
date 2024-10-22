#include <iostream>

using namespace std;

int main() {
	int a, b, c, sum = 0, arr[10] = {0};

	cin >> a >> b >> c;
	sum = a * b * c;

	while (sum != 0) {
		arr[sum % 10]++;
		sum /= 10;
	}

	for (int out : arr) {
		cout << out << endl;
	}
	return 0;
}