import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			int distance = y - x;
			int max = (int)Math.sqrt(distance);
			
			if(max == Math.sqrt(distance)) {
				bw.write(max * 2 - 1 + "\n");
			}
			else if(distance <= max * max + max) {
				bw.write(max * 2 + "\n");
			}
			else {
				bw.write(max * 2 + 1 + "\n");
			}
		}
		br.close();
		bw.flush();
		bw.close();
	}
}