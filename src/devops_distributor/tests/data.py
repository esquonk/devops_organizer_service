from devops_distributor.distributor import DataCenter

test_data = [
    # data from challenge
    (20, 8, [DataCenter('Paris', 20), DataCenter('Stockholm', 62)], 'Paris', 8),
    (6, 10, [DataCenter('Paris', 30), DataCenter('Stockholm', 66)], 'Stockholm', 9),
    (12, 7, [DataCenter('Berlin', 11), DataCenter('Stockholm', 21)], 'Berlin', 3),

]
