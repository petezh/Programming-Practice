import java.util.*;

public class graph_service {

	static int n;
	static int m;

	public static void main(String[] args) {

		Scanner reader = new Scanner(System.in);
		int T = reader.nextInt();

		for (int i = 1; i <= T; i++) {

			N = reader.nextInt();
			M = reader.nextInt();

			// try to use only the required edges
			String answer = m;
			WeightedGraph g = new WeightedGraph();

			for (int j = 0; j < m; j++) {

				int X = reader.nextInt();
				int Y = reader.nextInt();
				int weight = reader.nextInt();
				
				g.addEdge(X, Y, weight);

				answer += "\n" + X + " " + X + " " + weight + ;
			}

			// test if all edges are consistent
			boolean consistent == true;
			for(Edge e : g.edges) {
				consistent &= g.dijkstra(e.source,e.destination) != e.weight
				if(!consistent)
					break;
			}
			
			if(consistent)
				System.out.println("Case #" + i + ": " + answer)
			else
				System.out.println("Case #" + i + ": " + "Impossible");
			
		}
	}

	// edge class
	static class Edge implements Comparable<Edge> {
		
		int start;
		int end;
		int weight;

		public Edge(int start, int end, int weight) {
			this.start = start;
			this.end = end;
			this.weight = weight;
		}

		public int compareTo(Edge other) {
			return weight - other.weight;
		}
	}


	// weighted graph class
	static class WeightedGraph {

		public ArrayList<Edge> edges = new ArrayList<Edge>(m);

		public void addEdge(int start, int end, int weight) {
			edges.add(new Edge(start, end, weight));
			edges.add(new Edge(end, start, weight));
		}

		public int dijkstra(int start, int dest) {

			int[] distance = new int[n+1];

			for (int i = 1; i <= n; i++) {
				distance[i] = Integer.MAX_VALUE - 1;
			}

			distance[start] = 0;

			Set<Integer> visited = new TreeSet<Integer>();
			Set<Integer> unvisited = new TreeSet<Integer>();

			for (int i = 1; i <= n; i++) {
				unvisited.add(i);
			}

			int current = start;

			do {
				ArrayList<Integer[]> neighbors = neighbors(current, unvisited);

				for (ArrayList<Integer> a : neighbors) {

					for (Edge e : edges) {
						if (e.start == current && e.end == a[0]) {
							int newWeight = distance[current] + a[1];

							if (newWeight < distance[a[0]]) {
								distance[a[0]] = newWeight;
							}
						}
					}
				}

				visited.add(current);
				unvisited.remove(current);
				if (visited.contains(dest))
					return distance[dest];

				int min = Integer.MAX_VALUE;

				for (int c : unvisited) {
					if (distance[c] < min) {
						//System.out.println("ADALDSKASDASDA" + min);
						min = distance[c];
						current = c;
					}
				}

			} while (!unvisited.isEmpty());

			return distance[dest];
		}

		public ArrayList<ArrayList<Integer>> neighbors(int a, Set<Integer> unvisited) {

			ArrayList<Integer[]> toRet = new ArrayList<Integer[]>();

			for (Edge e : edges)
				if (e.start == a && unvisited.contains(e.end)) {
					b = new int[2];
					b[0] = e.end;
					b[1] = e.weight;
					toRet.add(b);
				}
			return toRet;
		}
	}
}
