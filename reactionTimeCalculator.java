import java.util.Scanner;
public class reactionTimeCalculator {
    public static void main(String[] args) throws InterruptedException{
        System.out.println("3");
        Thread.sleep(1000);
        System.out.println("2");
        Thread.sleep(1000);
        System.out.println("1");
        Thread.sleep(1000);

        System.out.println("Go!!!");

        long start = System.currentTimeMillis();        

        Scanner s=new Scanner(System.in);
        s.next();

        long stop = System.currentTimeMillis();
        
        long reactionTime = stop - start;
        System.out.println("Your reaction time was "+reactionTime+" ms.");
    
        
        
    }
}
