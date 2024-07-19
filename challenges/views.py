from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseRedirect

challenges_map = {
    'january': "Reading Challenge",
    'february': "Acts of Kindness Challenge",
    'march': "Fitness Challenge",
    'april': "Hydration Challenge",
    'may': "Art Challenge",
    'june': "Digital Detox Challenge",
    'july': "Decluttering Challenge",
    'august': "Gratitude Challenge",
    'september': "Skill-building Challenge",
    'november': "Financial Challenge",
    'december': "Self-care Challenge",
}


def monthly_challenge_by_number(request, month: int):
    try:
        months = list(challenges_map.keys())
        redirect_month = months[month - 1]
        return HttpResponseRedirect('/challenges/' + redirect_month)
    except Exception as e:
        return HttpResponseNotFound(e)

def monthly_challenge(request, month: str):
    try:
        msg = challenges_map.get(month.lower())
        return HttpResponse(msg)
    except Exception as e:
        print(e)
        return HttpResponseNotFound('This month is not supported!')
