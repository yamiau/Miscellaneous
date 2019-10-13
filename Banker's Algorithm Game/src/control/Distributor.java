package control;

import java.security.SecureRandom;

public class Distributor {

	private String[] processes;
	private String[] alphabet = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
	private int resources;
	private int[] max_res;
	private int[] available_res;
	private int[][] allocated;
	private boolean safe;
	private SecureRandom random = new SecureRandom();
	
	public Distributor() {
		processes = new String[(random.nextInt(9) + 2)];
		
		for (int i = 0; i < processes.length; i++) {
			processes[i] = alphabet[i];
		}
		
		resources = (random.nextInt(4) + 4);
		max_res = new int[resources];
		allocated =  new int[resources][processes.length];
		
		for (int i = 0; i < resources; i++) {
			max_res[i] = (random.nextInt(6) + 1);
		}	
	}
}
