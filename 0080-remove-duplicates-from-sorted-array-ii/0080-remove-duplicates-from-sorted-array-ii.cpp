class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() <= 2) return nums.size();
        int j=0;
        for( int i=2; i<nums.size(); i++){
            if(nums[i] != nums[j]){
                nums[j+2] = nums[i];
                j++;
            }
        }
        return j+2;
    }
};