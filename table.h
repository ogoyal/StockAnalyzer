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
    std::string filename = "example.csv";

public:
    struct DataTable
    {
        std::vector<std::string> date;
        std::vector<std::string> stock;
        std::vector<double> price;
    };

    std::vector<std::string> database;
    void createFile();
    void readFile();
    void openFile();
    void addEntry();
    std::string getLine(int);
};


#endif
