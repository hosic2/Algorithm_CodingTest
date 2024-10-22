import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		double r = Double.parseDouble(br.readLine());
		br.close();
		
		bw.write(r * r * Math.PI + "\n");
		bw.write(r * r * 2 + "\n");
		bw.flush();
		bw.close();
	}
}