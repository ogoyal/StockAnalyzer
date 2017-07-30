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
#include <set>
#include <unordered_map>
#include "table.h"
#include "Graph.h"

typedef std::pair<std::string, float> csvPair;
std::map<std::string, float> alphaOrder(std::vector<std::string> name, std::vector<float> price);
std::unordered_map<std::string, float> numericOrder(std::vector<std::string> name, std::vector<float> price);

int main(int argc, const char * argv[]) {

    Table::DataTable csvTable;
    Table stocks;
    Graph graph;
    std::string name;
    std::map<std::string, float> alphaMap;
    std::unordered_map<std::string, float> numericMap;

    stocks.readFile();
    
    graph.getData(stocks);
    csvTable.name = graph.getName();
    csvTable.price = graph.getPrice();
    
    int choice = 1;

    try {
    switch(choice) {
	case 0:
    	    alphaMap = alphaOrder(csvTable.name, csvTable.price);
            for(auto c: alphaMap) {
              std::cout << c.first << " " << c.second <<std::endl;
            }
 	    break;
        case 1:
            numericMap = numericOrder(csvTable.name, csvTable.price);
	    break;
        default:
            std::cout << "Default case..." << std::endl; 
      }
    }
    catch(...) {
	std::cout << "csv map empty" << std::endl;
    }

    return 0;
}

struct sortPairSecond
{
   bool operator()(const csvPair &lhs, const csvPair &rhs)
   {
       return lhs.second > rhs.second;
   }
};

std::map<std::string, float> alphaOrder(std::vector<std::string> name, std::vector<float> price)
{
    std::map<std::string, float> csvMap;
    try {
        int range = name.size();
        if(name.size() == price.size()) {
            for(int i = 0; i < range; i++) {
	    	csvMap[name[i]] = price[i];
	    }
	}
    }
    catch(...) {
	std::cout << "name & price vectors size difference" << std::endl;
    }
    return csvMap;
}

std::unordered_map<std::string, float> numericOrder(std::vector<std::string> name, std::vector<float> price) {
    std::map<std::string, float> tmpMap = alphaOrder(name, price);
    std::unordered_map<std::string, float> csvMap;
    std::set<csvPair, sortPairSecond> csvSet;

    for(auto c: tmpMap) {
	csvSet.insert(c);
    }
    
    for(auto c: csvSet) {
        std::cout << c.first << " " << c.second << std::endl;
        csvMap[c.first] = c.second;
    }
    
    return csvMap;
}


