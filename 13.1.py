from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:num>', methods=['GET'])
def check_prime_number(num):
    """Check if the given number is prime."""
    if is_prime(num):
        return jsonify({"Number": num, "isPrime": True})
    else:
        return jsonify({"Number": num, "isPrime": False})

if __name__ == '__main__':
    app.run(debug=True)