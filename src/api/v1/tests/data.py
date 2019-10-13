bad_arguments = [
    {
        'DE_capacity': 10,
        'data_centers': [{'name': 'Paris', 'servers': 10}],
    },
    {
        'DM_capacity': 10,
        'data_centers': [{'name': 'Paris', 'servers': 10}],
    },
    {
        'DM_capacity': 8,
        'DE_capacity': 5,
        'data_centers': [{'city': 'Paris', 'servers': 10}, {'name': 'Stockholm', 'servers': 20}]
    },
    {
        'DM_capacity': -8,
        'DE_capacity': 5,
        'data_centers': [{'name': 'Stockholm', 'servers': 20}]
    },
    {
        'DM_capacity': 1,
        'DE_capacity': 0,
        'data_centers': [{'name': 'Stockholm', 'servers': 20}]
    }
]
