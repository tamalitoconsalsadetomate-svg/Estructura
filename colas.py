class Order:
    def __init__(self, qtty: int, customer: str):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print(f"     ------------")

    def get_qtty(self) -> int:
        return self.qtty

    def get_customer(self) -> str:
        return self.customer


class Node:
    def __init__(self, info, next_node=None):
        self.info = info    
        self.next = next_node 

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

class LinkedQueue:
    def __init__(self):
        self.top = None   
        self.tail = None  
        self._size = 0    

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.top is None

    def front(self):
        if self.is_empty():
            return None
        return self.top.get_info()

    def enqueue(self, info):
        new_node = Node(info, None)
        if self.is_empty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        
        info = self.top.get_info()
        self.top = self.top.get_next()
        self._size -= 1
        
        if self.top is None:  
            self.tail = None
            
        return info

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self._size}")
        
        node = self.top
        index = 1
        while node is not None:
            print(f"   ** Element {index}")
            order = node.get_info()
            if isinstance(order, Order):
                order.print_order()
            else:
                print(f"     Info: {order}")
                print(f"     ------------")
            node = node.get_next()
            index += 1
            
        print("******************************")

    def get_nth(self, pos: int):
        if pos < 1 or pos > self._size:
            return None
        
        node = self.top
        current_pos = 1
        while node is not None:
            if current_pos == pos:
                return node.get_info()
            node = node.get_next()
            current_pos += 1
            
        return None

class TestQueue:
    @staticmethod
    def main():
        print("--- INICIANDO PRUEBAS DE LA COLA ---")
        queue = LinkedQueue()

        o1 = Order(20, "cust1")
        o2 = Order(30, "cust2")
        o3 = Order(40, "cust3")
        o4 = Order(50, "cust3")

        print("\n-> Añadiendo pedidos o1, o2, o3:")
        queue.enqueue(o1)
        queue.enqueue(o2)
        queue.enqueue(o3)
        queue.print_info()

        print("\n-> Consultando el primer elemento (front):")
        first_order = queue.front()
        if first_order:
            first_order.print_order()

        print("\n-> Extrayendo un elemento (dequeue):")
        extracted = queue.dequeue()
        if extracted:
            print("Pedido extraído:")
            extracted.print_order()
        queue.print_info()

        print("\n-> Añadiendo el cuarto pedido (o4):")
        queue.enqueue(o4)
        queue.print_info()

        print("\n-> Probando getNth(3) [Tercer elemento]:")
        nth_element = queue.get_nth(3)
        if nth_element:
            nth_element.print_order()
        else:
            print("Posición no válida.")


TestQueue.main()