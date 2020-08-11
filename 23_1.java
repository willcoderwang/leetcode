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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length < 1)
            return null;

        ListNode result = lists[0];

        for (int i=1; i<lists.length; ++i) {
            result = mergeTwoList(result, lists[i]);
        }

        return result;
    }

    private ListNode mergeTwoList(ListNode l1, ListNode l2) {
        // l1 and l2 are sorted
        ListNode head = new ListNode(0);
        ListNode head_end = head;
        while(l1 != null && l2 != null) {
            ListNode min_node;
            if (l1.val <= l2.val) {
                min_node = l1;
                l1 = l1.next;
            } else {
                min_node = l2;
                l2 = l2.next;
            }
            head_end.next = min_node;
            head_end = head_end.next;
        }

        if (l1 != null)
            head_end.next = l1;
        if (l2 != null)
            head_end.next = l2;

        return head.next;
    }
}