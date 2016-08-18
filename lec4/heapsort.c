/**
        Eliel Zamora
        6.006 Intro to Algorithms
        Header describing:
                - Priority Queue ADT
                - Heap functions
                - Heapsort
*/

typedef struct {
        int * heap
        int size;
} Heap;
typedeft struct{
        int * array
        int size;
} Array;
typedef Heap PriorityQueue;

int heapify (Heap h, int i);
int makeHeap(int * array, int size);
int parent(int i);
int left(int i);
int right(int i);
int getParent(Heap h, int i);
int getLeft(Heap h int i);
int getRight(Heap h, int i);
int assertMaxHeapProperty(Heap h);
int assertSorted(Array a);
Array heapsort(Heap heap);

int main (int argc, char ** argv){



}

/** Definitions */

int parent(int i){
        return (i/2) -1
}
int left(int i){
	return (i*2) -1
}
int right(int i){
        return (i*2)
}
