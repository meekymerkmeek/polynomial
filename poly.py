"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my honor, Mark Fakhory, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: mwf634
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """
        Insert a term into the polynomial in descending order by exponent.
        If a term with the same exponent exists, sum the coefficients.
        Remove term if the resulting coefficient is zero.
        """
        if coeff == 0:
            return
        new_node = Node(coeff, exp)

        if self.head is None or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        current = self.head
        while current and current.exp > exp:
            prev = current
            current = current.next

        if current and current.exp == exp:
            current.coeff += coeff
            if current.coeff == 0:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            return
        new_node.next = current
        if prev:
            prev.next = new_node
        else:
            self.head = new_node
    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """
        Add another polynomial to the current one.
        Return a new LinkedList representing the sum.
        """
        result = LinkedList()
        a = self.head
        b = p.head

        while a and b:
            if a.exp > b.exp:
                result.insert_term(a.coeff, a.exp)
                a = a.next
            elif a.exp < b.exp:
                result.insert_term(b.coeff, b.exp)
                b = b.next
            else:
                result.insert_term(a.coeff + b.coeff, a.exp)
                a = a.next
                b = b.next

        while a:
            result.insert_term(a.coeff, a.exp)
            a = a.next

        while b:
            result.insert_term(b.coeff, b.exp)
            b = b.next

        return result

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        """
        Multiply the current polynomial with another.
        Return a new LinkedList representing the product.
        """
        result = LinkedList()
        a = self.head

        while a:
            temp = LinkedList()
            b = p.head
            while b:
                temp.insert_term(a.coeff * b.coeff, a.exp + b.exp)
                b = b.next
            result = result.add(temp)
            a = a.next
        return result

    # Return a string representation of the polynomial.
    def __str__(self):
        """
        Return a string representation of the polynomial.
        Format: (coeff, exp) + (coeff, exp) ...
        """
        terms = []
        current = self.head
        while current:
            terms.append(str(current))
            current = current.next
        return " + ".join(terms)


def main():
    """
    Reads two polynomials from input, computes and prints their sum and product.
    Input format follows assignment specification.
    """
    input_lines = []
    try:
        while True:
            line = input()
            input_lines.append(line)
    except EOFError:
        pass

    p = LinkedList()
    q = LinkedList()

    i = 0
    n = int(input_lines[i])
    i += 1
    for _ in range(n):
        coeff, exp = map(int, input_lines[i].split())
        q.insert_term(coeff, exp)
        i += 1

    while i < len(input_lines) and input_lines[i].strip() == "":
        i += 1

    m = int(input_lines[i])
    i += 1
    for _ in range(m):
        coeff, exp = map(int, input_lines[i].split())
        q.insert_term(coeff, exp)
        i += 1

    sum_poly = p.add(q)
    prod_poly = p.mult(q)

    print(str(sum_poly))
    print(str(prod_poly))



if __name__ == "__main__":
    main()
