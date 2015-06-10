/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var sum = listnodeToNum(l1) + listnodeToNum(l2);
	return numToListnode(sum);
};

var listnodeToNum = function(listnode){
	var num = 0, digit = 0;

	while(listnode !== null){
		num += listnode.val * Math.pow(10, digit);
		digit += 1;
		listnode = listnode.next;
	}
	return num;
}

var numToListnode = function(num) {
	var lst = ("" + num).split("").reverse();
	var firstNode, previousNode;
	
	for(var i in lst){
		var node = new ListNode(parseInt(lst[i]));
		firstNode = firstNode || node;
		
		if(previousNode === undefined){
			previousNode = node;
		} else{
			previousNode.next = node;
			previousNode = node;
		}
	}
	return firstNode;
}