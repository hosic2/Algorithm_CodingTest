import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			int z = Integer.parseInt(st.nextToken());
			
			if(x == 0 && y == 0 && z == 0) {
				break;
			}
			
			if((x * x) == (y * y) + (z * z)) {
				bw.write("right" + "\n");
			}
			else if((y * y) == (x * x) + (z * z)) {
				bw.write("right" + "\n");
			}
			else if((z * z) == (x * x) + (y * y)) {
				bw.write("right" + "\n");
			}
			else {
				bw.write("wrong" + "\n");
			}	
		}
		bw.flush();
		bw.close();
	}
}