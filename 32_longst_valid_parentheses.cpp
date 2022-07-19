#include <cstring>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int left = 0, right = 0, max1 = 0;
        //scan left to right
        for(auto x : s){
            if(x == '('){
                left ++;
            } else {
                right ++;
            }
            
            if (right == left) {
                max1 = max(max1, 2*right);
            } else if (right >= left) {
                left = right = 0;
            }
        }
        
        // scan right to left
        left = right = 0;
        for(auto x = s.crbegin(); x != s.crend(); ++x) {
            if(*x == '('){
                left ++;
            } else {
                right ++;
            }
            
            if (right == left) {
                max1 = (max1 < 2*left)?(2*left):max1;
            } else if (left >= right) {
                left = right = 0;
            }
        }
        return max1;
    }
};