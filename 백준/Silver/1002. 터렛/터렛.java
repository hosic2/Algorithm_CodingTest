import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int r1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int r2 = Integer.parseInt(st.nextToken());
			
			bw.write(Point(x1, y1, r1, x2, y2, r2)+ "\n");
		}
		br.close();
		bw.flush();
		bw.close();
	}

	public static int Point(int x1, int y1, int r1, int x2, int y2, int r2) {
		int distance = (int)(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
		
		if(x1 == x2 && y1 == y2 && r1 == r2) {
			return -1;
		}
		
		else if(distance > Math.pow(r1 + r2, 2)) {
			return 0;
		}
		
		else if(distance < Math.pow(r2 - r1, 2)) {
			return 0;
		}
		else if(distance == Math.pow(r2 - r1, 2)) {
			return 1;
		}
		else if (distance == Math.pow(r1 + r2, 2)) {
			return 1;
		}
		else {
			return 2;
		}
	}
}