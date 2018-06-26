import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class RectangleIntersect {

    public static class Rectangle {

        // coordinates of bottom left corner
        private int leftX;
        private int bottomY;
    
        // dimensions
        private int width;
        private int height;
    
        public Rectangle() {}

        public Rectangle(int leftX, int bottomY, int width, int height) {
            this.leftX = leftX;
            this.bottomY = bottomY;
            this.width  = width;
            this.height = height;
        }

        public int getLeftX() {
            return leftX;
        }

        public int getBottomY() {
            return bottomY;
        }

        public int getWidth() {
            return width;
        }

        public int getHeight() {
            return height;
        }

        @Override
        public String toString() {
            return String.format("(left: %d, bottom: %d, width: %d, height: %d)",
                leftX, bottomY, leftX + width, bottomY + height);
        }

        @Override
        public boolean equals(Object o) {
            if (o == this) {
                return true;
            }
            if (!(o instanceof Rectangle)) {
                return false;
            }
            final Rectangle r = (Rectangle) o;
            return leftX == r.leftX && bottomY == r.bottomY
                   && width == r.width && height == r.height;
        }

        @Override
        public int hashCode() {
            int result = 17;
            result = result * 31 + leftX;
            result = result * 31 + bottomY;
            result = result * 31 + width;
            result = result * 31 + height;
            return result;
        }
    }

    public static Rectangle findRectangularOverlap(Rectangle rect1, Rectangle rect2) {

        // calculate the overlap between the two rectangles 
        if(rect1.equals(rect2))
            return rect1;
            
        // Right X Point of First Rectangle
        int rightXOne = rect1.getLeftX() + rect1.getWidth();
        
        //Right X Point of Second Rectangle
        int rightXTwo = rect2.getLeftX() + rect2.getWidth(); 
        
        //Top Y Point of First Rectangle
        int topYOne = rect1.getBottomY() + rect1.getHeight(); 
        
        //Top Y Point of Second Rectangle
        int topYTwo = rect2.getBottomY() + rect2.getHeight(); 
        
        
        //If Rectangles intersect, Left X Will be Right Most of Input's Left Xs...
        int resultLeftX = Math.max(rect1.getLeftX(), rect2.getLeftX());
        
        //...and Bottom Y Will be Higher of Input's Bottom Ys
        int resultBottomY = Math.max(rect1.getBottomY(), rect2.getBottomY());
        
        //Width is Distance Between Left Most of Input's Right Xs, and Left X of Intersection
        int resultWidth = Math.min(rightXOne, rightXTwo) - resultLeftX;
        
        //Height is Distance Between Lower of Input's Top Ys, and Bottom Y of Intersection
        int resultHeight = Math.min(topYOne, topYTwo) - resultBottomY;
        
        //If Rectangles Don't Intersect, Width and/or Height Will be Negative or zero
        if (resultWidth <= 0 || resultHeight <= 0)
            return new Rectangle();
        else
            return new Rectangle(resultLeftX, resultBottomY, resultWidth, resultHeight);
    }
    
    // tests

    @Test
    public void overlapAlongBothAxesTest() {
        final Rectangle actual = findRectangularOverlap(
            new Rectangle(1, 1, 6, 3), new Rectangle(5, 2, 3, 6));
        final Rectangle expected = new Rectangle (5, 2, 2, 2);
        assertEquals(expected, actual);
    }

    @Test
    public void oneRectangleInsideAnotherTest() {
        final Rectangle actual = findRectangularOverlap(
            new Rectangle(1, 1, 6, 6), new Rectangle(3, 3, 2, 2));
        final Rectangle expected = new Rectangle(3, 3, 2, 2);
        assertEquals(expected, actual);
    }

    @Test
    public void bothRectanglesTheSameTest() {
        final Rectangle actual = findRectangularOverlap(
            new Rectangle(2, 2, 4, 4), new Rectangle(2, 2, 4, 4));
        final Rectangle expected = new Rectangle(2, 2, 4, 4);
        assertEquals(expected, actual);
    }

    @Test
    public void touchOnHorizontalEdgeTest() {
        final Rectangle actual = findRectangularOverlap(
            new Rectangle(1, 2, 3, 4), new Rectangle(2, 6, 2, 2));
        final Rectangle expected = new Rectangle();
        assertEquals(expected, actual);
    }

    @Test
    public void touchOnVerticalEdgeTest() {
        final Rectangle actual = findRectangularOverlap(
            new Rectangle(1, 2, 3, 4), new Rectangle(4, 3, 2, 2));
        final Rectangle expected = new Rectangle();
        assertEquals(expected, actual);
    }

    @Test
    public void touchAtCornerTest() {
        final Rectangle actual = findRectangularOverlap(
            new Rectangle(1, 1, 2, 2), new Rectangle(3, 3, 2, 2));
        final Rectangle expected = new Rectangle();
        assertEquals(expected, actual);
    }

    @Test
    public void noOverlapTest() {
        final Rectangle actual = findRectangularOverlap(
            new Rectangle(1, 1, 2, 2), new Rectangle(4, 6, 3, 6));
        final Rectangle expected = new Rectangle();
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