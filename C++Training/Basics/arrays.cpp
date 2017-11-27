/*
 * Author: Fionn Mcguire
 * Date: 01-11-2017
 * Description: Practicing Arrays
 * */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
//#include <cstdlib>

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

	/*
	int randomNum = (rand() % 100) +1;
	do 
	{
		cout << randomNum << "\n";
		randomNum = (rand() %100) +1;
	} while(randomNum != 100);*/
	int IntnumGuessed = 0;
	int numGuessed;
	do{
		cout << "Guess a number between 1 and 10\n";
		cin >> numGuessed;
		IntnumGuessed = numGuessed;
	}while(IntnumGuessed != 4);

	cout << "You win\n";

	int array1[10] = {1,2,3,4,5,6,7,8,9,10};
	for(auto i : array1)
	{
		cout << i << "\n";
	}


	return 0;
}
