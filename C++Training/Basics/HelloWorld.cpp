//
//  main.cpp
//  HelloWorld
//
//  Created by Fionn Mcguire on 23/10/2017.
//  Copyright © 2017 Fionn Mcguire. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    cout << "Hello, World!\n";
    int age;
    char name[6];
    cin >> name;
    cin >> age;
    cout << "\t Hello, " << name << " you are " << age << " years old!" << endl;
    return 0;
}
