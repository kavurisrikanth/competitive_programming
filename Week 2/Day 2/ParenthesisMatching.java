import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static int getClosingParen(String sentence, int openingParenIndex) {

        // find the position of the matching closing parenthesis
        int open = 0;
        boolean started = false;
        
        for(int i = openingParenIndex; i < sentence.length(); i++) {
            char cur = sentence.charAt(i);
            if(cur == '(') {
                if(!started)
                    started = true;
                open++;
            } else if(cur == ')')
                open--;
                
            if(open == 0 && started)
                return i;
                
        }

        throw new IllegalArgumentException("No matching closing parenthesis found.");
    }




    // tests

    @Test
    public void allOpenersThenClosersTest() {
        final int expected = 7;
        final int actual = getClosingParen("((((()))))", 2);
        assertEquals(expected, actual);
    }

    @Test
    public void mixedOpenersAndClosersTest() {
        final int expected = 10;
        final int actual = getClosingParen("()()((()()))", 5);
        assertEquals(expected, actual);
    }

    @Test(expected = Exception.class)
    public void noMatchingCloserTest() {
        getClosingParen("()(()", 2);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}