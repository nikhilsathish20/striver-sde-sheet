class Solution {
    public int uniquePaths(int m, int n) {	
        if(m == 1 || n == 1) return 1;
        int upMove = uniquePaths(m-1, n);
        int leftMove = uniquePaths(m, n-1);        
        return upMove + leftMove;
    }
}