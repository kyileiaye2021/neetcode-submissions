class Solution {
    public int getSum(int a, int b) {

        // b is used as a carry
        // while carry is not equal to 0, we have to add it to a
        // a is res that we will return

        while (b != 0){
            int temp = (a & b) << 1;
            a ^= b;
            System.out.print(a);
            b = temp;
        }

        return a;
        
    }
}
