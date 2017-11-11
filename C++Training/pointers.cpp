/*
 * Author: Fionn Mcguire
 * Date 11-11-2017
 * Description: Pointer practice
 * */

#include <iostream>

using namespace std;

int main()
{

	char v_array[6] = {'f','i','o','n','n','\0'};
	char* pointer = &v_array[4];
	char x = *pointer;
	cout << x << "\n";






	return 0;
}
