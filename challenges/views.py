from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

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


def index(request):
    # msg_body = '<ul>'
    months = list(challenges_map.keys())
    # for idx, name in enumerate(months):
    #     redirect_month = months[idx]
    #     redirect_path = reverse('month-challenge', args=[redirect_month])
    #     msg_body += f"\n<li><a href={redirect_path}>{name}</a></li>"
    # msg_body += '</ul>'
    return render(
        request,
        "challenges/index.html",
        {
            'page_name': 'all challenges',
            'months_list': months,
        },
    )


def monthly_challenge_by_number(request, month: int):
    try:
        months = list(challenges_map.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except Exception as e:
        return HttpResponseNotFound(e)


def monthly_challenge(request, month: str):
    try:
        msg = challenges_map.get(month.lower())
        return render(request, "challenges/challenge.html", {
                'month': month,
                'text': msg,
            },
            )
    except Exception as e:
        return HttpResponseNotFound(f'This month is not supported!\n{e}')
