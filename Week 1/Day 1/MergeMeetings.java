import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class MergeMeetings {

    public static class Meeting {

        private int startTime;
        private int endTime;

        public Meeting(int startTime, int endTime) {
            // number of 30 min blocks past 9:00 am
            this.startTime = startTime;
            this.endTime   = endTime;
        }

        public int getStartTime() {
            return startTime;
        }

        public void setStartTime(int startTime) {
            this.startTime = startTime;
        }

        public int getEndTime() {
            return endTime;
        }

        public void setEndTime(int endTime) {
            this.endTime = endTime;
        }

        @Override
        public boolean equals(Object o) {
            if (o == this) {
                return true;
            }
            if (!(o instanceof Meeting)) {
                return false;
            }
            final Meeting meeting = (Meeting) o;
            return startTime == meeting.startTime && endTime == meeting.endTime;
        }

        @Override
        public int hashCode() {
            int result = 17;
            result = result * 31 + startTime;
            result = result * 31 + endTime;
            return result;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", startTime, endTime);
        }
    }

    public static List<Meeting> mergeRanges(List<Meeting> meetings) {

        // merge meetings ranges
        char[] tracker = new char[48];
        
        for (Meeting one: meetings) {
            int start = one.getStartTime(),
                end = one.getEndTime();
                
            tracker[start] = '(';
            tracker[end] = ')';
        }
        
        int limit = tracker.length,
            openCount = 0,
            firstOpenAt = -1;
        boolean open = false;
        List<Meeting> ans = new ArrayList<>();

        for(int i = 0; i < limit; i++) {
            char current = tracker[i];
            if(current == '(') {
                if(!open) {
                    open = true;
                    firstOpenAt = i;
                }
                openCount += 1;
            }
            
            if(current == ')') {
                if(open) {
                    openCount -= 1;
                    if(openCount == 0) {
                        ans.add(new Meeting(firstOpenAt, i));
                        open = false;
                    }
                }
            }
        }

        return ans;
    }


















    // tests

    @Test
    public void meetingsOverlapTest() {
        final List<Meeting> meetings = Arrays.asList(new Meeting(1, 3), new Meeting(2, 4));
        final List<Meeting> actual = mergeRanges(meetings);
        final List<Meeting> expected = Arrays.asList(new Meeting(1, 4));
        assertEquals(expected, actual);
    }

    @Test
    public void  meetingsTouchTest() {
        final List<Meeting> meetings = Arrays.asList(new Meeting(5, 6), new Meeting(6, 8));
        final List<Meeting> actual = mergeRanges(meetings);
        final List<Meeting> expected = Arrays.asList(new Meeting(5, 8));
        assertEquals(expected, actual);
    }

    @Test
    public void meetingContainsOtherMeetingTest() {
        final List<Meeting> meetings = Arrays.asList(new Meeting(1, 8), new Meeting(2, 5));
        final List<Meeting> actual = mergeRanges(meetings);
        final List<Meeting> expected = Arrays.asList(new Meeting(1, 8));
        assertEquals(expected, actual);
    }

    @Test
    public void meetingsStaySeparateTest() {
        final List<Meeting> meetings = Arrays.asList(new Meeting(1, 3), new Meeting(4, 8));
        final List<Meeting> actual = mergeRanges(meetings);
        final List<Meeting> expected = Arrays.asList(
            new Meeting(1, 3), new Meeting(4, 8)
        );
        assertEquals(expected, actual);
    }

    @Test
    public void multipleMergedMeetingsTest() {
        final List<Meeting> meetings = Arrays.asList(
            new Meeting(1, 4), new Meeting(2, 5), new Meeting (5, 8));
        final List<Meeting> actual = mergeRanges(meetings);
        final List<Meeting> expected = Arrays.asList(new Meeting(1, 8));
        assertEquals(expected, actual);
    }

    @Test
    public void meetingsNotSortedTest() {
        final List<Meeting> meetings = Arrays.asList(
            new Meeting(5, 8), new Meeting(1, 4), new Meeting(6, 8));
        final List<Meeting> actual = mergeRanges(meetings);
        final List<Meeting> expected = Arrays.asList( 
            new Meeting(1, 4), new Meeting(5, 8)
        );
        assertEquals(expected, actual);
    }

    @Test
    public void sampleInputTest() {
        final List<Meeting> meetings = Arrays.asList(
            new Meeting(0, 1), new Meeting(3, 5), new Meeting(4, 8),
            new Meeting(10, 12), new Meeting(9, 10) 
        );
        final List<Meeting> actual = mergeRanges(meetings);
        final List<Meeting> expected = Arrays.asList( 
            new Meeting(0, 1), new Meeting(3, 8), new Meeting(9, 12)
        );
        assertEquals(expected, actual);
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