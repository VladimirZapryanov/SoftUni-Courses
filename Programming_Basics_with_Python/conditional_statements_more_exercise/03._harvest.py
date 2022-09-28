from math import floor, ceil


def harvest(vineyard, grapes_from_one_meter, needed_wine, workers, vineyard_percent_for_wine, grape_for_one_litter_wine):
    all_grape = vineyard * grapes_from_one_meter
    grape_for_wine = all_grape * vineyard_percent_for_wine
    produced_wine = grape_for_wine / grape_for_one_litter_wine
    wine_difference = produced_wine - needed_wine

    if produced_wine >= needed_wine:
        wine_per_person = wine_difference / workers
        return f'Good harvest this year! Total wine: {floor(produced_wine)} liters.\n{ceil(wine_difference)} liters left -> {ceil(wine_per_person)} liters per person.'
    else:
        return f'It will be a tough winter! More {(floor(abs(wine_difference)))} liters wine needed.'


vineyard = int(input())
grapes_from_one_meter = float(input())
needed_wine = int(input())
workers = int(input())

vineyard_percent_for_wine = 0.4
grape_for_one_litter_wine = 2.5

print(harvest(vineyard, grapes_from_one_meter, needed_wine, workers, vineyard_percent_for_wine, grape_for_one_litter_wine))