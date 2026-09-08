def memoria_dinamica():
    frutas = []
    frutas.append("mango")
    frutas.append("manzana")
    frutas.append("granada")
    frutas.append("durazno")
    print("Lista inicial de frutas:")
    print(frutas)
    frutas.pop(0)  
    frutas.pop(1)  
    frutas.append("sandía")
    print("\nLista de frutas:")
    print(frutas)

memoria_dinamica()