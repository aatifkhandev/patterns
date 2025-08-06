#include<iostream>
using namespace std;

class Node{
    public:
  int data;
  Node* next;

  Node(int val){
    data = val;
    next = NULL;
  }
};

Node* reverse_List(Node* head){

    // if(head==NULL ||head->next ==NULL){
    //     return head;
    // }

    Node* prev = NULL;
    Node* curr = head;
    Node* forward = NULL;
    
    while(curr!=NULL){
        forward = curr->next;
        curr->next = prev;
        prev = curr;
        curr = forward;
    }
    return prev;

}

void printList(Node* head){
    Node*temp = head;
    while(temp!=NULL){
        cout<<temp->data;
        temp = temp->next;
    }
    cout<<endl;
}

int main(){
Node* head = new Node(1);
head->next = new Node(2);
head->next->next = new Node(3);
head = reverse_List(head);
printList(head);
return 0;
}