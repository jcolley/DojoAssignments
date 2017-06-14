//Singley Linked List

function SLLNode(val) {
    this.val = val;
    this.next = null;
}

function SList() {
    this.head = null;
    this.addFront = function (val) {
        var newNode = new SLLNode(val);
        newNode.next = this.head;
        this.head = newNode;
        return this;
    }
}


var myList = new SList();
myList.addFront(1).addFront(2).addFront(3);
console.log(JSON.stringify(myList));