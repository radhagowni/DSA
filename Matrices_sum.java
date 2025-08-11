import java.util.*;
class Main 
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter numbers of rows and columns of matrix A");
        int row1=sc.nextInt();
        int col1=sc.nextInt();
        int[][] A=new int[row1][col1];
        System.out.println("Enter elements of matrix A:");
        for(int i=0;i<row1;i++)
        {
            for(int j=0;j<col1;j++)
            {
                 A[i][j]=sc.nextInt();
            }
        }
        System.out.println("Enter numbers of rows and columns of matrix B");
        int row2=sc.nextInt();
        int col2=sc.nextInt();
        int[][] B=new int[row2][col2];
        System.out.println("Enter elements of matrix B:");
        for(int i=0;i<row2;i++)
        {
            for(int j=0;j<col2;j++)
            {
                 B[i][j]=sc.nextInt();
            }
        }
        System.out.println("Sum of two matrices A and B:");
        for(int i=0;i<row1;i++)
        {
            for(int j=0;j<col1;j++)
            {
                A[i][j]=A[i][j]+B[i][j];
                System.out.print(A[i][j]+" ");
            }
            System.out.print("\n");
        }
    }

}
