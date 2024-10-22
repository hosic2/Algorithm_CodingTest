import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String word = br.readLine();
		int[] arr = new int[26];
		
		for(int i = 0; i < word.length(); i++) {
			
			if('A' <= word.charAt(i) && word.charAt(i) <= 'Z') {
				arr[word.charAt(i) - 'A']++;
			}
			else {
				arr[word.charAt(i) - 'a']++;
			}
		}
		int max = -1;
		char ch = '?';
		
		for(int i = 0; i < arr.length; i++) {
			
			if(arr[i] > max) {
				max = arr[i];
				ch = (char) (i+'A');
			}
			else if(arr[i] == max) {
				ch = '?';
			}
		}
		br.close();
		bw.write(ch);
		bw.flush();
		bw.close();
	}
}