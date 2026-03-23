#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <array>

using namespace std;

/**
 * 字母异位词分组 - 使用 array 作为键
 * 
 * 时间复杂度：O(n × k)，其中 n 是字符串数量，k 是字符串平均长度
 * 空间复杂度：O(n × k)
 */
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 用于存储分组结果
        vector<vector<string>> groups;
        // 使用 array<int, 26> 作为键（可以哈希化）
        map<array<int, 26>, vector<string>> result;
        
        // 遍历每个字符串
        for (string str : strs) {
            // 初始化 26 个计数器的数组
            array<int, 26> count = {0};
            
            // 统计每个字符出现的次数
            for (char ch : str) {
                count[ch - 'a']++;
            }
            
            // 将字符串添加到对应的分组
            result[count].push_back(str);
        }
        
        // 将结果转换为 vector<vector<string>>
        for (auto& pair : result) {
            groups.push_back(pair.second);
        }
        
        return groups;
    }
};