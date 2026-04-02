class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        // Step 1: count frequency of each number
        for (int num : nums) {
            freq[num]++;
        }

        // Step 2: bucket where index = frequency
        vector<vector<int>> bucket(nums.size() + 1);

        for (auto& entry : freq) {
            int num = entry.first;
            int count = entry.second;
            bucket[count].push_back(num);
        }

        // Step 3: collect top k frequent elements
        vector<int> result;

        for (int i = nums.size(); i >= 1; i--) {
            for (int num : bucket[i]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result;
                }
            }
        }

        return result;
    
    }
};