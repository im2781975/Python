/***/
class CircularQueue:     
    def __init__(self, size):       self.size = size        
        self.queue = [None] * size
        self.head = self.tail = -1
    def enqueue(self, item):         if ((self.tail + 1) % self.size == self.head):             print("Queue is Full")  elif (self.head == -1):
            self.head = 0       
            self.tail = 0   
            self.queue[self.tail] = item         
        else:             
            self.tail = (self.tail + 1) % self.size
            self.queue[self.tail] = item          
    def dequeue(self):        
        if (self.head == -1):       print("Queue is Empty")         
        elif (self.head == self.tail):             temp = self.queue[self.head]             
            self.head = -1  
            self.tail = -1  
            return temp 
        else:             
            temp = self.queue[self.head]        
            self.head = (self.head + 1) % self.size
            return temp    
    def display(self):        
        if(self.head == -1):        print("No element in the Queue")         
        elif (self.tail >= self.head):             
            for i in range(self.head, self.tail + 1):                 print(self.queue[i], end=" ")         
        else:             
            for i in range(self.head, self.size):  print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):       print(self.queue[i], end=" ")  
queue = CircularQueue(5) 
queue.enqueue(1) 
queue.enqueue(2)
queue.enqueue(3)
queue.display() 
print("\n") 
print(queue.dequeue())
queue.display() 
/***/
class Queue: 
    def __init__(self): 
        self.queue = [] 
        def enqueue(self, item): self.queue.append(item)
        def dequeue(self): 
            if len(self.queue) == 0:
                return None         
            else:             
                return self.queue.pop(0)          
        def is_empty(self):         return len(self.queue) == 0  
queue = Queue() 
queue.enqueue(1)
print(queue.dequeue()) 
/***/
#include <iostream> 
#include <queue>  
using namespace std;
int main() { 
    queue<int> queue; 
    queue.push(10); 
    queue.push(20);
    queue.push(30); 
    while (!queue.empty()){ 
        int front = queue.front(); cout << front << endl; queue.pop(); 
    } 
    return 0; 
} 
/***/
#include <iostream>  
using namespace std;
const int MAX_SIZE = 10;  
class CircularQueue {   
    public:     
    CircularQueue(){       
        head = tail = -1;       
        buffer = new int[MAX_SIZE];
    }      
        ~CircularQueue(){       
            delete [] buffer;     
        }
        void enqueue(int value){       if ((tail + 1) % MAX_SIZE == head) {              cout << "Coda piena, non è possibile inserire elementi." << endl;         
                    return;       
            } 
            tail = (tail + 1) % MAX_SIZE;       
            buffer[tail] = value;  
            if (head == -1)   
                head = tail;       
        }
        int dequeue(){       
            if (head == -1){         cout << "Coda vuota, non è possibile rimuovere elementi." << endl;         
                return -1;       
            }        
            int value = buffer[head];   
            if (head == tail){         head = tail = -1;       
            }else {         
                head = (head + 1) % MAX_SIZE;       
            }        
            return value;     
        }    
        private:     
        int head, tail;     
        int *buffer;
}; 
/***/
#include <stdio.h> 
#include <stdlib.h>  
#define MAX_SIZE 100  
int queue[MAX_SIZE]; 
int front = 0; 
int rear = -1; 
int item_count = 0;  
void insert(int data){     
    if (item_count == MAX_SIZE){         printf("Error: Queue overflow\n");     
    } else{         
        rear = (rear + 1) % MAX_SIZE;        
        queue[rear] = data;         item_count++;    
    }
}  
int remove_data(){     
    int data;     
    if (item_count == 0){         printf("Error: Queue underflow\n");         return -1;     
    } else {         
        data = queue[front];         front = (front + 1) % MAX_SIZE;         
        item_count--;         
        return data;     
    } 
}  
void print_queue(){     
    int i;     
    if (item_count == 0){         
        printf("Error: Queue is empty\n");     
    } else {         
        for (i = 0; i < item_count; i++){             
            int index = (front + i) % MAX_SIZE; 
            printf("%d\n", queue[index]);   
        }     
    } 
} 
/***/
#include <iostream> 
using namespace std;  
class Stack{ 
    private: 
    struct Node{         
        int data;         
        Node* next;     
    };     
    Node* top;  
    public:     
    Stack(){ 
        top = nullptr; 
    }      
    void push(int value){        
        Node* new_node = new Node;
        new_node->data = value;
        new_node->next = top;  
        top = new_node;     
    }      
    int pop(){        
        if (top == nullptr){        
            cout << "Pila vuota!\n";            
            return -1;         
        }          
        int value = top->data;
        Node* temp = top;         
        top = top->next;         
        delete temp;         
        return value;     
    } 
}; 
/***/
#include <stdio.h>
#include <stdlib.h>  
struct StackNode{     
    int data;    
    struct StackNode* next; 
};
struct Stack{     
    struct StackNode* top;
};  
struct StackNode* newNode(int data){     
    struct StackNode* node = (struct StackNode*)  malloc( sizeof( struct StackNode));     
    node->data = data;    
    node->next = NULL;     
    return node; 
}
struct Stack* createStack(){     struct Stack* stack = (struct Stack*) malloc( sizeof(struct Stack));     
    stack->top = NULL;     
    return stack; }

