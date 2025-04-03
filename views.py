from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player
import json

@csrf_exempt
def get_player(request, username):
    if request.method == 'GET':
        try:
            player = Player.objects.get(username=username)
            return JsonResponse({
                'status': 'success',
                'player': {
                    'username': player.username,
                    'highscore': player.highscore
                }
            })
        except Player.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Player not found'
            }, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})

@csrf_exempt
def register_player(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            if not username:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Username is required'
                }, status=400)
            
            player, created = Player.objects.get_or_create(
                username=username,
                defaults={'highscore': 0}
            )
            return JsonResponse({
                'status': 'success',
                'player': {
                    'username': player.username,
                    'highscore': player.highscore,
                    'is_new': created
                }
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})

@csrf_exempt
def update_highscore(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            score = data.get('score')
            
            if not username or score is None:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Username and score are required'
                }, status=400)
            
            player = Player.objects.get(username=username)
            if score > player.highscore:
                player.highscore = score
                player.save()
            
            return JsonResponse({
                'status': 'success',
                'player': {
                    'username': player.username,
                    'highscore': player.highscore
                }
            })
        except Player.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Player not found'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})

@csrf_exempt
def get_all_players(request):
    if request.method == 'GET':
        try:
            players = Player.objects.all().order_by('-highscore')
            return JsonResponse({
                'status': 'success',
                'players': [
                    {
                        'username': player.username,
                        'highscore': player.highscore
                    }
                    for player in players
                ]
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})