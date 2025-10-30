#define _USE_MATH_DEFINES

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

double getSurfaceArea (double);
double getVolume (double);

int main() {
    double diameter;
    cout << "Diameter of the sphere: ";
    cin >> diameter;

    double radius = diameter / 2.0;
    double surfaceArea = getSurfaceArea(radius);
    double volume = getVolume(radius);

    cout << fixed << setprecision(4);
    cout << "Surface Area: " << surfaceArea << endl;
    cout << "Volume: " << volume << endl;

    return 0;
}

double getSurfaceArea(double radius) {
    return 4 * M_PI * radius * radius;

}

double getVolume(double radius) {
    return (4.0/3.0) * M_PI * pow(radius, 3);
}