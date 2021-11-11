
class Pizza(object):

    class PizzaBuilder(object):
        """
        A classe interna PizzaBuilder retorna a si mesma de
        todos os métodos, exceto build (), que retorna um
        nova instância de Pizza construída com as opções selecionadas.
        """
        def __init__(self):
            self.extra_cheese = False
            self.tomato = False

        def add_tomato(self):
            self.tomato = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)

    def __init__(self, builder):
        """
        O construtor da classe leva uma instância
        de seu construtor como um parâmetro.
        """
        self.tomato = builder.tomato
        self.extra_cheese = builder.extra_cheese


def main():
    print ("Construindo uma pizza simples ...")

    # Podemos fazer esse encadeamento de opções.
    pizza = Pizza.PizzaBuilder().add_tomato().add_extra_cheese().build()

    if pizza.tomato:
        print ("A pizza tem tomate.")
    if pizza.extra_cheese:
        print ("A pizza tem queijo extra.")
        print("---------------------------------------------------------------")

if __name__ == "__main__":
    main()

