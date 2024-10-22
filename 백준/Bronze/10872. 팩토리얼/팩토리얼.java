import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int multiplication = 1;
		
		for(int i = 1; i <= n; i++) {
			multiplication *= i;
		}
		bw.write(multiplication + "\n");
		bw.flush();
		bw.close();
	}
}