import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int count = n;
		int j = 0;
		
		for(int i = 0; i < n; i++) {
			String word = br.readLine();
			boolean[] check = new boolean[26];
			
			for(j = 1; j < word.length(); j++) {
				if(word.charAt(j-1) != word.charAt(j)) {
					if(check[word.charAt(j)-97] == true) {
						count--;
						break;
					}
					else{
						check[word.charAt(j-1)-97] = true;
					}
				}
			}
		}
		br.close();
		bw.write(count + "\n");
		bw.flush();
		bw.close();
	}
}