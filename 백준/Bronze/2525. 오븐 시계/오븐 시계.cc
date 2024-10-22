#include <bits/stdc++.h>

using namespace std;

int main(){
	int a, b, c;
	
	cin >> a >> b >> c;
	
	int temp = a * 60 + b + c;
	
	a = temp / 60;
	b = temp % 60;
	
	if(a >= 24) a -= 24;
	
	cout << a << " " << b;
}