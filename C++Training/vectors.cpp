/*
 * Author: Fionn Mcguire
 * Date: 02-11-2017
 * Description: Practicing Vectors
 * */

#include <iostream>
#include <vector>

using namespace std;


int addNumbers(int first, int second=0)
{
	return first+second;
}

int addNumbers(int first, int second, int third)
{
	return first+second+third;
}

int main()
{
	vector <int> lotteryNumVect(10);
	int lotteryNumArray[5] = {4,13,14,24,34};
	lotteryNumVect.insert(lotteryNumVect.begin(),lotteryNumArray,lotteryNumArray+3);

	lotteryNumVect.insert(lotteryNumVect.begin()+5,44);
	cout << lotteryNumVect.at(5) << "\n";

	lotteryNumVect.push_back(10);
	cout << "Final Value: " << lotteryNumVect.back() << "\n";
	// pop_back removes final value
		 
	cout << addNumbers(1) << "\n";
	cout << addNumbers(1,5,6) << "\n";



}
