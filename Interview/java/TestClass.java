

/*
1. Thread Safety Discussion
  * Stack is threadsafe but Queue/ArrayDequeu is not.
  * Thread safety adds some overhead
  *

 2. Avoid boxing variable if possible.
  * int is primitive not boxed. Integer is primitive boxed.


*/

import java.util.*;
import java.util.stream.Collectors;

class Node {
	int x;
	int y;
	Node(int x, int y) {
		this.x = x;
		this.y = y;
	}

	int getX() {return x;}
	int getY() {return y;}
	public String toString() {
		return String.format("(%d, %d)", x, y);
	}
}


public class TestClass {

	private static void print(Object o){
		System.out.println(o);
	}


   private static void testDeque() {
   	    print("\nTesting Deque:");

   		Deque<Integer> q = new ArrayDeque<>();
   		q.addLast(5);
   		q.addLast(7);
   		q.addLast(1);
   		print(q);
   		q.addFirst(2);
   		print(q);
   		q.removeFirst();
   		print(q);
   		q.removeLast();
   		print(q);
   		print(q.peekLast());
   }

   private static void testSet() {

   	  print("\nTesting TreeSet:");

   		TreeSet<Integer> s = new TreeSet<>(Comparator.reverseOrder());
   		s.add(5);
   		s.add(1);
   		s.add(2);
   		s.add(7);
   		print(s);
   		s.remove(1);
   		print(s);
   		s.add(8);
   		print(s);
   		print(s.contains(5));

   		// TreeSet spe3cific methods
   		print(s.floor(3)); 
   		print(s.ceiling(3));
   		print(s.first());
   		print(s.pollFirst());


   		//TreeSet<Node> s2 = new TreeSet<>(Comparator.comparingInt(Node::getX));
   		TreeSet<Node> s2 = new TreeSet<>(Comparator.comparingInt((Node n) -> n.x));
   		s2.add(new Node(1,2));
   		s2.add(new Node(3,2));
   		print(s2);


   		print("\nTesting Linked LinkedHashSet:");
   		LinkedHashSet<Integer> a = new LinkedHashSet<>();
   		a.add(5);
   		a.add(1);
   		a.add(2);
   		a.add(7);
   		print(a);
   		a.remove(1);
   		print(a);
   		a.add(8);
   		print(a);
   		print(a.contains(5));

   		// LinkedHashSet spe3cific methods
   		// print(a.first());
   		// print(a.last());
   		// print(a.floor(6));

   }

   private static void testMap() {

   		TreeMap<Integer, Integer> s = new TreeMap<>();
   		s.put(10, 100);
   		s.put(3, 2);
   		s.put(2, 200);
   		s.put(4, 7);
   		print(s); 

   		print(s.floorKey(5));
   		print(s.ceilingKey(5));
   		print(s.firstKey());
   		print(s.lastKey());



   }

   private static void testSort() {

   		int[] a = new int[]{5,2,1,3,4,56,2};
   		Arrays.sort(a);
   		for (int a1: a) print(a1);
   		print("");

		Integer[] a2 = new Integer[]{5,2,1,3,4,56,2};
   		Arrays.sort(a2, Comparator.reverseOrder());
   		for (int a1: a2) print(a1);
   		print("");


   		Node[] a3 = new Node[]{new Node(1,2), new Node(5,3)};
   		//Arrays.sort(a3, Comparator.comparingInt(Node::getX));
   		Arrays.sort(a3, (c, d) -> c.getX() - d.getX());
   		for (Node a1: a3) print(a1);
   		print("");

   		List<Node> a4 = new ArrayList<>();
   		a4.add(new Node(1,2));
   		a4.add(new Node(3,2));
   		//a4.sort(Comparator.comparingInt(Node::getX));
   		a4.sort((c, d) -> c.getX() - d.getX());
   		for (Node a1: a4) print(a1);

   }

   private static void testPriority() {

   		PriorityQueue<Integer> q = new PriorityQueue<>();
   		q.add(3);
   		q.add(1);
   		q.add(5);
   		q.add(3);
   		print(q);
   		print(q.peek());
   		print(q.remove());
   		print(q);
   }

   private static void testStream() {
   		List<Integer> a = new ArrayList<>();
   		a.add(2);
   		a.add(1);
   		a.add(3);
   		a.add(5);
   		print(a);

   		Iterator<Integer> it = a.iterator();
   		while(it.hasNext()) {
   			print(it.next());
   		}

   		print(a.stream().filter(x -> x > 1).collect(Collectors.toList()));
   		print(a.stream().filter(x -> x > 1).collect(Collectors.toSet()));
   		print(a.stream().filter(x -> x > 1).map(x -> x-1).collect(Collectors.toMap(x -> x, x -> x*x*x)));

   }

	public static void main(String[] args) {
		System.out.println("Hello");
		//testDeque();
		//testSet();
		//testSort();
		//testMap();
		//testPriority();
		testStream();
	}
}