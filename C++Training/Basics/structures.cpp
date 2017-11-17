/*
 * Author: Fionn Mcguire
 * Date: 15-11-2017
 * Description: Practicing structures
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct newperson
{
	char name[20];
	int age;
};

class Person{
		string firstname;
		string surname;
		int age;
		string address;
		string profession;
	public:

		void printDetails()
		{
			cout << "Name: " << firstname << " " << surname << "\n";
			cout << "Age: " << age << "\n";
			cout << "Address: " << address << "\n";
			cout << "Profession: " << profession << "\n";
		}

		Person (string first, string last, int a, string add, string prof){
			firstname = first;
			surname = last;
			age = a;
			address = add;
			profession = prof;
			printf("Created Person\n");
		}

		~Person (){
			printf("Destructed Person\n");
		}
};



int main(){

	newperson fionn = {"Fionn",23};
	cout << fionn.name << "\n";
	cout << fionn.age << "\n";

	
	Person Fionn("fionn", "mcguire", 23, "space", "computer");

	Fionn.printDetails();









	return 0;

}
