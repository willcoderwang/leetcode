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
        ListNode result = new ListNode(0);
        ListNode result_end = result;
        boolean found = false;
        do {
            int min_index = 0;
            int min = 0;
            found = false;
            for (int i=0; i<lists.length; ++i) {
                ListNode node = lists[i];
                if (node != null) {
                    if (found && node.val < min) {
                        min_index = i;
                        min = node.val;
                    }
                    else if (!found) {
                        min_index = i;
                        min = node.val;
                        found = true;
                    }
                }
            }

            if (found) {
                result_end.next = lists[min_index];
                result_end = result_end.next;
                lists[min_index] = lists[min_index].next;
            } else {
                break;
            }
        } while (found);

        return result.next;
    }
}