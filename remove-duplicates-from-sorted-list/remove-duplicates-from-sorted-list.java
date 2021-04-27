/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
            // if done
            if(head == null || head.next == null) return head;
            // recurse
            head.next = deleteDuplicates(head.next);
            // if dupe, skip
            return head.val == head.next.val ? head.next : head;
    }
}