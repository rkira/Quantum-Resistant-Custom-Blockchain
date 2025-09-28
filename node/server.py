from flask import Flask, request, render_template_string, redirect, url_for, jsonify
from blockchain.core import QuantumBlockchain

app = Flask(__name__)
blockchain = QuantumBlockchain()

# List to store pending transaction outputs for display
transactions_output = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
        
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            amount = 0

        # Create a new transaction using the blockchain object
        tx = blockchain.new_transaction(sender, receiver, amount)
        # Append the transaction to our pending list
        transactions_output.append(tx)
        # Redirect to prevent form re-submission on refresh
        return redirect(url_for("index"))
    
    # HTML template with a form and a section to display pending transactions
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Transaction Form</title>
    </head>
    <body>
        <h2>Create a New Transaction</h2>
        <form method="POST">
            <label for="sender">Sender:</label><br>
            <input type="text" id="sender" name="sender" required><br>
            <label for="receiver">Receiver:</label><br>
            <input type="text" id="receiver" name="receiver" required><br>
            <label for="amount">Amount:</label><br>
            <input type="number" id="amount" name="amount" step="any" required><br><br>
            <input type="submit" value="Submit">
        </form>
        <hr>
        <h3>Pending Transactions to be Validated:</h3>
        {% for tx in transactions %}
            <p>Test Transaction: {{ tx }}</p>
        {% else %}
            <p>No pending transactions.</p>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(template, transactions=transactions_output)

@app.route('/chain', methods=['GET'])
def full_chain():
    # Returns the full blockchain and its length
    return jsonify({'chain': blockchain.chain, 'length': len(blockchain.chain)}), 200

@app.route('/mine', methods=['GET'])
def mine():
    # Mine a new block which validates the pending transactions
    block = blockchain.mine_block()
    # Clear the pending transactions once they're validated (mined)
    transactions_output.clear()
    return jsonify(block), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
