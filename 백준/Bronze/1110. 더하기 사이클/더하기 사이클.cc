#include <iostream>

using namespace std;

int main() {
	int n, a = 0 , cycle = 0, temp = 0;

	cin >> n;
	temp = n;

	while (1) {
		a = n / 10 + n % 10;
		n = (n % 10) * 10 + a % 10;
		cycle++;

		if (temp == n) {
			cout << cycle;
			break;
		}
	}
	return 0;
}