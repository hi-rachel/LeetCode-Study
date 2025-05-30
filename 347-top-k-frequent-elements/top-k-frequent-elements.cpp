class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqCntMp;
        vector<vector<int>> v(nums.size()+1, vector<int>());
        int maxSize = 0;
        for(int i=0;i<nums.size();i++){
            freqCntMp[nums[i]]+=1;
            v[freqCntMp[nums[i]]].push_back(nums[i]);
            if(maxSize<freqCntMp[nums[i]])
                maxSize = freqCntMp[nums[i]];
        }
        for(int idx = maxSize;idx>0;idx--){
            if(v[idx].size()==k){
                return v[idx];
            }
        }
        return vector<int>();
    }
};