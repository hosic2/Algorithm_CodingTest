#include <iostream>

using namespace std;

int main() {
	int a,b;

	while (true) {
		if (scanf("%d %d", &a, &b) == EOF) {
			break;
		}
		cout << a + b << endl;
	}
	return 0;
}