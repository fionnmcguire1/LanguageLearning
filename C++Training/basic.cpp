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

	int largestInt = 2147483647;
	cout << "Largest int: " << largestInt << " \n";
	largestInt+=1;
	cout << "Largest Int: " << largestInt << " \n";
	
	
	int five = 5;

	//Demonstrating arithmetic operations
	cout << "5+5=" << five+five << "\n";	
	cout << "5-5=" << five-five << "\n";
	cout << "50/5=" << 50/five << "\n";
	cout << "5*5=" << five*five << "\n";
	cout << "51%5=" << 51%5 << "\n";
	cout << "5++=" << five++ << "\n";
	cout << "++5=" << ++five << "\n";
	cout << "5--=" << five-- << "\n";
	cout << "--5=" << --five << "\n";
	return 0;
}

