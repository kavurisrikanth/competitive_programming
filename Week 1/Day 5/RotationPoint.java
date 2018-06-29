import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class RotationPoint {

    public static int findRotationPoint(String[] words) {

        // find the rotation point in the array
        int someAWord = binarySearch(words);
        while(words[someAWord].charAt(0) == 'a' && someAWord >= 0) {
            someAWord--;
        }

        return someAWord + 1;
    }

    private static int binarySearch(String[] words) {
        int start = 0,
                end = words.length,
                mid = 0;
        char firstChar = words[0].charAt(0);

        while (start < end) {
            mid = (start + end)/2;
            String current = words[mid];
            char currentChar = current.charAt(0);

            if(currentChar == 'a')
                return mid;

            if(currentChar >= firstChar && currentChar <= 'z')
                start = mid + 1;

            if(currentChar >= 'a' && currentChar <= firstChar)
                end = mid;
        }

        return 0;
    }

    // tests

    @Test
    public void smallArrayTest() {
        final int actual = findRotationPoint(new String[] {"cape", "cake"});
        final int expected = 1;
        assertEquals(expected, actual);
    }

    @Test
    public void mediumArrayTest() {
        final int actual = findRotationPoint(new String[] {"grape", "orange", "plum",
                "radish", "apple"});
        final int expected = 4;
        assertEquals(expected, actual);
    }

    @Test
    public void largeArrayTest() {
        final int actual = findRotationPoint(
                new String[] {"ptolemaic", "retrograde", "supplant", "undulate", "xenoepist",
                        "asymptote", "babka", "banoffee", "engender", "karpatka", "othellolagkage"});
        final int expected = 5;
        assertEquals(expected, actual);
    }

    @Test
    public void possiblyMissingEdgeCaseTest() {
        // are we missing any edge cases?
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