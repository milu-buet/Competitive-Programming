
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		
		//System.out.println("Hello");

		Scanner in = new Scanner(System.in);
		int t = in.nextInt();

		for(int i=0; i<t; i++){

			int n = in.nextInt();
			int l=100,h=-1;
			for(int j=0;j<n;j++){
				int x = in.nextInt();

				if(h<x) h=x;
				if(l>x) l=x;
			}

			System.out.println(2*(h-l));
		}

	}


}