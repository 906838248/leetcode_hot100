#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    /**
     * 无重复字符的最长子串 - 滑动窗口法
     * 
     * 时间复杂度：O(n)
     * 空间复杂度：O(min(m, n))
     */
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) {
            return 0;
        }
        
        unordered_map<char, int> char_index;
        int max_length = 0;
        int left = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char c = s[right];
            
            if (char_index.find(c) != char_index.end() && char_index[c] >= left) {
                left = char_index[c] + 1;
            }
            
            char_index[c] = right;
             max_length = max(max_length, right - left + 1);
         }
         
         return max_length;
     }
};