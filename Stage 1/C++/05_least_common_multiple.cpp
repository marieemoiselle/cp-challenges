#include <iostream>
using namespace std;

long long getGCD (long long, long long);
long long getLCM (long long, long long);

int main () {
    int n;
    cout << "Enter number of inputs: ";
    cin >> n;

    long long num;
    cout << "Enter " << n << " inputs: ";
    cin >> num;

    long long result = num;

    // LCM iteration
    for (int i = 1; i < n; i ++) {
        cin >> num;
        result = getLCM(result, num);
    }

    cout << "LCM = " << result << endl;
}

long long getGCD(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long getLCM(long long a, long long b) {
    return (a * b) / getGCD(a, b);
}