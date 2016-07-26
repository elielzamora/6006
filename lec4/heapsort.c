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
        int cap;
} Heap;
typedeft struct{
        //todo
}
typedef Heap PriorityQueue;

int heapify (Heap heap, int i);
int makeHeap(int * array, int size);
int getParent(Heap heap, int i);
int getLeft(Heap heap int i);
int getRight(Heap heap, int i);
Array heapsort(Heap heap);

int main (int argc, char ** argv){



}
