def calculate_discount(orginal_price, discount_percentage):

    try:
        if orginal_price <0:
            raise ValueError("orginal price cannot be negative.")
        if not (0 <= discount_percentage <=100):
            raise ValueError("Discount percentage must be between 0 and 100.")

            discount_price = orginal_price * (1 - discount_percentage/100) 
            return round(discounted_price, 2)

        except Exception as e:
            print(f"Error: {e}")
            return None