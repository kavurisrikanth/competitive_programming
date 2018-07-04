import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static void reverseWords(char[] message) {

        // decode the message by reversing the words
        reverse(message, 0, message.length-1);

        int i = 0, start = 0, end = 0;
        while(i <= message.length) {
            if(i == message.length || message[i] == ' ') {
                end = i - 1;
                reverse(message, start, end);
                
                start = i + 1;
            }
            
            i++;
        }
    }

    public static void reverse(char[] msg, int from, int to) {
        int forward = from,
            backward = to;
            
        while(forward < backward) {
            char temp = msg[forward];
            msg[forward] = msg[backward];
            msg[backward] = temp;
            
            forward++;
            backward--;
        }
    }
















    // tests

    @Test
    public void oneWordTest() {
        final char[] expected = "vault".toCharArray();
        final char[] actual = "vault".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void twoWordsTest() {
        final char[] expected = "cake thief".toCharArray();
        final char[] actual = "thief cake".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void threeWordsTest() {
        final char[] expected = "get another one".toCharArray();
        final char[] actual = "one another get".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void multipleWordsSameLengthTest() {
        final char[] expected = "the cat ate the rat".toCharArray();
        final char[] actual = "rat the ate cat the".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void multipleWordsDifferentLengthsTest() {
        final char[] expected = "chocolate bundt cake is yummy".toCharArray();
        final char[] actual = "yummy is cake bundt chocolate".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void emptyStringTest() {
        final char[] expected = "".toCharArray();
        final char[] actual = "".toCharArray();
        reverseWords(actual);
        assertArrayEquals(expected, actual);
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