int isEmpty(struct Stack* stack){     return !stack->top; 
} 
void push(struct Stack* stack, int data){     
    struct StackNode* node = newNode(data);     
    node->next = stack->top;
    stack->top = node;     
    printf("%d inserito nella pila\n", data);
}
int pop(struct Stack* stack){     if (isEmpty(stack))                 return -1;     
    struct StackNode* temp = stack->top;     
    int popped = temp->data;    
    stack->top = stack->top->next;
    free(temp);     
    return popped; 
} 
int peek(struct Stack* stack) {     if (isEmpty(stack))                 return -1;     
    return stack->top->data; 
} 
/***/
#include <stdio.h>
#include <stdbool.h>   
#define MAX_SIZE 100  
int stack[MAX_SIZE]; 
int top = -1;  
bool isEmpty(){   
    return top == -1; 
}  
bool isFull(){  
    return top == MAX_SIZE-1; 
}  
void push(int value){     
    if (isFull()){         
        printf("Pila Full\n");
        return;    
    }      
    top++;     
    stack[top] = value; 
} 
int pop(){     
    if (isEmpty()){        
        printf("Pila vuota!\n");
        return -1;     
    } 
int value = stack[top];    
    top--;     
    return value; 
} 
/***/
#include <memory> 
using namespace std; 
class LinkedListUP{ 
    private: 
    struct Node{ 
        int data; 
        shared_ptr<Node> next; 
        Node(int data) : data(data), next(nullptr) {} 
        Node(int data, shared_ptr<Node> next) : data(data), next(std::move(next)) {} 
    }; 
    shared_ptr<Node> head; 
    public:
        LinkedListUP(); 
        void insertAtStart(int value); 
        void insertAtEnd(int value); 
        void deleteNode(int value);
        void printList(); 
}; 
#include <iostream> 
#include "LinkedListUP.h"
LinkedListUP::LinkedListUP(){ 
    head=NULL; 
} 
void LinkedListUP::insertAtStart(int value){ 
    auto new_node = make_shared<Node>(value); 
    new_node->next = move(head); head = move(new_node); 
} 
void LinkedListUP::insertAtEnd(int value){ 
    if (!head){ 
        head = make_shared<Node>(value); 
    }
    else{ 
        auto current = head.get();
        while (current->next){ current = current->next.get(); 
        } 
        current->next = make_shared<Node>(value); 
    } 
} 
void LinkedListUP::deleteNode(int value){ 
    if (!head){ 
        return; 
    }
    if (head->data == value){ 
        head = move(head->next); return; 
    } 
    auto current = head.get();
    while (current->next && current->next->data != value){ 
        current = current->next.get(); 
    }
    if (current->next){ 
        current->next = move(current->next->next); 
    } 
}
void LinkedListUP::printList(){
    if (!head){ 
        cout << "List is empty" << endl; 
        return; 
    } 
    auto curr = head;
    while (curr){ 
        cout << curr->data << " "; curr = curr->next; 
    } 
    cout<<endl; 
}
/***/
#include <iostream> 
#include <cstdlib> 
using namespace std; 
void inserisce_dietro(){ 
    list root=NULL, aux; 
    char n;  
    while ((n=getchar()) != '\n'){ 
        if (root==NULL){  
            root=(list)malloc(sizeof(struct list_element));  
            aux=root;  
        } 
        else{  
            aux->next=(list)malloc(sizeof(struct list_element)); 
            aux=aux->next;  
        } 
        aux->value=n;  
        aux->next=NULL;  
    }  
} 
void showlist(list l){  
    printf("[");  
    while (l!=NULL){ 
        putchar(l->value);  
        l=l->next;  
        if (l!=NULL)        
            printf(",");    
    }   
    printf("]\n");  
} 
void showr_list(list l){   
    if (l!=NULL){     
        putchar(l->value);      
        if (l->next!=NULL){       printf(",");  showr_list(l->next);
        }    
    }  
} 
void showr_l(list l){   
    printf("[");    
    showr_list(l);    
    printf("]\n");  
} 
/***/
int RicercaSequential(int *arr, int len, int val){
    int i = 0;
    while(i < len){
        if(arr[i] == val)
            return i;
        i++;
    }
    return -1;
}
/***/
int RicercaBinarySplit(int *arr, int val, int l, int r){
    if(r < l)
        return -1;
    else{
        int mid = (l + r) / 2;
        if(arr[mid] == val)
            return mid;
        if(mid == 0)
            return -1;
        else if(val < arr[mid])
            return RicercaBinarySplit(arr, val, l, mid - 1);
        else
            return RicercaBinarySplit(arr, val, mid + 1, r);
    }
}
/***/
int RecursiveMin(int arr[], int len, int l, int r){
    if(l == r)
        return arr[l];
    else {
        int mean = (l + r)/2;
        return min(RecursiveMin(arr, len, l, mean), RecursiveMin(arr, len, mean + 1, r));
    }
}
/***/
void Hanoi(int n, int A, int C, int B){
    if(n == 1)
        cout << A << " " << C << "\n";
    else{
        Hanoi(n, A, B, C);
        cout << A << " " << C << "\n";
        Hanoi(n, B, C, A);
    }
}
int main(){
    Hanoi(3, 1, 3 , 2);
}
/***/
int Fib(int n){
    if(n == 1 || n == 2)
        return 1;
    int first = 1, second = 1, fib;
    for(int i = 3; i <= n; i++){
        fib = first + second;
        first = second;
        second = fib;
    }
    return fib;
}
/***/
int Fib(int n){
    int fib;
    if(n == 1 || n == 2)
        fib = 1;
    else
        fib = Fib(n - 1) + Fib(n - 2);
    return fib;
}
/***/
int fattorial(int n){
    int fatt;
    if(n == 1)
        fatt = 1;
    else
        fatt = n * fattorial(n - 1);
    return fatt;
}
/***/
from array import *
a = [0] * 10
b = ['A', ' ', 'B', 30, 40]
print(a, b)
arr = array('i', [10, 20, 30])
arr[2] = 80
for x in arr:
    print(x)
