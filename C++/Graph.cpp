//
//  Graph.cpp
//  Programming in C++
//
//  Created by Ojas Goyal on 9/17/16.
//  Copyright (c) 2016 Ojas Goyal. All rights reserved.
//

#include "Graph.h"
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <boost/algorithm/string.hpp>

void Graph::createGraph()
{

}

std::vector<std::string> Graph::getName()
{
    std::vector<std::string> rName;
    try {
        for (auto c: sconn) {
            rName.push_back(c.first);
        }
    }
    catch(...) {
        std::cout << "Something wrong with name" << std::endl;
    }
    return rName;        
}

std::vector<float> Graph::getPrice()
{
    char* idx;
    std::vector<float> rPrice;
    try {
    for (auto c: sconn) {
        value = std::strtof(c.second.c_str(), &idx);
	rPrice.push_back(value);
      }
    }
    catch(...) {
        std::cout << "Something wrong with strtof" << std::endl;
    }
    return rPrice;
}

std::string Graph::getWord(std::string line, int index)
{
    std::vector<std::string> word;
    boost::split(word, line, boost::is_any_of(","));
    return word[index];
}

void Graph::getData(Table stocks)
{
    bool first = true;
    for(auto c: stocks.database)
    {
        if (! c.empty() and first == false)
        {
            name = getWord(c,1);
            delta = getWord(c,3);
	    sconn[name] = delta;
        }
	first=false;
    }

}
