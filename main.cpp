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
#include "graph.h"

int main(int argc, const char * argv[]) {
    Table::DataTable csvTable;
    Table stocks;
    Graph graph;
    std::string name;
    std::string header;

    stocks.readFile();
    header = stocks.getLine(0);
    
    graph.getData(stocks);
    //graph.createGraph();    
    csvTable.price = graph.getPrice();

    return 0;
}
