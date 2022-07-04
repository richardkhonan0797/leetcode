/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    let dummy = new ListNode(0, head);
    let l = dummy;
    let r = head;
    
    for (let i = 0; i < n; i++) {
        r = r.next;    
    }
    
    while (r) {
        r = r.next;
        l = l.next;
    }
    
    l.next = l.next.next;
    
    return dummy.next;
};
