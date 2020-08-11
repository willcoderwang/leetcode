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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode front=head, end = head;
        for (int i=0; i <= n; ++i) {
            if (end == null) {
                return head.next;
            }
            end = end.next;
        }

        while (end != null) {
            end = end.next;
            front = front.next;
        }

        front.next = front.next.next;

        return head;
    }
}