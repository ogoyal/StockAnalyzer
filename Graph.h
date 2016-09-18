//
//  Graph.h
//  Programming in C++
//
//  Created by Ojas Goyal on 9/17/16.
//  Copyright (c) 2016 Ojas Goyal. All rights reserved.
//

#ifndef __Programming_in_C____Graph__
#define __Programming_in_C____Graph__

#include <stdio.h>
#include <iostream>
#include "table.h"

class Graph
{
private:
    int xaxis;
    int yaxis;
    std::string horizontal;
    std::string vertical;
    std::string name;
    std::string delta;
    std::string filename = "example.csv";
    
public:
    void createGraph();
    void displayData(std::vector<Table>);
    void getData(Table);
    std::string getWord(std::string, int);
};


#endif /* defined(__Programming_in_C____Graph__) */
