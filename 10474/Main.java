
import java.util.Scanner;
import java.util.Arrays;

public class Main{

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int N,Q,i=0,a,b,ind;
		int[] marbles;

		while(++i>0){
			N = in.nextInt();
			Q = in.nextInt();

			if(N == 0 && Q == 0){
				break;
			}
			marbles = new int[N];
			for(int n=0;n<N;n++){
				marbles[n] = in.nextInt();
			}

			Arrays.sort(marbles);

			System.out.println("CASE# "+ Integer.toString(i) +":");
			for(int q=0;q<Q;q++){
				int qr = in.nextInt();

				a=0; b=N-1;
				while(a<b){
						int mid = (a+b)/2;
						if(marbles[mid] >= qr){
							b = mid;
						}
						else {
							a = mid +1 ;
						}
				}

				ind = (a+b)/2;

				if(marbles[ind] == qr){
					System.out.println(Integer.toString(qr) + " found at " + Integer.toString(ind+1));
				}else{
					System.out.println(Integer.toString(qr) + " not found");
				}

				
				
			}

		}

	}


}