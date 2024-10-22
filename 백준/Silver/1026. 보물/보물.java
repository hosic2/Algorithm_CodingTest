import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	static Scanner s = new Scanner(System.in);
	static int num = s.nextInt();
	static Integer [] arr1 = new Integer[num];
	static Integer [] arr2 = new Integer[num];
	public static void main(String[] args) {
		iterInput(num, arr1);
		iterInput(num, arr2);

		Arrays.sort(arr1);
		Arrays.sort(arr2, Collections.reverseOrder());
	
		System.out.println(mixArr(num));
	}

	static void iterInput(int num, Integer[] arr) {
		for(int i = 0; i < num; i++) {
			arr[i] = s.nextInt();
		}
	}
	
	static int mixArr(int num) {
		int result = 0;
		for(int i = 0; i < num; i++) {
			result += arr1[i] * arr2[i];
		}
		return result;
	}
}
