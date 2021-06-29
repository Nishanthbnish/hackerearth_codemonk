class RotateArray {
    /*Function to left rotate arr[] of size n by d*/
    void leftRotate(int arr[], int d, int n)
    {
        for (int i = 0; i < d; i++)
            leftRotatebyOne(arr, n);
    }
 
    void leftRotatebyOne(int arr[], int n)
    {
        int i, temp;
        temp = arr[0];
        for (i = 0; i < n - 1; i++)
            arr[i] = arr[i + 1];
        arr[n-1] = temp;
    }
 
    /* utility function to print an array */
    void printArray(int arr[], int n)
    {
        for (int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }
 
    // Driver program to test above functions
    public static void main(String[] args)
    {
        Scanner s=new Scanner();
        RotateArray rotate = new RotateArray();
        int n=5;
        int arr[] ;
        System.out.println("Enter the number")
        s=sc.nextInt();
        for(int i=0;i<=s;i++)
        {
            s
        }
        rotate.leftRotate(arr, 3, 5);
        rotate.printArray(arr, 5);
    }
}
