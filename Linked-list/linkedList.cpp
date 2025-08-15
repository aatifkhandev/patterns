#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node *next;

    Node(int data){
   this->data = data;
   this->next = NULL;
    }

};

class List{
    Node *head;
    Node *tail;

    public:
    List(){
        head = tail = NULL;
    }
    
    void push_front(int val){
        if(head == NULL){
            head = tail = NULL;
        }
        Node *newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }

    void pop_back(){
        if(head == NULL){
            return;
        }
        Node *temp = head;
        while(temp->next!=tail){
            temp = temp->next;
        }
        temp->next = NULL;
        delete tail;
        tail = temp;
    }

    void print(){
        Node *temp = head;
        while(temp!=NULL){
            cout<<temp->data;
            temp = temp->next;
        }
        cout<<endl;
    }
};

int main(){
    List ll;
    ll.push_front(1);
    ll.push_front(2);
    ll.push_front(3);
    ll.print();
    ll.pop_back();
    ll.print();
}