import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int m = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());
		int sum = 0;
		int min = 10001;
		boolean isPrimeNum;		
		for(int i = m; i <= n; i++) {
			
			if(i > 1) {
				isPrimeNum = true;
				for(int j = 2; j < i; j++) {
					if(i % j == 0) {
						isPrimeNum = false;
						break;
					}
				}
				if(isPrimeNum) {
					sum += i;
					if(min > i) {
						min = i;
					}
				}
			}
		}
		if(sum != 0) {
			bw.write(sum + "\n" + min);
		}
		else {
			bw.write("-1");
		}
		br.close();
		bw.flush();
		bw.close();
	}
}