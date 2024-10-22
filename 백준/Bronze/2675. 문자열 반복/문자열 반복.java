import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int reps = Integer.parseInt(st.nextToken());
			String word = st.nextToken();
			
			for(int j = 0; j < word.length(); j++) {
				for(int k = 0; k < reps; k++) {
					sb.append(word.charAt(j));
				}
			}
			sb.append("\n");
		}
		br.close();
		bw.write(String.valueOf(sb));
		bw.flush();
		bw.close();
	}
}