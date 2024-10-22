import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		br.close();
		
		int line = 0;
		int count = 0;
		
		while(count < n) {
			line++;
			count = line * (line + 1) / 2;
		}
		
		if(line%2 == 0) {
			int son = line - (count - n);
			int mother = 1 + count - n;
			bw.write(son + "/" + mother + "\n");
		}else {
			int son = 1 + count - n;
			int mother = line - (count - n);
			bw.write(son + "/" + mother + "\n");
		}
		bw.flush();
		bw.close();
	}
}