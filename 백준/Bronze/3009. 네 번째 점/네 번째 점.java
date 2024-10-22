import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int[] dot1  = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
		st = new StringTokenizer(br.readLine(), " ");
		int[] dot2  = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
		st = new StringTokenizer(br.readLine(), " ");
		int[] dot3  = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
		
		int x;
		int y;
		
		if(dot1[0] == dot2[0]) {
			x = dot3[0];
		}
		else if(dot1[0] == dot3[0]) {
			x = dot2[0];
		}
		else {
			x = dot1[0];
		}
		if(dot1[1] == dot2[1]) {
			y = dot3[1];
		}
		else if(dot1[1] == dot3[1]) {
			y = dot2[1];
		}
		else {
			y = dot1[1];
		}
		bw.write(x + " " + y + "\n");
		bw.flush();
		bw.close();
	}
}