import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String n = br.readLine();
		
		int num = 0;
		
		for(int i = 0; i < n.length(); i++) {
			switch(n.charAt(i)) {
			case 'A', 'B', 'C':
				num += 3;
				break;
			case 'D', 'E', 'F':
				num += 4;
				break;
			case 'G', 'H', 'I':
				num += 5;
				break;
			case 'J', 'K', 'L':
				num += 6;
				break;
			case 'N', 'M', 'O':
				num += 7;
				break;
			case 'P', 'Q', 'R', 'S':
				num += 8;
				break;
			case 'T', 'U', 'V':
				num += 9;
				break;
			case 'W', 'X', 'Y', 'Z':
				num += 10;
				break;
			}
		}
		br.close();
		bw.write(num + "\n");
		bw.flush();
		bw.close();
	}
}