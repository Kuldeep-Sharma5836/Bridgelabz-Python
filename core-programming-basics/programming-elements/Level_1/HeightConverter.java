import java.util.*;
public class HeightConverter {
    public static void main(String[] args) {
        System.out.println("Enter your height in centimeters:");
        Scanner sc=new Scanner(System.in);
        int heightInCM= sc.nextInt();
        double heightInInches = heightInCM / 2.54;
        double heightInFeet = heightInInches / 12;
        System.out.println("Your Height in cm is "+heightInCM+" while in feet is "+heightInFeet+" and inches is "+heightInInches);
    }
}