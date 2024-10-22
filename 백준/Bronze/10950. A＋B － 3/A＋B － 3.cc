#include <iostream>

using namespace std;

int main(){
    int cycle, a, b;
    
    cin >> cycle;
    
    for(int i = 0; i < cycle; i++){
        cin >> a >> b;
        cout << a + b << endl;
    }
}