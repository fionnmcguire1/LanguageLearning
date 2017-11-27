/*
 * Author: Fionn Mcguire
 * Date: 02-11-2017
 * Description: Practicing File IO
*/

#include <fstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	string fionnQ = "Nothing is so common as the wish to be remarkable\n\t - William Shakespeare";
	ofstream writer("fionnQ.txt");
	if(!writer)
	{
		cout << "Cannot write to file\n";
		writer.close();
	}
	else
	{
		writer << fionnQ;
		char letter;
		ifstream reader("fionnQ.txt");
		if(!reader)
		{
			cout << "Cant open reader\n";
		}
		else
		{
			for(int i=0; !reader.eof(); i++)
			{
				reader.get(letter);
				cout << letter;
			}
		}
		reader.close();
	}
	return 0;
}
