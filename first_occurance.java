// we are finding the first and last index of the element given
import java.util.*;
class Main 
{
    public static void main(String[] args) 
    {
        int first_index=-1;
        int last_index=-1;
        System.out.println("Enter size of the array:");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        System.out.println("Enter target element: ");
        int target=sc.nextInt();
        System.out.println("Enter array elements:");
        int[] a=new int[n];
        
        for(int i=0;i<n;i++)
        {
            a[i]=sc.nextInt();
        }
       
        for(int i=0;i<n;i++)
        {
            if (a[i]==target)
            {
                first_index=i;
                break;
            }
        }
        for(int i=n-1;i>=0;i--)
        {
            if (a[i]==target)
            {
                last_index=i;
                break;
            }
        }
        System.out.println("The first occurance of the element "+target+" is "+first_index);
        System.out.println("The last occurance of the element "+target+" is "+last_index);
      
        
    }

}