/***/
int main(){
    int *p = NULL;
    p = new int[100];
    for(int i = 0; i < 100; i++)
        p[i] = rand();
    delete []p;
    for(int i = 0; i < 100; i++)
        cout << p[i] << " ";
}
/***/
void RicercaBinaryNonRecursive(int arr[], int n, int val){
    int l = 0, r = n - 1;
    int mid =(l + r)/2;
    while(l != r){
        if(arr[mid] == val)
            return mid;
        if(arr[mid] < val)
            l = mid + 1;
        else
            r = mid - 1;
        mid = (l + r)/2;
    }
    return (arr[mid] == val) ? mid : -1;
}
/***/
def RicercaLineare(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
/***/
def RicercaBinary(arr, key):
   l = 0, r = len(arr)
   mid = (l + r)//2
   while True:
       if mid < 0 || mid >= len(a):
           return -1
        if arr[mid] == val:
            return mid
        if arr[mid] < val:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l + r)//2
/***/
int main(){
    int arr[8] = {41, 37, 10, 74, 98, 22, 83, 66};
    int n = 8;
    for(int i = n - 1; i >= 0; i--){
        int maxi = i;
        for(int j = i - 1; j >= 0; j--){
            if(arr[j] > arr[maxi])
                maxi = j;
        }
        if(maxi != i){
            int tmp = arr[i];
            arr[i] = arr[maxi];
            arr[maxi] = tmp;
        }
    }
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
}
/***/
arr = [41, 37, 10, 74, 98, 22, 83, 66]
n = 8
for i in range(n - 1, -1, -1):
    maxi = i
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[maxi]:
            maxi = j
    if maxi != i:
        tmp = arr[i]
        arr[i] = arr[maxi]
        arr[maxi] = tmp
