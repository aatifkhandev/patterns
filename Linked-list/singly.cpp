#include<iostream>
using namespace std;

class Node{
    public:

    int data;
    Node*next = NULL;

    Node(int data){
        this->data = data;
        this->next = NULL;
    }
};

void push_front(Node*&head , int data){
    Node*temp = new Node(data);
    temp->next = head;
    head  =  temp;
}

void print(Node*&head){
    Node*temp = head;
    while(temp!=NULL){
        cout<<temp->data<<"";
        temp = temp->next;
    }
    cout<<endl;
}


int main(){
Node *node1  = new Node(10);
Node*head = node1;
print(head);
push_front(head,12);
print(head);
}