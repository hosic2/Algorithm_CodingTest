import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int num = s.nextInt();
		int[][] arr = new int[num][2];
		int count = 0;
		
		for(int i = 0; i < num; i++) {
			for(int j = 0; j < 2; j++) {
				arr[i][j] = s.nextInt();
			}
		}
		
		Arrays.sort(arr, (v1, v2) -> {
            if(v1[1] == v2[1]) { 
                return v1[0] - v2[0]; //0번 인덱스 기준으로 오름차순
            }
            return v1[1] - v2[1]; //1번 인덱스 기준으로 오름차순
        });
		
		int prev_end = 0;
		
		for(int i = 0; i < num; i++) {
			if(prev_end <= arr[i][0]) {
				prev_end = arr[i][1];
				count++;
			}
		}
		System.out.println(count);
	}
}