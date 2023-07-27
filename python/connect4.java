import java.util.Scanner;

public class Connect4 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		char[][] grid = new char[6][7];
		
		//initialize array
		for (int row = 0; row < grid.length; row++){
			for (int col = 0; col < grid[0].length; col++){
				grid[row][col] = ' ';
			}
		}
		
		int turn = 1;
		char player = 'R';
		boolean winner = false;		
		
		//play a turn
		while (winner == false && turn <= 42){
			boolean validPlay;
			int play;
			do {
				display(grid);
				
				System.out.print("Player " + player + ", choose a column: ");
				play = in.nextInt();
				
				//validate play
				validPlay = validate(play,grid);
				
			}while (validPlay == false);
			
			//drop the checker
			for (int row = grid.length-1; row >= 0; row--){
				if(grid[row][play] == ' '){
					grid[row][play] = player;
					break;
				}
			}
			
			//determine if there is a winner
			winner = isWinner(player,grid);
			
			//switch players
			if (player == 'R'){
				player = 'B';
			}else{
				player = 'R';
			}
			
			turn++;			
		}
		display(grid);
		
		if (winner){
			if (player=='R'){
				System.out.println("Black won");
			}else{
				System.out.println("Red won");
			}
		}else{
			System.out.println("Tie game");
		}
		
	}
	
	public static void display(char[][] grid){
		System.out.println(" 0 1 2 3 4 5 6");
		System.out.println("---------------");
		for (int row = 0; row < grid.length; row++){
			System.out.print("|");
			for (int col = 0; col < grid[0].length; col++){
				System.out.print(grid[row][col]);
				System.out.print("|");
			}
			System.out.println();
			System.out.println("---------------");
		}
		System.out.println(" 0 1 2 3 4 5 6");
		System.out.println();
	}
	
	public static boolean validate(int column, char[][] grid){
		//valid column?
		if (column < 0 || column > grid[0].length){
			return false;
		}
		
		//full column?
		if (grid[0][column] != ' '){
			return false;
		}
		
		return true;
	}