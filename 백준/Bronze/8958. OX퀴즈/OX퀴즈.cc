#include <iostream>
#include <string>

using namespace std;

int main() {
	int input, sum, count;
	string s;
	cin >> input;

	for (int i = 0; i < input; i++) {
		cin >> s;

		sum = count = 0;

		for (int j = 0; j < s.length(); j++){
			if (s[j] == 'O') {
				count++;
			}
			else {
				count = 0;
			}
			sum += count;
		}
		cout << sum << endl;
	}
	return 0;
}