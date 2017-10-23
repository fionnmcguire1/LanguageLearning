//
//  main.cpp
//  HelloWorld
//
//  Created by Fionn Mcguire on 23/10/2017.
//  Copyright © 2017 Fionn Mcguire. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    std::cout << "Hello, World!\n";
    int age;
    char name[6];
    std::cin >> name;
    std::cin >> age;
    std::cout << "\t Hello, " << name << " you are " << age << " years old!\n";
    return 0;
}
