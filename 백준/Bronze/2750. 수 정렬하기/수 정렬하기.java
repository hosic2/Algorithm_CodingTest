import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		Integer n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		
		for(int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		br.close();
		
		Arrays.sort(arr);
		
		for(int val : arr) {
			bw.write(val + "\n");
		}
		bw.flush();
		bw.close();
	}

}