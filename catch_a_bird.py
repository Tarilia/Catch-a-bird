import numpy as np


class CatAndBird:
    def __init__(self, weight):
        self.weight = weight

    def activate(self, factor):
        return 1 / (1 + np.exp(-factor))

    def to_summarize(self, factor):
        result = np.dot(self.weight, factor)
        return result


def main():
    print('Сможет ли кошка поймать птичку?')
    print('Зависит от нескольких факторов:')
    print('Наличие кошки')
    print('Наличие птички')
    print('Здоровье кошки')
    print('Болезнь птички')
    print('Птичка в кошкиной доступности')
    print('У птички нет укрытия')
    print('У птички нет защитников')

    assessment_of_factors = input('Оцените каждый фактор(0 - нет, 1 - да), '
                                  'запишите одной строкой через пробел: ')
    assessment_of_factors = list(map(int, assessment_of_factors.split()))
    weight = [5, 5, 3, 3, 3, 1, 1]
    cat_and_bird = CatAndBird(weight)
    bias = 7
    result_sum = cat_and_bird.to_summarize(assessment_of_factors) - bias
    the_result_of_the_capture = cat_and_bird.activate(result_sum)

    print(f'Кошка сможет поймать птичку с вероятностью в '
          f'{the_result_of_the_capture:.2f}%')


if __name__ == "__main__":
    main()
