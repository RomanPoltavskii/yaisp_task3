# Отрезок на прямой линии задается координатой начала A и координатой окончания B
# (точки начала и окончания отрезка принадлежат отрезку). Задан набор отрезков, которые
# могут накладываться друг на друга. Необходимо среди заданного набора отрезков найти два отрезка,
# сумма длин объединения которых будет максимальной (здесь возможны два варианта, если эти два отрезка
# не пересекались, то объединение будет состоять из этих же двух отрезков,
# если же отрезки пересекались, то их объединением будет один отрезок).

def read_segments(path):
    segments = LineSegments()
    with open(path) as f:
        for line in f:
            a, b = map(int, line.split())
            segments.add(LineSegment(a, b))
    return segments


class LineSegment:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_length(self):
        return abs(self.b - self.a)

    def __lt__(self, other):
        return self.a < other.a

    def __str__(self):
        return f"[{self.a}, {self.b}]"


class LineSegments:
    def __init__(self):
        self.segments = []

    def add(self, segment):
        self.segments.append(segment)


    def find_maximum_combined_length(self):
        n = len(self.segments)
        self.segments.sort()
        max_length = 0
        max_segments = None
        for i in range(n):
            for j in range(i + 1, n):
                if self.segments[j].a <= self.segments[i].b:  # проверяем, пересекаются ли отрезки
                    combined_length = (self.segments[i].get_length() +
                                       self.segments[j].get_length() -
                                       (self.segments[j].a - self.segments[i].b))
                    if combined_length > max_length:
                        max_length = combined_length
                        max_segments = (self.segments[i], self.segments[j])
        return max_segments

    def __str__(self):
        return ", ".join(str(segment) for segment in self.segments)


# Создаем список отрезков
segments = read_segments('input.txt')

# Находим два отрезка с максимальной суммой длин объединения
max_segments = segments.find_maximum_combined_length()

# Записываем результат в файл
with open("output.txt", "w") as f:
    f.write(f"Отрезки: {segments}\n")
    f.write(f"Два отрезка с максимальной суммой длин объединения: {max_segments[0]}, {max_segments[1]}\n")
    f.write(f"Сумма длин объединения: {max_segments[0].get_length() + max_segments[1].get_length() - (max_segments[1].a - max_segments[0].b)}\n")