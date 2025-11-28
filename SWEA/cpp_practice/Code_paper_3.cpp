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
void free_nnode(Node* start, int node_cnt, Node** tail); // start 이후부터 node_cnt만큼 삭제
void insert_nnode(Node* start, Node* new_head, Node* new_tail); // start 이후에 새 리스트 삽입
void append_nnode(Node** tail, Node* new_head, Node* new_tail); // tail에 새 리스트 추가
void popleft_nnode(Node** head, int node_cnt); // head에 node_cnt만큼 삭제
void append_left_nnode(Node** head, Node* new_head, Node* new_tail); // head앞에 새 리스트 추가
Node* get_start(int start, Node* head); // start 번째 노드 주소 찾기
void print_hedder(Node* head); // 코드 10개 출력
void print_all(Node* head); // 디버그용


int main() {
	for (int i = 0; i < 999999; i++) {
		node_pool[i].next = &node_pool[i + 1];
	}

	for (int tc = 1; tc < 11; tc++) {
		int data_cnt, instruction_cnt, start; // 데이터 개수, 명령어 개수, x번째 노드
		char instruction; // 명령어
		Node* head = nullptr; Node* tail = nullptr; Node* start_node = nullptr;
		Node* new_head = nullptr; Node* new_tail = nullptr;

		cin >> data_cnt;
		for (int i = 0; i < data_cnt; i++) { // 초기화
			cin >> input_data[i];
		}
		new_nnode(input_data, data_cnt, &head, &tail);
		// print_all(head);

		cin >> instruction_cnt;
		for (int ins = 0; ins < instruction_cnt; ins++) {
			cin >> instruction;
			switch (instruction) {
			case 'I':
				cin >> start >> data_cnt;
				for (int i = 0; i < data_cnt; i++) {
					cin >> input_data[i];
				}
        start_node = get_start(start, head);
        new_nnode(input_data, data_cnt, &new_head, &new_tail);
        if (start == 0) { // head 앞에 붙이기
          append_left_nnode(&head, new_head, new_tail);
        }
        else if (start_node == tail) { // tail에 붙이기
          append_nnode(&tail, new_head, new_tail);
        }
        else { // 중간에 삽입
          insert_nnode(start_node, new_head, new_tail);
        }
				break;
			case 'D':
				cin >> start >> data_cnt;
				if (start == 0) {
					popleft_nnode(&head, data_cnt);
				}
				else {
					start_node = get_start(start, head);
					free_nnode(start_node, data_cnt, &tail);
				}
				break;
			case 'A':
				cin >> data_cnt;
				for (int i = 0; i < data_cnt; i++) {
					cin >> input_data[i];
				}
				new_nnode(input_data, data_cnt, &new_head, &new_tail);
				append_nnode(&tail, new_head, new_tail);
				break;
			default:
				return 1;
			}
			// print_all(head);
		}
		cout << '#' << tc << ' ';
		print_hedder(head);
		cout << endl;
	}

	return 0;
}

void new_nnode(int* data, int data_cnt, Node** head, Node** tail) {
	*head = free_node_head;
	Node* cur = free_node_head;
	for (int i = 0; i < data_cnt-1; i++) {
		cur->code = data[i];
		cur = cur->next;
	}
	cur->code = data[data_cnt - 1];
	*tail = cur;
	free_node_head = cur->next;
	cur->next = nullptr;
}

void free_nnode(Node* start, int node_cnt, Node** tail) {
	Node* cur = start;
	for (int i = 0; i < node_cnt - 1; i++) {
		cur = cur->next;
	}
	free_node_tail->next = start->next;
	cur = cur->next;
	if (*tail == cur) {
		*tail = start;
		(*tail)->next = nullptr;
	}
	else {
		start->next = cur->next;
	}
	free_node_tail = cur;
	cur->next = nullptr;
}

void insert_nnode(Node* start, Node* new_head, Node* new_tail) {
	Node* post = start->next;
	start->next = new_head;
	new_tail->next = post;
}

void append_nnode(Node** tail, Node* new_head, Node* new_tail) {
	(*tail)->next = new_head;
	(*tail) = new_tail;
}

void popleft_nnode(Node** head, int node_cnt) {
	Node* cur = *head;
	for (int i = 0; i < node_cnt - 1; i++) {
		cur = cur->next;
	}
	free_node_tail->next = *head;
	*head = cur->next;
	cur->next = nullptr;
}

void append_left_nnode(Node** head, Node* new_head, Node* new_tail) {
  new_tail->next = *head;
  *head = new_head;
}

Node* get_start(int start, Node* head) {
	Node* cur = head;
	for (int i = 0; i < start-1; i++) {
		cur = cur->next;
	}
	return cur;
}

void print_hedder(Node* head) {
	Node* cur = head;
	for (int i = 0; i < 10; i++) {
		cout << cur->code << ' ';
		if (cur->next == nullptr) {
			break;
		}
		cur = cur->next;
	}
}

void print_all(Node* head) {
	while (head != nullptr) {
		cout << head->code << ' ';
		head = head->next;
	}
	cout << endl;
}