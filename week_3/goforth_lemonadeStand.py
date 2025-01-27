"""
Author: Caleb Goforth 
Date: 1/26/2025
File Name: goforth_lemonadeStand.py
Description: A Python program that simulates a lemonade stand by calculating the cost 
and profit of making and selling lemonade.
"""

# Function to calculate the cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    """
    Calculates the total cost of making lemonade.
    Parameters:
        lemons_cost (float): Cost of lemons.
        sugar_cost (float): Cost of sugar.
    Returns:
        float: Total cost of making lemonade.
    """
    total_cost = lemons_cost + sugar_cost  # Summing up lemons and sugar cost
    return total_cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    """
    Calculates the profit from selling lemonade.
    Parameters:
        lemons_cost (float): Cost of lemons.
        sugar_cost (float): Cost of sugar.
        selling_price (float): Selling price of the lemonade.
    Returns:
        float: Profit from selling lemonade.
    """
    total_cost = calculate_cost(lemons_cost, sugar_cost)  # Get the total cost
    profit = selling_price - total_cost  # Profit is selling price minus cost
    return profit

# Main section to test the functions
if __name__ == "__main__":
    # Variables for cost and selling price
    lemons_cost = 4.0  # Cost of lemons in dollars
    sugar_cost = 2.0   # Cost of sugar in dollars
    selling_price = 10.0  # Selling price of lemonade in dollars

    # Calculating the total cost
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    
    # Calculating the profit
    profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

    # Formatting the results as strings
    cost_result = f"({lemons_cost}) + ({sugar_cost}) = ({total_cost})"
    profit_result = f"Selling Price ({selling_price}) - Total Cost ({total_cost}) = Profit ({profit})"

    # Outputting the results
    print("Cost Calculation:")
    print(cost_result)
    print("\nProfit Calculation:")
    print(profit_result)
