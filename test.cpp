#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    string minWindow(string s, string t) {
        int left = 0;
        unordered_map<char, int> need;
        unordered_map<char, int> window;
        int len_min = 100000;
        int left_min = 0;
        int first = 0;
        int flag=0;
        int required=t.size();
        if(required>s.size()) return "";
        for(auto i:t){
            need[i]++;
        }
        for(int right=0;right<s.size();right++){
            char str=s[right];
            window[str]++;
            if(need.find(str) != need.end()&&window[str]==need[str]){
                flag++;
            }
            while(flag==required){
                int len = right-left+1;
                if(len<len_min){
                    len_min=len;
                    first = left;
                }
                char left_char = s[left];
                window[left_char]--;
                if(need.find(left_char)!=need.end() && window[left_char]<need[left_char]){
                    flag--;
                }
            }
        }
        // 修正：使用 substr 提取子字符串
        if (len_min == 100000) {
            return "";  // 没有找到有效窗口
        }
        string result = s.substr(first, len_min);
        return result;


        

        
    }
};

int main() {
    Solution sol;
    string result = sol.minWindow("ADOBECODEBANC", "ABC");
    return 0;
}