import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int count=0;
	    int max=0;
	    System.out.println("Enter size of array A:");
	    int n=sc.nextInt();
	    int[] A=new int[n];
	    System.out.println("Note:Array should consists of binary values only.");
	    System.out.println("Enter elements of array A:");
        for(int i=0;i<n;i++)
        {
            A[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            if (A[i]==1)
            {
                count+=1;
            }
           else
           {
                if (count>max)
            {
                max=count;
            }
                count=0;
            }
        }
        System.out.println("Length of longest consecutive 1's :"+max);
	    }
}