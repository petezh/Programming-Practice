/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
ListNode* reverseBetween(ListNode* head, int m, int n)
{
    ListNode dummy(0);
    dummy.next = head;

    ListNode* p = &dummy;
    for (n -= m; m > 1; --m, p = p->next); // find the node precedes node m and update n relative to m.

    ListNode* q = p->next;
    ListNode* r = q->next;
    for (ListNode* t; n > 0; --n, t = r->next, r->next = q, q = r, r = t);

    p->next->next = r;
    p->next = q;

    return dummy.next;
}
};