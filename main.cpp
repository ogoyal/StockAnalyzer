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
    std::map<std::string, float> csvMap;

    stocks.readFile();
    
    graph.getData(stocks);
    csvTable.name = graph.getName();
    csvTable.price = graph.getPrice();

    try {
        int range = csvTable.name.size();
        if(csvTable.name.size() == csvTable.price.size()) {
            for(int i = 0; i < range; i++) {
	    	csvMap[csvTable.name[i]] = csvTable.price[i];
	    }
	}
    }
    catch(...) {
	std::cout << "name & price vectors size difference" << std::endl;
    }
    for(auto c: csvMap) {
        std::cout << c.first << " " << c.second <<std::endl;
    }

    return 0;
}
