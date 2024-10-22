import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		int[] kg = new int[n];
		int[] cm = new int[n];
		
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			kg[i] = Integer.parseInt(st.nextToken());
			cm[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = 0; i < n; i++) {
			int rank = 1;
			for(int j = 0; j < n; j++) {
				if(i == j) {
					continue;
				}
				if(kg[i] < kg[j] && cm[i] < cm[j]) {
					rank++;
				}
			}
			bw.write(rank + " ");
		}
		bw.flush();
		bw.close();
	}
}