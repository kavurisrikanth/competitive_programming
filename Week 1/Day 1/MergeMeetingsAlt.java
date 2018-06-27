import java.util.*;
//
//import org.junit.Test;
//import org.junit.runner.JUnitCore;
//import org.junit.runner.Result;
//import org.junit.runner.notification.Failure;
//
//import static org.junit.Assert.*;

public class MergeMeetingsAlt {

    public static class Meeting {

        private int startTime;
        private int endTime;

        public Meeting(int startTime, int endTime) {
            // number of 30 min blocks past 9:00 am
            this.startTime = startTime;
            this.endTime = endTime;
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

        boolean[] tracker = new boolean[48];
        
        for(int i=0;i<meetings.size();i++){
            int start = meetings.get(i).startTime,
                limit = meetings.get(i).endTime;

            for(int j = start; j < limit; j++){
                tracker[j] = true;
            }
        }

        List<Meeting> mergedList = new ArrayList<>();
        boolean started = false;
        int start = 0, 
            end = 0;

        for(int i = 0; i < tracker.length; i++) {
            if(tracker[i] && !started){
                started = true;
                start = i;
            } else if(!tracker[i] && started){
                started = false;
                end = i;
                
                mergedList.add(new Meeting(start, end));
            }
        }
        return mergedList;
    }

    public static void main(String[] args){
        final List<Meeting> meetings = Arrays.asList(new Meeting(1, 3), new Meeting(2, 4),new Meeting(7,9));
        final List<Meeting> actual = mergeRanges(meetings);

    }


}