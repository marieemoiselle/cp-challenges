#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    cout << "Enter string: ";
    getline(cin, str);

    for (char &c : str) {
        c = tolower(c);
    }

    int steps = 0;
    for (int i = 0; i + 2 < str.size(); i++) {
        // check if current substring is "ada"
        if (str[i] == 'a' && str[i + 1] == 'd' && str[i + 2] == 'a') {
            steps++;
            str[i + 2] = 'd';
        }
    }

    cout << "Ada: " << steps << endl;
    return 0;
}