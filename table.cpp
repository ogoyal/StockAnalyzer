//
//  table.cpp
//  Programming in C++
//
//  Created by Ojas Goyal on 7/30/16.
//  Copyright (c) 2016 Ojas Goyal. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include "table.h"


void Table::rows(int num)
{
    nrows = num;
}

void Table::columns(int num)
{
    ncols = num;
}

void Table::box()
{
    nelems = nrows * ncols;
}

void Table::fillBox(int **arr)
{
    srand(time(NULL));
    for(int i = 0; i < nrows; i++)
    {
        for(int j = 0; j < ncols; j++)
        {
            arr[i][j] = random();
        }
    }
    arry = arr;
}
 
void Table::display()
{
    std::cout << "Box Values: " << std::endl;
    for(int i = 0; i < nrows; i++)
    {
        for(int j = 0; j < ncols; j++)
        {
            std::cout << arry[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int Table::random()
{
    nrand = rand() % 9 + 1;
    return nrand;
}

