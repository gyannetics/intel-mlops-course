# maintenance test business logic

def test_maintenance(temperature: int, hydraulic_pressure: int):
    """Tests if maintenance is needed based on temperature and hydraulic pressure readings.

    Parameters
    ----------
    temperature : int
        Test parameter for temperature sensor readings.
    hydraulic_pressure : int
        Test parameter for hydraulic pressure readings.

    Returns
    -------
    str
        'Needs Maintenance' or 'No Maintenance Required' based on readings.
    """
    if temperature > 50 or hydraulic_pressure > 2000:
        maintenance_status = 'Needs Maintenance'
    else:
        maintenance_status = 'No Maintenance Required'
    
    return maintenance_status
