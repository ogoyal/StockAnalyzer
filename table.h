//
//  table.h
//  Programming in C++
//
//  Created by Ojas Goyal on 7/30/16.
//  Copyright (c) 2016 Ojas Goyal. All rights reserved.
//

#ifndef Programming_in_C___table_h
#define Programming_in_C___table_h

#include <vector>

class Table
{
private:
    int nrows;
    int ncols;
    int nelems;
    int nrand;
    int **arry;
    //std::vector<std::vector<int>> vec();
    
public:
    void rows(int);
    void columns(int);
    void box();
    void display();
    void fillBox(int **arr);
    int random();
};


#endif
