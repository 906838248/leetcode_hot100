#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() <= 1) {
            return intervals;
        }

        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[0] < b[0];
             });

        vector<vector<int>> merged;
        merged.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); i++) {
            vector<int>& current = intervals[i];
            vector<int>& last_merged = merged.back();

            if (current[0] <= last_merged[1]) {
                last_merged[1] = max(last_merged[1], current[1]);
            } else {
                merged.push_back(current);
            }
        }

        return merged;
    }
};
