# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1 Greet Template
def greet(name, greeting_template="Hello, <name>!"):
    return greeting_template.replace("<name>", name)

# Part 2 Force
def force(mass, body='earth'):
    # Round the gravity factor to 1 decimal
    bodies = {
        'mercury': 3.7,
        'venus': 8.87,
        'earth': 9.8,
        'mars': 3.71,
        'jupiter': 24.79,
        'saturn': 10.44,
        'uranus': 8.69,
        'neptune': 11.15,
        'pluto': 0.62,
        'moon': 1.62,
        'sun': 274.0
    }
    gravity = round(bodies[body], 1)
    return mass * gravity

    
# Part 3 Gravity
def pull(m1, m2, d):
    G = 6.674 * 10 ** -11
    pull = G * ((m1 * m2) / d ** 2)
    return pull


    