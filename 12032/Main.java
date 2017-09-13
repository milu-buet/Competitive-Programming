
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int T,n,ans,k,cap;
		int[] rungs = new int[100001];

		T = in.nextInt();
		for(int i=0;i<T;i++){
			n = in.nextInt();
			rungs[0] = 0;
			k = 0;
			cap = 0;
			for(int j=1;j<=n;j++){
				rungs[j] = in.nextInt();
				int diff = rungs[j] - rungs[j-1];

				if(cap == diff){
					 cap--;
				}
				else{

					if(k<diff){
						k = diff;
						cap = k-1;
					}
					else if(cap < diff){
						 k++;
						 cap = k;
					}

				}

			}

			System.out.println("Case " + (i+1) + ": "+ k);
		}
	}
}