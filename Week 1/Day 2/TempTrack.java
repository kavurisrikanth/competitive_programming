import java.util.List;
import java.util.ArrayList;

public class TempTrack {

    static class TempTracker {

        // fill in the TempTracker class methods below
        int[] temperatures = new int[111];
        double sum = 0.0, mean = 0.0;
        int min = 0, max = 0, numInserts = 0, mostSoFar = 0, mode = -1; 

        // records a new temperature
        public void insert(int temperature) {
            // Assume the list is sorted to begin with
            temperatures[temperature] += 1;
            numInserts += 1;
            
            min = 110;
            max = 0;
            
            sum = 0;
            for(int i = 0; i < 111; i++) {
                int current = temperatures[i];
                if(current != 0) {
                    sum += (i * current);
                    
                    if(i < min)
                        min = i;
                        
                    if(i > max)
                        max = i;
                        
                    if(current > mostSoFar) {
                        mostSoFar = current;
                        mode = i;
                    }
                }
            }
            mean = sum/numInserts;
        }

        // returns the highest temp we've seen so far
        public int getMax() {
            return max;
        }

        // returns the lowest temp we've seen so far
        public int getMin() {
            return min;
        }

        // returns the mean of all temps we've seen so far
        public double getMean() {
            return mean;
        }

        // return a mode of all temps we've seen so far
        public int getMode() {
            return mode;
        }
    }


    public static void main(String[] args) {
        
    }
}