import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[] arr = new int[26];
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = -1;
		}
		
		String a = br.readLine();
		
		for(int i = 0; i < a.length(); i++) {
			char ch = a.charAt(i);
			
			if(arr[ch-'a'] == -1) { //ch가 갖고 있는 문자 인코딩값(아스키코드값)에 'a'또는 97을 뺀다.
				arr[ch-'a'] = i;
			}
		}
		for(int num : arr) {
			bw.write(num+ " ");
		}
		br.close();
		bw.flush();
		bw.close();
	}

}