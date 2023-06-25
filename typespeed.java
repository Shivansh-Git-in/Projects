import java.time.LocalTime;
import java.util.*;
import java.util.concurrent.TimeUnit;
public class typespeed {

    static String[] words={"apple","mango","hello","the","man","children","walk","weather","mountain","philanthropist"};
    public static void main(String[] args) throws InterruptedException{
        System.out.println("3");
        TimeUnit.SECONDS.sleep(1);
        System.out.println("2");
        TimeUnit.SECONDS.sleep(1);
        System.out.println("1");
        TimeUnit.SECONDS.sleep(1);

        Random randm = new Random();
        for(int i=0;i<10;i++){
        System.out.print(words[randm.nextInt(9)]+ " ");
        }
        System.out.println();

        double start = LocalTime.now().toNanoOfDay();
        Scanner sc=new Scanner(System.in);
        String typedwords=sc.nextLine();
        double end = LocalTime.now().toNanoOfDay();
        double timeelapsed=end-start;
        double seconds = timeelapsed/1000000000.0;
        int WPM = (int)((((double)typedwords.length()/5)/seconds)*60);
        
        System.out.println("Your words per minute is: "+WPM+" !");
    }
}
