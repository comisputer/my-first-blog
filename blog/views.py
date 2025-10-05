from django.shortcuts import render
from django.http import JsonResponse


# def post_list(request):
#     return HttpResponse("Blog index is working.")

def post_list(request):
    return render(request, 'blog/post_list.html', {})


def chart_data(request):
    """Return JSON data for a mixed bar + line chart."""
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    bar_values = [120, 180, 130, 160, 210, 190]
    line_values = [100, 150, 140, 170, 200, 220]

    return JsonResponse(
        {
            "labels": labels,
            "bar": {
                "name": "Sales",
                "values": bar_values,
            },
            "line": {
                "name": "Forecast",
                "values": line_values,
            },
        }
    )


def chart_page(request):
    return render(request, 'blog/chart.html')


def chartjs_polar_page(request):
    return render(request, 'blog/chartjs_polar.html')