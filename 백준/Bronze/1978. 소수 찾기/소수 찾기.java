import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int pcount = 0;
		
		for(int i = 0; i < n; i++) {
			int num = Integer.parseInt(st.nextToken());
			int count = 0;
			
			for(int j = 2; j <= num; j++) {
				if(num % j == 0) {
					count++;
				}
			}
			if(count == 1) {
				pcount++;
			}
		}
		br.close();
		bw.write(pcount + "\n");
		bw.flush();
		bw.close();
	}
}