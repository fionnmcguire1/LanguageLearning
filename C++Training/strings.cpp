/*
 * Author: Fionn Mcguire
 * Date: 02-11-2017
 * Description: Practicing Strings
*/

#include <iostream>
#include <string>

using namespace std;

int main()
{
	char happy[6] = {'H','a','p','p','y','\0'};
	string birthday = " Birthday";
	cout << happy + birthday << "\n";

	cout << "Size: " << birthday.size() << "\n";
	cout << "Is string empty " << birthday.empty() << "\n";
	cout << birthday.append("!") << "\n";
	cout << "Compare: " << birthday.compare(" Birthday") << "\n";
	//Substr
	string substr = birthday.assign(birthday,1,5);
	cout << substr << "\n";	
	//Search
	int IndexOfSubstr = birthday.find("th",0);
	cout << IndexOfSubstr << "\n";


	birthday.insert(0, "Happy");
	cout << birthday << "\n";

	birthday.replace(5,8, "Graduation!");
	cout << birthday << "\n";
	
	birthday.erase(5,11);
	cout << birthday << "\n";


	return 0;
}

