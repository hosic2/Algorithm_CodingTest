import java.util.Scanner;

public class Main {
	public static StringBuilder sb = new StringBuilder();
	public static int count = 0;
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int n = s.nextInt();
		s.close();
		moveHanoi(1, 2, 3, n);
		sb.insert(0, count + "\n");
		System.out.print(sb);
	}

	public static void moveHanoi(int start, int move, int end, int num) {
		count ++;
		if(num == 1) {
			sb.append(start + " " + end + "\n");
			return;
		}
		moveHanoi(start, end, move, num-1);
		sb.append(start + " " + end + "\n");
		moveHanoi(move, start, end, num-1);
	}
}