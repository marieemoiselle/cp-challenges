#include <iostream>
using namespace std;

long long tribonacci(int);

int main() {
    int n;
    cout << "Enter n: ";
    cin >> n;

    cout << "Element " << n << " of the Tribonacci Sequence: " << tribonacci(n) << endl;

    return 0;
}

long long tribonacci(int n) {

    // Base cases -> handling first three
    if (n == 0) {
        return 0;
    }
    if (n == 1 || n == 2) {
        return 1;
    }

    // Recursive case
    return tribonacci(n - 1) + tribonacci (n - 2) + tribonacci (n - 3);
}