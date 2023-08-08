
//#include <boost/optional.h>
#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <utility>
#include <map>

using namespace std;

std::map<std::string, int> functionThatSplits_a_stringByAnotherString(std::string s, std::string str2) {
    try {
        if (s == "") {//check for all bad strings
            throw std::runtime_error("");
        } else {
            if (str2 == ""){
                throw std::runtime_error("");
            }
            vector <std::string> *subStrings = new std::vector<string>();

            for(auto it = s.begin(); it <= s.end(); it++){
                if(str2.find(*it) == std::string::npos) {
                    continue;
                } else
                    subStrings->push_back(s.substr(0, it -s.begin()));
                    std::cout << "Added string to list!";
            }
            std::map<std::string, int> toReturn = std::map<std::string, int>();
            for (std::string ss: *subStrings) {
                //toReturn.insert(std::make_pair<std::string, int>(ss, 1));
                toReturn.insert(std::make_pair<std::string, int>(ss, 0));
            }
            return toReturn;
        }
    } catch (...) {
        throw std::runtime_error("");
        std::cout << "Failed to split strings.";
    }
}



