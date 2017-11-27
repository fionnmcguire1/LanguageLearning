/*
 * Author: Fionn Mcguire
 * Date: 17-11-2017
 * Description: Practicing Making a linked list
 */


#include <iostream>
#include <cstdlib>

using namespace std;

struct Node()
{
	int data;
	Node* next;
};

class LinkedList()
{
	private:
		typedef struct Node{
			int data;
			Node* next;
		}* nodePtr;
		nodePtr head;
		nodePtr curr;
		nodePtr temp;

	public:
		LinkedList();
		void AddNode(int data);
		void DeleteNode(int data);
		void PrintList();

			


};
int ()
{




	return 0;
}
