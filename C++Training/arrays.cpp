/*
 * Author: Fionn Mcguire
 * Date: 01-11-2017
 * Description: Practicing Arrays
 * */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int myFavNums[5];
	int badNums[5] = {4,5,6,7,8};

	cout << "Bad Number: " << badNums[0] << "\n";
	//Strings have double quotes chars always have single quotes
	char myName[2][7] = {{'F','i','o','n','n'},
		{'M','c','g','u','i','r','e'}};
	int rows = sizeof myName / sizeof myName[0];
	int cols = sizeof myName[0] / sizeof(char);
	for(int i = 0; i<rows;i++)
	{
		for(int j=0; j < cols;j++)
		{
			cout << myName[i][j];
		}
		cout << "\n";
	}

	




	return 0;
}
