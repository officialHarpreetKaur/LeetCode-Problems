class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0 ||(x % 10 == 0 && x != 0)){
            return false;
        }
        int revN = 0;
        while(x > revN){
            revN = revN * 10 + x % 10;
            x /= 10;
        }
        return x == revN || x == revN / 10;
    }
}