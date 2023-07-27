import java.util.*;
public class solution{
    public static void main(String args[]){
        Scanner s = new Scanner(System.in);
        int n=s.nextInt();
        for(int i=0;i<n;i++){
            int k=s.nextInt();
            int ar[] = new int[k];
            for(int j=0;j<k;j++){
                ar[j]=s.nextInt();
                int c=check(ar);
            }
            System.out.println("");
        }
    }
    static int check(int a[]){
        int b[]=new int[a.length];
        b=a;
        Arrays.sort(a);
        if(b==a){
            System.out.print(1);
            return 0;
        }
        int r=0;
        l1:for(int i=1;i<b.length;i++){
            if(b[i-1]>b[i]){
                r=i;
                break l1;
            }
        }
        int k=0;
        int c[] = new int[a.length];
        for(int i=r;i<a.length;i++){
            c[i-r]=b[i];
            k=i-r;
        }
        for(int i=0;i<r;i++){
            k++;
            c[k]=b[i];
        }
        if(c==a){
            System.out.print(1);
        }
        else{
            System.out.print(0);
        }
        return 0;
    }
}