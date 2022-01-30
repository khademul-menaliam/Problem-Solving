class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
                unordered_map<int,int> mp;
        vector<int> pairs;
        
        for(int i=0;i<nums.size();i++){
            if(mp.find(target-nums[i]) != mp.end()){
                pairs.push_back(mp[target-nums[i]]);
                pairs.push_back(i);
                break;
            }
            else
                mp[nums[i]] = i;
        }
        
        return pairs;
    }
};