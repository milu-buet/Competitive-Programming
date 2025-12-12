
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);

		int N,Q,query;
		String h="",l="";

		N = in.nextInt();
		int[] heights = new int[N+5];
		for(int i=0;i<N;i++){
			heights[i] = in.nextInt();
		}

		Q = in.nextInt();
		for(int i=0;i<Q;i++){
			query = in.nextInt();
			int a = 0, b=N-1;
			while(a<b){
					int mid = (a+b)/2;
					if(heights[mid] == query){
						break;
					}
					else if(heights[mid] > query){
						b = mid - 1;
					}
					else {
						a = mid +1 ;
					}
			}

			int ind = (a+b)/2;

			if(heights[ind] == query){

				while(ind < N && heights[ind++] == query){;}
				if(ind == N){ind = N-1;}
				else ind = ind - 2;

				if(ind < N - 1){
					h = Integer.toString(heights[ind + 1]);
				}else{
					h = "X";
				}
				
				while(ind > -1 && heights[ind--] == query){;}
				if(ind == -1){ind = 0;}
				else ind = ind + 2;
				if(ind>=1){
					l = Integer.toString(heights[ind - 1]);
				}else{
					l = "X";
				}
			}

			else if(query < heights[ind]){
				h = Integer.toString(heights[ind]);
				if(ind>=1){
					l = Integer.toString(heights[ind - 1]);
				}else{
					l = "X";
				}
			}

			else if(query > heights[ind]){
				l = Integer.toString(heights[ind]);
				if(ind < N -1){
					h = Integer.toString(heights[ind + 1]);
				}else{
					h = "X";
				}
			}

			System.out.println(l+" "+h);

		}

	}


}