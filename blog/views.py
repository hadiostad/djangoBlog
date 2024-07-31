from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "microsoft-will-pay",
        "image": "microsoft.webp",
        "author": "Hadi Ostad",
        "date": date(2024, 7, 30),
        "title": "Microsoft News",
        "excerpt": "Microsoft tells employees it will pay one-time cash awards of up",
        "content": """
          Microsoft on Tuesday said it will pay a one-time performance-based cash award of up to 25% of annual bonus to rank-and-file employees.
          Salaried and hourly workers at the senior director level and below will be eligible for the award, Kathleen Hogan, Microsoft’s chief people officer, said in a memo distributed to employees. Junior-level employees can obtain an award amounting to as much as 25% of their bonus, while senior directors can get up to 10%.
          Hogan said in the memo that Microsoft’s leaders want to show recognition to workers for a good fiscal year. Microsoft reported fourth-quarter results after the close of trading on Tuesday, and said revenue increased 15% from a year earlier. For the full fiscal year, which ended June 30, revenue climbed about 16%, accelerating from 7% in fiscal 2023.
        """
    },
    {
        "slug": "apple-iphone-ai",
        "image": "Apple.webp",
        "author": "Hadi Ostad",
        "date": date(2024, 7, 29),
        "title": "Apple iPhone AI!",
        "excerpt": "Apple releases first preview of its long-awaited iPhone AI",
        "content": """
            Apple on Monday released the first version of Apple Intelligence, its suite of
            artificial intelligence features that will improve Siri, automatically generate
            emails and images and sort notifications.

            The new software called Apple Intelligence was released in the developer beta of
            iOS 18.1. It is also available in similar releases for iPad and Mac. It is
            currently available for developers to test.

            In addition, users will have to register for a waitlist inside Apple’s
            settings app after updating to gain access to the service, which involves
            pinging Apple servers for more complicated requests.
        """
    },
    {
        "slug": "Samsung-second-quarter",
        "image": "samsung.webp",
        "author": "Hadi Ostad",
        "date": date(2024, 7, 30),
        "title": "Samsung quarter",
        "excerpt": "Samsung second-quarter operating profit soars 1,458%",
        "content": """
            The South Korean giant said robust demand for high-bandwidth as well as
            conventional memory, such as regular dynamic random access memory, from
            customers expanding AI investments contributed to the strong performance.

            For the second half, Samsung said it expects the demand from server AI to
            stay strong across server products including HBM, server DRAM and SSD. SSD,
            or solid-state drive, refers to a semiconductor-based storage device.
        """
    }
]


def get_date(post):
    return post['date']


def main_page(request):
    #sorted_posts = all_posts.sort(key=get_date)
    #latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        "posts": all_posts
    })


def posts(request):
    return render(request, 'blog/posts.html')


def single_post(request, slug):
    return render(request, 'blog/single-post.html')
