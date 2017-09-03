
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		String[] urls = new String[10];
		int[] rank = new int[10];
		int[] toprank = new int[10];
		int toprank_index;
		int T = in.nextInt();

		for(int i=0;i<T;i++){
			toprank_index=0;
			toprank[0] = 0;
			for(int j=0;j<10;j++){
				urls[j] = in.next();
				rank[j] = in.nextInt();

				//System.out.println(toprank[0]);
				//System.out.println(rank[j]);
				//System.out.println(">>");

				if(rank[toprank[0]] == rank[j]){
					toprank[toprank_index++] = j;
				}
				else if(rank[toprank[0]] < rank[j]){
					toprank_index=0;
					toprank[toprank_index++] = j;
				}

				//System.out.println(toprank[0]);
				//System.out.println(rank[j]);
				//System.out.println(">>1");


			}	
			//System.out.println(urls[2]);
			
			System.out.println("Case #"+ String.valueOf(i+1) +":");
			for(int j=0;j<toprank_index;j++){
				System.out.println(urls[toprank[j]]);	
			}

		}

	
		 
	}


}