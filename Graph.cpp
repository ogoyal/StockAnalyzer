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

void Graph::displayData(std::vector<Table> data)
{

}

std::string Graph::getWord(std::string line, int index)
{
    std::vector<std::string> word;
    boost::split(word, line, boost::is_any_of(","));
    return word[index];
}

void Graph::getData(Table stocks)
{

    for(auto c: stocks.database)
    {
        if (! c.empty())
        {
            name = getWord(c,1);
            delta = getWord(c,3);
            std::cout << name << " " << delta << std::endl;
        }
    }
    // std::vector<Table> data;
    // return data;
}
