/*
 *Author: Fionn Mcguire
 *Date: 01-11-2017
 *Description: Using conditionals C++
 * 
 */

#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int age = 70;
	int ageAtLastExam = 16;
	bool notDUI = true;

	if(((age >= 1) && (age <= 16)) || notDUI == false)
	{
		cout << "You cant Drive!\n";
	}
	else
	{
		cout << "Shut up and Drive!!!\n";
	}
	
	int switchOption = (5>2) ? 5:2;

	switch(switchOption)
	{

		case 1:
			cout << "Fionn\n";
			break;
		case 2:
			cout << "Mike\n";
			break;
		case 3:
			cout << "Paul\n";
			break;
		case 4:
			cout << "John\n";
			break;
		case 5:
			cout << "Ian\n";
			break;
		default:
			cout << "Hello\n";

	}

	int checker = 5;
	if(checker == 5) cout << "One line conditional!\n";



	return 0;
}
