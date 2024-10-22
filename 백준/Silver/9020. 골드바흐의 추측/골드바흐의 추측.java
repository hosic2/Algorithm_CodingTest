import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);

		int input = s.nextInt();
		for (int j = 0; j < input; j++) {
			int test = s.nextInt();
			for (int a = test / 2, b = test / 2;; a++, b--) {
				if (check(a) && check(b)) {
					System.out.println(b + " " + a);
					break;
				}
			}
		}
	}

	public static boolean check(int n) {
		for (int i = 2; i <= n / 2; i++) {
			if (n % i == 0)
				return false;
		}
		return true;
	}
}
