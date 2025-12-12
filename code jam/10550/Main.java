
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);

		 while(true){

			int pos = in.nextInt();
			int a = in.nextInt();
			int b = in.nextInt();
			int c = in.nextInt();
			
			if(pos==0 && a==0 && b==0 && c==0){
				break;
			}

			int ans = 720 + 360;

			if(a>=pos){
				ans += (40-a+pos)*9;
			}else{
				ans += (pos-a)*9;
			}

			//System.out.println(ans);

			if(b>=a){
				ans += (b-a)*9;
			}else{
				ans += (40-a+b)*9;
			}
			//System.out.println(ans);

			if(c>=b){
				ans += (40-c+b)*9;
			}else{
				ans += (b-c)*9;
			}


			System.out.println(ans);
		 }

	}


}