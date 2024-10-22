import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		System.out.println(sequence(Integer.parseInt(br.readLine())));
	}
	
	public static int sequence(int num) {
		int count = 0;
		if(num < 100){
			return num;
		}
		else {
			count = 99;
		}
		for(int i = 100; i <= num; i++) {
			int hundread = i / 100;
			int ten = (i / 10) % 10;
			int one = i % 10;
			
			if((ten * 2) ==(hundread + one)) {
				count++;
			}
		}
		return count;
		}
}