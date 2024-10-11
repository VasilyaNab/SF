class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item_id):
        self.items.append(item_id)
    def is_empty(self):
        return len(self.items) == 0
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Очередь пуста")
            else:
            self.items.pop(0)
            return self.items
    def show_queue(self):
        output = " ".join(map(str, self.items))
        print(output)
