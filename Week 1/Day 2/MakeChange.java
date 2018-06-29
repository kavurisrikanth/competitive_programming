public class MakeChange {

    public static int changePossibilities(int amount, int[] denominations, int len) {

        // calculate the number of ways to make change
        if(amount < 0)
            return 0;
            
        if(amount == 0)
            return 1;
            
        if(len <= 0)
            return 0;
            
        return changePossibilities(amount, denominations, len - 1) + 
                changePossibilities(amount - denominations[len-1], denominations, len);
    }


    public static void main(String[] args) {
        System.out.println(changePossibilities(10, new int[] {1, 2}, 2));
    }
}   