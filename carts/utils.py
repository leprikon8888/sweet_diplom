from carts.models import Cart


def get_user_carts(request):
    """A function that retrieves user carts based on the given request object.
    Parameters:
    - request: The request object containing user authentication and session information """
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product')

    if not request.session.session_key:
        request.session.create()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')

