#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() 
{
	const double PI = 3.1415926535;
	//Takes up 1byte in memory
	char myGrade = 'A';
	bool isHappy = true;
	int myAge = 23;
	double otherfavNum = 1.6547893456987345;

	cout << "Size of int " << sizeof(myAge) << " Bytes\n";
	cout << "Size of bool " << sizeof(isHappy) << " Bytes\n";
	cout << "Size of double " << sizeof(otherfavNum) << " Bytes\n";
	cout << "Size of char " << sizeof(myGrade) << " Bytes\n";
	cout << "Size of const double " << sizeof(PI) << " Bytes\n";

return 0;
}

