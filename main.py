# ...existing code...
from pyscript import display, document


def intrams_checker(e):
    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML = ''
    
    reg_elem = document.querySelector('input[name="registration"]:checked')
    clear_elem = document.querySelector('input[name="clearance"]:checked')
    level_elem = document.getElementById('level')
    section_elem = document.getElementById('section')

    if reg_elem is None:
        display('Not eligible: Missing student registration. Please inquire your PE teacher!', target='output')
        return
    if clear_elem is None:
        display('Not eligible: Missing medical clearance. Please fetch it from the clinic!', target='output')
        return

    registration = reg_elem.value
    clearance = clear_elem.value

    try:
        grade_level = int(level_elem.value) if level_elem and level_elem.value.strip() != '' else None
    except Exception:
        grade_level = None

    section = section_elem.value.lower() if section_elem and section_elem.value else ''

    if registration != 'registered':
        display('Not eligible: Missing student registration. Please inquire your PE teacher!', target='output')
    elif clearance != 'cleared':
        display('Not eligible: Missing medical clearance. Please fetch it from the clinic!', target='output')
    elif section == 'emerald':
        display('Congratulations! You are part of the Green Hornets', target='output')
        document.getElementById('image').innerHTML = '<img src="green_hornets.jpg" width="400" height="400">'
    elif section == 'ruby':
        display('Congratulations! You are part of the Yellow Tigers', target='output')
        document.getElementById('image').innerHTML = '<img src="yellow_tigers.jpg" width="400" height="400">'
    elif section == 'sapphire':
        display('Congratulations! You are part of the Blue Bears', target='output')
        document.getElementById('image').innerHTML = '<img src="blue_bears.jpg" width="400" height="400">'
    else:
        display('Congratulations! You are part of the Red Bulldogs', target='output')
        document.getElementById('image').innerHTML = '<img src="red_bulldogs.jpg" width="400" height="400">'
# ...existing code...