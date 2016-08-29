//
//  main.cpp
//  Programming in C++
//
//  Created by Ojas Goyal on 7/26/16.
//  Copyright (c) 2016 Ojas Goyal. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include "table.h"


int main(int argc, const char * argv[]) {
    Table::DataTable csvTable;
    Table table;
    std::string name;
    std::string header;

    table.readFile();
    header = table.getLine(0);
    
    return 0;
}
