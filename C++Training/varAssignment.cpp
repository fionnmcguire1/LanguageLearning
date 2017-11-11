/*
 * Author: Fionn Mcguire
 * Date: 1--11-2017
 * Description: Testing some variable limitations and different methodologies of assigning variables
 * */

#include <iostream>

using namespace std;

int main(){

	double a = 7.2;
	double b{7.2};
	double c = {7.2};
	auto d = 5;

	cout << "A: " << a << "\n";
	cout << "B: " << b << "\n";
	cout << "C: " << c << "\n";
	cout << "D: " << d << "\n";


	return 0;
}
