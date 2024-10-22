import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		String a = br.readLine();
		int sum = 0;
		
		for(int i = 0; i < n; i++) {
			sum += a.charAt(i)-48; 
		}
		br.close();
		bw.write(sum + "\n");
		bw.flush();
		bw.close();
	}
}