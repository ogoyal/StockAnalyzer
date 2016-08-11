//
//  main.cpp
//  Programming in C++
//
//  Created by Ojas Goyal on 7/26/16.
//  Copyright (c) 2016 Ojas Goyal. All rights reserved.
//

#include <iostream>
#include "table.h"

struct Stock
{
    std::string name;
    double price;
};

int main(int argc, const char * argv[]) {
    Table sudoku;
    Stock comp;
    int **arry;
    arry = new int *[9];
    for(int i = 0; i < 9; i++)
    {
        arry[i] = new int[9];
    }
    
    sudoku.rows(9);
    sudoku.columns(9);
    sudoku.box();
    sudoku.fillBox(arry);
    sudoku.display();
    
    return 0;
}
