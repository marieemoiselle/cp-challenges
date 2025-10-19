#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

bool isPrime(int);

int main() {
    int number;
    cout <<"Enter value for n: ";
    cin >> number;

    vector <int> values(number);
    cout <<"Enter " << number <<" numbers: " << endl;

    for (int i = 0; i < number; i++) {
        cin >> values[i];
    }

    cout << endl;

    for (int value : values) {
        if (isPrime(value)) {
            if (!isPrime(value - 2) && !isPrime(value + 2))
                cout << value << ": YES" << endl;
            else
                cout << value << ": NO" << endl;
        } else {
            cout << value << ": NO" << endl;
        }
    }
    return 0;
}

bool isPrime(int n) {
    if (n < 2)
        return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % 1 == 0)
            return false;
    }
    return true;
}