import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	static Scanner s = new Scanner(System.in);
	public static void main(String[] args) {
		
		int n = s.nextInt();
		int arr[] = new int[n];
		
		insertNum(arr, n);
		
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		
		insertQueue(arr, n ,pq);
		
		System.out.println(calculator(arr, n, pq));
	}
	
	static void insertNum(int[] arr, int n) {
		for(int i = 0; i < n; i++) {
			arr[i] = s.nextInt();
		}
	}
	
	static void insertQueue(int[] arr, int n, PriorityQueue<Integer> pq) {
		for(int i = 0; i < n; i++) {
			pq.add(arr[i]);
		}
	}
	
	static int calculator(int[] arr, int n, PriorityQueue<Integer> pq) {
		int result = 0;
		
		while(pq.size() > 1) {
			int a = pq.poll();
			int b = pq.poll();
			
			result += a + b;
			pq.add(a + b);
		}
		return result;
	}

}
