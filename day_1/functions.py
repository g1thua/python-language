def apply_discount (price , discount) :
    if not isinstance(price, (int,float)):
        print ('The price should be a number')
        return None
    if not isinstance(discount, (int, float)):
        print ('The discount should be a number')
        return None
    if price <= 0:
        print('The price should be greater than 0')     
        return None
    if discount < 0 or discount > 100:
        print('The discount should be between 0 and 100')
        return None
    if price > 0 and (discount > 0 and discount < 100):
        final_price = price - (discount/100 * price)
    print(final_price)
    return final_price   
apply_discount('1500', 20)
