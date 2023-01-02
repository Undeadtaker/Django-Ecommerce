from .basket import Basket

# Returns the store session
def basket(req):
    return {'basket': Basket(req)}