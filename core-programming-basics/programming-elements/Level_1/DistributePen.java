import java.util.*;
public class DistributePen {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the total number of pens and total number of students:");
        int totalPens = sc.nextInt();
        int totalStudents = sc.nextInt();
        int pensPerStudent = totalPens / totalStudents;
        int remainingPens = totalPens % totalStudents;  
        System.out.println("Each student gets " + pensPerStudent + " pens.");
        System.out.println("Remaining pens: " + remainingPens);
    }
}