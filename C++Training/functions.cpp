/*
 * Author: Fionn Mcguire
 * Date: 07-11-2017
 * Description: Working with functions
 */



#include <iostream>
#include <fstream>
#include <vector>
#include <string>


using namespace std;


//Define functions outside of main
int addNumbers(int firstNum,int secondNum=0)
{
	return firstNum + secondNum;
}
//You can use the same function name but they must have different inputs
int addNumbers(int f,int s,int t)
{
	return f+s+t;
}







int main()
{
	int f = 1;
	int s = 2;
	int t = 3;	

	cout << "1 Number: " << addNumbers(f) << "\n";
	cout << "2 Numbers: " << addNumbers(f,s) << "\n";
	cout << "3 Numbers: " << addNumbers(f,s,t) << "\n";


	return 0;
}
