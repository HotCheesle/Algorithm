#include <iostream>

using namespace std;

class Node {
public:  
  int code;
  Node* next = nullptr;
};

Node node_pool[1000000];
int input_data[10000] = { 0 };
Node* free_node_head = &node_pool[0];
Node* free_node_tail = &node_pool[1000000];

void new_nnode(int* data, int data_cnt, Node** head, Node** tail); // n개의 리스트 만들기
Node* get_pre_start(int start, Node* head); // start-1 번째 노드 주소 찾기


int main() {
  for (int i = 0; i < 999999; i++) {
    node_pool[i].next = &node_pool[i+1];
  }

  for (int tc = 1; tc < 11; tc++) {
    int data_cnt, instruction_cnt, start; // 데이터 개수, 명령어 개수, x번째 노드
    char instruction; // 명령어
    Node* head = nullptr; Node* tail = nullptr; Node* pre = nullptr;
    Node* new_head = nullptr; Node* new_tail = nullptr;

    cin >> data_cnt;
    for (int i = 0; i < data_cnt; i++) { // 초기화
      cin >> input_data[i];
    }
    new_nnode(input_data, data_cnt, &head, &tail);

    cin >> instruction_cnt;
    for (int ins = 0; ins < instruction_cnt; ins++) {
      cin >> instruction;
      switch (instruction){
        case 'I': 
          break;
        case 'D': 
          break;
        case 'A':
          break;
        default:
          return 1;
      }
    }
  }


  return 0;
}

void new_nnode(int* data, int data_cnt, Node** head, Node** tail) {
  *head = free_node_head;
  Node* cur = free_node_head;
  for (int i = 0; i < data_cnt; i++) {
    cur -> code = data[i];
    cur = cur -> next;
  }
  *tail = cur;
  free_node_head = cur->next;
}

void free_nnode(Node* start, int node_cnt, Node** tail){
  Node* cur = start;
  for (int i = 0; i < node_cnt-1; i++) {
    cur = cur -> next;
  }
  free_node_tail -> next = start -> next;
  if (*tail == cur) {
    *tail = start;
  }
  else {
    start -> next = cur -> next;
  }

}

Node* get_pre_start(int start, Node* head) {
  Node* cur = head;
  for (int i = 0; i < start-1; i++) {
    cur = cur -> next;
  }
  return cur;
}