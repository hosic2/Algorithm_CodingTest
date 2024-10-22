import java.io.*;

public class Main {
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				star(i,j);
			}
			sb.append("\n");
		}
		bw.write(sb + "\n");
		bw.flush();
		bw.close();
		
	}
	public static void star(int x, int y) {
		while(true) {
			if(x == 0) {
				break;
			}
			if(x % 3 == 1 && y % 3 == 1) {
				sb.append(" ");
				return;
			}
			x /= 3;
			y /= 3;
		}
		sb.append("*");
	}
}