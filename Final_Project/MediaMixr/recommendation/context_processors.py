import sys
sys.path.append("..")

def interests(request):
    from accounts.models import Interest
    return {'interests':Interest.objects.all()}
def genres(request):
    from recommendation.models import Genre
    return {'genres':Genre.objects.all()}