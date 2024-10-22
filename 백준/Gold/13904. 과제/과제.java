import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	static Scanner s = new Scanner(System.in);
	
	public static void main(String[] args) {
		int n = s.nextInt();
		
		int arr[][] = new int[n][2];
		
		insertNum(arr, n);
		
		Arrays.sort(arr, new Comparator<int[]>() {
			public int compare(int[] o1, int[] o2) {
				return Integer.compare(o2[1], o1[1]);
			}
		});
		
		System.out.println(calculator(arr, n));
	}
	
	static void insertNum(int arr[][], int n) {
		for(int i = 0; i < n; i++) {
			arr[i][0] = s.nextInt();
			arr[i][1] = s.nextInt();
		}
	}
	
	static int calculator(int arr[][], int n) {
		int result = 0;
		int [] date = new int[1001];
		
		for(int i = 0; i < n; i++) {
			for(int j = arr[i][0]; j > 0; j--) {
				if(date[j] == 0) {
					date[j] = arr[i][1];
					break;
				}
			}
		}
		
		for(int i = 0; i < date.length; i++) {
			result += date[i];
		}
		return result;
	}

}