print(arr)
/***/
arr = [41, 37, 10, 74, 98, 22, 83, 66]
n = 8
for i in range(1, n):
    val = arr[i]
    j = i - 1
    while(j >= 0 and arr[j] > val):
        arr[j + 1] = arr[j];
        j = j - 1
    arr[j + 1] = val
print(arr)
/***/
int main(){
    int arr[8] = {41, 37, 10, 74, 98, 22, 83, 66};
    int n = 8;
    for(int i = 1; i < n; i++){
        int val = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > val){
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = val;
    }
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
}
/***/
int main(){
    int arr[8] = {41, 37, 10, 74, 98, 22, 83, 66};
    int n = 8;
    bool swap = true;
    while(swap){
        swap = false;
        for(int i = 0; i < n - 1; i++){
            if(arr[i] > arr[i + 1]){
                int tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
                swap = true;
            }
        }
    }
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
}
/***/
arr = [41, 37, 10, 74, 98, 22, 83, 66]
n = 8
swap = True
while(swap):
    swap = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            tmp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = tmp
            swap = True
print(arr)
/***/
#include<iostream>
using namespace std;
void merge(int arr[], int l, int mid, int r){
    int i = l, j = mid + 1, k = 0;
    int tmp[r - l + 1];
    for(int i = 0; i < (r - l + 1); i++)
        tmp[i] = 0;
    while(i <= mid && j <= r){
        if(arr[i] <= arr[j]){
            tmp[k] = arr[i]; i++;
        }
        else{
            tmp[k] = arr[j]; j++;
        }
        k++;
    }
    while(i <= mid){
        tmp[k] = arr[i];
        i++; k++;
    }
    while(j <= r){
        tmp[k] = arr[j];
        j++; k++;
    }
    for(k = l; k <= r; k++)
        arr[k] = tmp[k - l];
}
void mergesort(int arr[], int l, int r){
    if(l < r){
        int mid = (l + r)/2;
        mergesort(arr, l, mid);
        mergesort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }
}
int main(){
    int arr[8] = {41, 37, 10, 74, 98, 22, 83, 66}; 
    int n = 8;
    mergesort(arr, 0, n - 1);
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
}
/***/
def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    k = 0
    tmp = [0] * (r - l + 1)
    
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i+= 1
        else:
            tmp[k] = arr[j]
            j+= 1
        k+= 1
    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1
    while j <= r:
        tmp[k] = arr[j]
        j+= 1
        k+= 1
    for k in range(l, r + 1):
        arr[k] = tmp[k - l]
def mergesort(arr, l, r):
    if(l < r):
        mid = (l + r)//2;
        mergesort(arr, l, mid);
        mergesort(arr, mid + 1, r);
        merge(arr, l, mid, r);

