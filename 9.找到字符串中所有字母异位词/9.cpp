#include <string>
#include <vector>
#include <unordered_map>


class Solution {
public:
    /**
     * 找到字符串中所有字母异位词 - 滑动窗口法
     * 
     * 时间复杂度：O(n)
     * 空间复杂度：O(1)，只有26个字母
     */
    std::vector<int> findAnagrams(std::string s, std::string p) {
        if (p.empty() || p.length() > s.length()) {
            return {};
        }
        
        std::vector<int> result;
        std::vector<int> target(26, 0);
        std::vector<int> window(26, 0);
        
        for (char c : p) {
            target[c - 'a']++;
        }
        
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            window[s[right] - 'a']++;
            
            if (right - left + 1 > p.length()) {
                window[s[left] - 'a']--;
                left++;
            }
            
            if (window == target) {
                result.push_back(left);
            }
        }
        
        return result;
    }
};


#include <iostream>
int main() {
    Solution solution;
    
    std::cout << "===== 测试结果 =====" << std::endl;
    
    std::vector<std::pair<std::pair<std::string, std::string>, std::vector<int>>> test_cases = {
        {{"cbaebabacd", "abc"}, {0, 6}},
        {{"abab", "ab"}, {0, 1, 2}},
        {{"baa", "aa"}, {1}},
        {{"", "abc"}, {}},
        {{"abc", ""}, {}},
        {{"a", "a"}, {0}},
        {{"a", "b"}, {}},
    };
    
    for (size_t i = 0; i < test_cases.size(); i++) {
        std::string s = test_cases[i].first.first;
        std::string p = test_cases[i].first.second;
        std::vector<int> expected = test_cases[i].second;
        std::vector<int> result = solution.findAnagrams(s, p);
        
        bool passed = result == expected;
        
        std::cout << "测试用例 " << (i + 1) << "：" << (passed ? "通过" : "失败") << std::endl;
        std::cout << "  s='" << s << "', p='" << p << "'" << std::endl;
        std::cout << "  期望：";
        for (int idx : expected) std::cout << idx << " ";
        std::cout << std::endl;
        std::cout << "  实际：";
        for (int idx : result) std::cout << idx << " ";
        std::cout << std::endl;
        std::cout << std::endl;
    }
    
    return 0;
}
