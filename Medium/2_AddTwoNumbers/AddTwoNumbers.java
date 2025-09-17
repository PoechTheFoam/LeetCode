package LeetCode;
public class AddTwoNumbers{
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }}
    class Solution {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            int carry=0;
            ListNode result=new ListNode(0);
            ListNode dummy=result;
            while (l1!=null||l2!=null){
                int x=(l1!=null)?l1.val:0;
                int y=(l2!=null)?l2.val:0;
                int res=x+y;
                if (carry!=0){
                    res+=carry;
                    carry=0;
                }
                if (res>=10) {
                    carry=res/10;
                    res=res%10;
                }
                dummy.next=new ListNode(res);
                if (l1!=null) l1=l1.next;
                if (l2!=null) l2=l2.next;
                dummy=dummy.next;
            }
            if (carry!=0) dummy.next=new ListNode(carry);
            return result.next;
        }
    }
}
