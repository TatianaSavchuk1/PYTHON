# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - 
# стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = 5
b = 3
c = 4

if a + b > c and a + c > b and b + c > a:
    print('треугольник существует')
    if a == b == c:
        print('и он - равносторонний')
    elif a == b and a!= c or b == c and b != a or a == c and a != b:
        print('и он - равнобедненный')
    else:
        print('и он - разносторонний')
else:
    print('такой треугольник существовать не может')