arr = [41, 37, 10, 74, 98, 22, 83, 66]
n = 8
mergesort(arr, 0, n - 1);
print(arr)
/***/
def quicksort(arr, l, r):
    i = l
    j = r
    pivot = arr[(l + r) //2]
    while i <= j:
        while arr[i] < pivot:
            i+= 1
        while arr[j] > pivot:
            j-= 1
        if i <= j:
            if i < j:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            i += 1
            j -= 1
    if l < j:
        quicksort(arr, l, j)
    if i < r:
        quicksort(arr, i, r)
arr = [41, 37, 10, 74, 98, 22, 83, 66]
n = 8
quicksort(arr, 0, n - 1);
print(arr)
/***/
void quicksort(int arr[], int l, int r){
    int i = l, j = r;
    int pivot = arr[(l + r)/2];

    while(i <= j){
        while(arr[i] < pivot)
            i++;
        while(arr[j] > pivot)
            j--;
        if(i <= j){
            if(i < j){
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
            i++; j--;
        }
    }
    if(l < j)
        quicksort(arr, l, j);
    if(i < r)
        quicksort(arr, i, r);
}
int main(){
    int arr[8] = {41, 37, 10, 74, 98, 22, 83, 66}; 
    int n = 8;
    quicksort(arr, 0, n - 1);
    for(int i = 0; i < n; i++)
        cout << arr[i] << " ";
}
/***/
#include <iostream> 
using namespace std; 
void heapify(int a[],int sx,int dx){
    int temp=a[sx], i=sx, j= 2*i;
    while (j <= dx){    
        if((j < dx) && (a[j + 1] > a[j]))      
            j++;    
        if (temp < a[j]) {       a[i] = a[j];      
            i = j;      
            j = 2 * i;     
        } 
        else       
            j = dx + 1;   
    }      
    if (i != sx)   
    a[i] = temp;
}  
void heapsort(int a[], int n) {   int tmp,sx,dx;
    for (sx = n / 2;sx >= 1;sx--)     heapify(a,sx,n); 
    for (dx = n;dx > 1;dx--){     tmp = a[1];     
        a[1] = a[dx];     
        a[dx] = tmp;    
        heapify(a,1,dx - 1);   
    } 
}
int main(){
    int a[]={0, 42, 38, 11, 75, 99, 23, 84, 67};   
    int n=8;  
    heapsort(a,n);   
    for (int i=1;i<n+1;i++)     cout<<a[i]<<" "; 
}  
/***/
def heapify(a,sx,dx):      
    temp=a[sx]   
    i=sx   
    j= 2*i      
    while j <= dx:     
        if j < dx and a[j + 1] > a[j]:       
            j+=1     
        if temp < a[j]:       
            a[i] = a[j]       
            i = j       
            j = 2 * i     
        else:       
            j = dx + 1      
    if i != sx:     
        a[i] = temp    
def heapsort(a,n): 
    for sx in range(n//2,0,-1):     heapify(a,sx,n)     
    for dx in range(n,1,-1):     tmp = a[1]     
        a[1] = a[dx]     
        a[dx] = tmp     
        heapify(a,1,dx-1)   
a=[0, 42, 38, 11, 75, 99, 23, 84, 67]
n=8 
heapsort(a,n)
print(a) 
/***/
int main() {
    int* int_ptr_malloc = (int*) malloc(sizeof(int));
    *int_ptr_malloc = 5; 
    cout<<"Valore puntato: "<<*int_ptr_malloc<<endl; 
    free(int_ptr_malloc);
    int* int_ptr_new = new int; 
    *int_ptr_new = 10;
    cout <<"Valore puntato: "<<*int_ptr_new<<endl; 
    delete int_ptr_new; 
    return 0;
}
/***/
int main(){ 
    list root=NULL, aux;  
    char n;  
    while ((n=getchar()) != '\n'){ aux=(list)malloc(sizeof(struct list_element));  
        aux->value=n;  
        aux->next=root;  
        root=aux; 
    }   
} 
