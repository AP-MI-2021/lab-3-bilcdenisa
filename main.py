import math


def citire_lista():
    int_lista = []
    str_lista = input('Introduceti elemente')
    str_elemente = str_lista.split(' ')

    for str_element in str_elemente:
        int_lista.append(int(str_element))

    return int_lista

def has_same_div_count(lista):
    # verifica daca elementele din lista au acelasi numar de divizori
    # :param lista: subsecventa pe care o verificam
    # :return: returnam true daca elementele au acelasi numar de divizori, false in caz contrar


    #verific cati divizori are primul numar din lista
    nr_divizori = 0
    for divizor in range(1,lista[0]+1):
        if lista[0]%divizor == 0:
            nr_divizori +=1

    #verific daca restul elementelor au acelasi nr de divizori
    for element in lista:
        nr_divizori2 = 0
        for divizor in range(1,element+1):
            if element % divizor == 0:
                nr_divizori2 +=1
        if nr_divizori != nr_divizori2:
            return False

    return True


def get_longest_same_div_count(lst: list[int]) -> list[int]:
    # determina cea mai lunga secventa cu proprietatea ca toate numerele au acelasi numar de divizori
    # :param lst: lista in care cautam subsecventa
    # :return: returnam subsecventa gasita

    lista_secvente= []
    n = len(lst)
    if n == 1:
        return lst

    for inceput in range(n):
        for sfarsit in range(inceput,n):
            if has_same_div_count(lst[inceput:sfarsit+1]):
                lista_secvente.append(lst[inceput:sfarsit+1])

    maxim = []

    for secventa in lista_secvente:
        if len(secventa) > len(maxim):
            maxim = secventa

    return maxim

def has_all_perfect_squares(list):
    # verifica daca elementele din lista sunt patrate perfecte
    # :param list: subsecventa pe care o verificam
    # :return: returnam true daca elementele sunt patrate perfecte, false in caz contrar

    for element in list:
        if math.sqrt(element) != int(math.sqrt(element)):
            return False
    return True


def get_longest_all_perfect_squares(lst: list[int]) ->list[int]:
    # determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt patrate perfecte
    # :param lst: lista in care cautam subsecventa
    # :return: returnam subsecventa gasita

    lista_secvente = []
    n=len(lst)
    if n == 1:
        return lst

    for inceput in range(n):
        for sfarsit in range(inceput,n):
            if has_all_perfect_squares(lst[inceput:sfarsit+1]):
                lista_secvente.append(lst[inceput:sfarsit+1])

    maxim = []

    for secventa in lista_secvente:
        if len(secventa) > len(maxim):
            maxim = secventa

    return maxim


def same_bit_counts(lista):
    # verifica daca elementele din lista au acelasi numar de biti 1
    # :param lista: subsecventa pe care o verificam
    # :return: true-daca au acelasi numar de biti 1, false in caz contrar

    copie = lista[0]
    aparitii_bit_1 = 0

    while copie != 0:
        cifra = copie % 10
        if cifra == 1:
            aparitii_bit_1 += 1
        copie = copie // 10

    for element in lista:
        aparitii_1 = 0
        while element != 0:
            cifra = element % 10
            if cifra == 1:
                aparitii_1 += 1
            element = element // 10

        if aparitii_bit_1 != aparitii_1:
            return False

    return True


def get_longest_same_bit_counts(lst: list[int]) ->list[int]:
    # determina cea mai lunga subsecventa cu proprietatea ca toate numerele au acelasi numar de biti 1
    # :param lst: lista in care cautam subsecventa
    # :return: returnam subsecventa gasita

    lista_secvente = []
    n = len(lst)

    if n == 1:
        return lst
    for inceput in range(n):
        for sfarsit in range(inceput, n):
            if same_bit_counts(lst[inceput:sfarsit+1]):
                lista_secvente.append(lst[inceput:sfarsit+1])

    maxim = []

    for secventa in lista_secvente:
        if len(secventa) > len(maxim):
            maxim = secventa

    return maxim


def test_get_longest_all_perfect_squares():

    assert get_longest_all_perfect_squares([11, 9, 16, 5, 9, 3, 49]) == [9, 16]
    assert get_longest_all_perfect_squares([3, 4, 5]) == [4]
    assert get_longest_all_perfect_squares([7, 9, 36, 25, 10]) == [9, 36, 25]
    assert get_longest_all_perfect_squares([25]) == [25]



def test_get_longest_same_bit_counts():

    assert get_longest_same_bit_counts([10, 110, 101, 1001, 110]) == [110, 101, 1001, 110]
    assert get_longest_same_bit_counts([101, 10010, 10101, 111]) == [101,10010]
    assert get_longest_same_bit_counts([101, 1111, 1001, 110, 10]) == [1001, 110]
    assert get_longest_same_bit_counts([11, 1111, 1001110, 10101010, 10]) == [1111, 1001110, 10101010]

def test_get_longest_same_div_count():

    assert get_longest_same_div_count([2, 3, 5, 6]) == [2, 3, 5]
    assert get_longest_same_div_count([6, 21, 9, 2]) == [6,21]
    assert get_longest_same_div_count([5]) == [5]
    assert get_longest_same_div_count([12, 5, 10, 15]) == [10, 15]


def main():

    while True:
        print('1. Citire date')
        print('2. Determinare cea mai lunga subsecventa in care toate numerele sunt patrate perfecte')
        print('3. Determinare cea mai lunga subsecventa in care toate numerele au același număr de biți de 1 în reprezentarea binară')
        print('4. Determina cea mai lunga secventa in care toate numerele au acelasi numar de divizori')
        print('x. Iesire din program')
        optiune = input('Alege optiunea')
        if optiune == '1':
            list = citire_lista()
        elif optiune == '2':
            lista_patrate_perfecte = get_longest_all_perfect_squares(list)
            print(lista_patrate_perfecte)
        elif optiune == '3':
            lista_biti_1 = get_longest_same_bit_counts(list)
            print(lista_biti_1)
        elif optiune == '4':
            lista_nr_cu_acelasi_nr_de_divizori = get_longest_same_div_count(list)
            print(lista_nr_cu_acelasi_nr_de_divizori)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')

test_get_longest_same_bit_counts()
test_get_longest_all_perfect_squares()
test_get_longest_same_div_count()
main()
