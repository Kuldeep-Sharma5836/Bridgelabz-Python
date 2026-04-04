import java.util.Scanner;

public class CalculatePrice {
     public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter unit price:");
        int unitPrice = sc.nextInt();
        System.out.println("Enter quantity:");
        int quantity = sc.nextInt();
        int totalPrice = unitPrice * quantity;
        System.out.println("Total price is " + totalPrice);
    }
    
}
