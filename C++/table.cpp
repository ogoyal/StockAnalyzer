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
#include <fstream>
#include <string>
#include "table.h"

void Table::openFile()
{
    std::string line;
    std::ofstream myFile(filename);

    myFile << "Date" << "," << "Stock" << "," << "Price" << '\n';
    if(myFile.is_open())
    {
        while (std::getline(std::cin,line))
        {
            if (not std::strcmp(line.c_str(), "Quit"))
            {
                break;
            }
            myFile << line << '\n';
            database.push_back(line);
        }
    }

    else
    {
        std::cout << "Error opening file" << std::endl;
    }

    myFile.close();
}

void Table::readFile()
{
    std::ifstream myFile(filename);
    std::string line;
    while (myFile.good())
    {
        getline(myFile, line);
        database.push_back(line);
    }
    myFile.close();
}

void Table::addEntry()
{
    std::ofstream myFile(filename);
    std::string line;
    std::getline(std::cin,line);
    myFile << line << '\n';
}

std::string Table::getLine(int num)
{
    std::string line;
    if(!database.empty())
    {
        line = database.at(num);
    }
    else
    {
        std::cout << "Database is empty!" << std::endl;
        return "";
    }
    return line;
}
