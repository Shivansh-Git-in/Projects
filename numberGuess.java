import java.util.*;
public class numberGuess {
    public static void main(String[] args){
        Random ran = new Random();
        Scanner sc=new Scanner(System.in);

        int count=0;

        int randomNumber = ran.nextInt(100)+1;
        while(true){
            System.out.println("Guess a number (0-100): ");
            int guess=sc.nextInt();
            count++;
            if(randomNumber==guess){
                System.out.println("Your guess was right!");
                System.out.println("You took "+count+"! chances to answer correctly");
                break;
            }else if(randomNumber>guess){
                System.out.println("The number is bigger than your guess.");
            }else{
                System.out.println("The number is smaller than your guess.");
        }
        }
    }
}
