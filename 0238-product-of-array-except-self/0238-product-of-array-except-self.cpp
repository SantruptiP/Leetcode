class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(),1);
        int prefix_product = 1;
        int suffix_product = 1;
        int i;
        for(i=0;i<nums.size();i++){
            result[i] = prefix_product;
            prefix_product = prefix_product * nums[i];
        }
        for(i=nums.size()-1;i>=0;i--){
            result[i] = suffix_product * result[i];
            suffix_product = suffix_product * nums[i]; 
        }
        return result;
    }
};